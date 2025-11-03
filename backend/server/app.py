"""
EmpowerWork Backend Server - Modal.com Ready
Flask API with Sign Language Detection (MediaPipe + Scikit-learn)
"""

import base64
import io
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import cv2
import numpy as np

# Import ASL detection modules
import sys
# Add parent directory to path for imports
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

try:
    from src.preprocessing import HandPreprocessor
    from src.inference import GestureClassifier
except ImportError as e:
    print(f"Warning: Could not import ASL modules: {e}")
    HandPreprocessor = None
    GestureClassifier = None

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')

# Initialize ASL detection components (lazy load for Modal cold starts)
preprocessor = None
classifier = None

def get_detection_components():
    """Lazy initialization of detection components"""
    global preprocessor, classifier
    if HandPreprocessor is None or GestureClassifier is None:
        raise RuntimeError("ASL detection modules not available")
    if preprocessor is None:
        print("Initializing MediaPipe preprocessor...")
        preprocessor = HandPreprocessor()
    if classifier is None:
        print("Initializing gesture classifier...")
        classifier = GestureClassifier()
    return preprocessor, classifier

def base64_to_image(base64_string):
    """Convert base64 string to OpenCV image"""
    try:
        # Remove data URL prefix if present
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        # Decode base64
        image_data = base64.b64decode(base64_string)
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print(f"Error decoding base64: {e}")
        return None

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "ok",
        "message": "EmpowerWork API is running",
        "features": ["asl_detection", "chat"]
    })

@app.route('/chat', methods=['POST'])
def chat():
    """AI chatbot endpoint (Groq-powered)"""
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # TODO: Implement Groq API integration
        response = f"Echo: {message}"
        
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/detect', methods=['POST'])
def detect():
    """Image/sign language detection endpoint"""
    try:
        data = request.json
        image_url = data.get('image_url')
        image_base64 = data.get('image_base64')
        
        if not image_url and not image_base64:
            return jsonify({"error": "image_url or image_base64 required"}), 400
        
        # Get detection components
        preprocessor, classifier = get_detection_components()
        
        # Load image
        if image_base64:
            img = base64_to_image(image_base64)
        elif image_url:
            # TODO: Load from URL
            return jsonify({"error": "URL loading not yet implemented"}), 501
        else:
            return jsonify({"error": "No image data provided"}), 400
        
        if img is None:
            return jsonify({"error": "Failed to decode image"}), 400
        
        # Process frame
        landmarks, vis_frame = preprocessor.process_frame(img)
        prediction = "No Gesture Detected"
        confidence = 0.0
        
        if landmarks is not None:
            gesture, confidence = classifier.predict(landmarks)
            if gesture is not None:
                prediction = gesture
        
        return jsonify({
            "detected": prediction != "No Gesture Detected",
            "sign": prediction,
            "confidence": float(confidence)
        })
    
    except Exception as e:
        print(f"Error in /detect: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/detect-frame', methods=['POST'])
def detect_frame():
    """Live webcam frame detection"""
    try:
        data = request.json
        frame = data.get('frame') or data.get('image_base64')
        
        if not frame:
            return jsonify({"error": "frame data required"}), 400
        
        # Get detection components
        preprocessor, classifier = get_detection_components()
        
        # Convert base64 to image
        img = base64_to_image(frame)
        if img is None:
            return jsonify({"error": "Failed to decode frame"}), 400
        
        # Process frame
        landmarks, vis_frame = preprocessor.process_frame(img)
        prediction = "No Gesture Detected"
        confidence = 0.0
        
        if landmarks is not None:
            gesture, confidence = classifier.predict(landmarks)
            if gesture is not None:
                prediction = gesture
        
        return jsonify({
            "detected": prediction != "No Gesture Detected",
            "sign": prediction,
            "confidence": float(confidence)
        })
    
    except Exception as e:
        print(f"Error in /detect-frame: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/predict-video', methods=['POST'])
def predict_video():
    """Video upload and prediction endpoint"""
    try:
        if 'video' not in request.files:
            return jsonify({"error": "video file required"}), 400
        
        video = request.files['video']
        
        # Get detection components
        preprocessor, classifier = get_detection_components()
        
        # Read video
        video_path = f"/tmp/{video.filename}"
        video.save(video_path)
        
        cap = cv2.VideoCapture(video_path)
        predictions = []
        frame_count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process every 30th frame (adjust as needed)
            frame_count += 1
            if frame_count % 30 == 0:
                landmarks, vis_frame = preprocessor.process_frame(frame)
                if landmarks is not None:
                    gesture, confidence = classifier.predict(landmarks)
                    if gesture is not None:
                        predictions.append({
                            "frame": frame_count,
                            "sign": gesture,
                            "confidence": float(confidence)
                        })
        
        cap.release()
        os.remove(video_path)
        
        return jsonify({
            "status": "processed",
            "predictions": predictions
        })
    
    except Exception as e:
        print(f"Error in /predict-video: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    print(f"Starting EmpowerWork server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
