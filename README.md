# 🚀 EmpowerWork

**AI-Powered Inclusive Employment Platform for People with Disabilities**

---

## 📋 Overview

EmpowerWork is a full-stack web platform that leverages AI and assistive technologies to bridge employment gaps for people with disabilities. Built as a graduation project, it provides real-time sign language interpretation, AI-driven accessibility tools, and inclusive hiring resources.

---

## ✨ Features

### Core Functionality
- **🤖 AI Chatbot** - Groq-powered assistant for guidance and support
- **👋 Live ASL Detection** - Real-time sign language recognition via webcam
- **📸 Image Detection** - Computer vision for accessibility assessment
- **♿ Inclusive Tools** - Text-to-speech, keyboard navigation, screen-reader support
- **🎯 Smart Recruitment** - AI filters to reduce bias in candidate selection

### Tech Stack
- **Frontend**: HTML5, CSS3, Vanilla JS, GSAP animations, Swiper.js
- **Backend**: Flask (Python), Groq AI API, Roboflow (ASL detection)
- **Deployment**: GitHub Pages (frontend), Modal.com (backend)

---

## 🏗️ Project Structure

```
EmpowerWork/
├── frontend/
│   ├── public/
│   │   ├── index.html          # Landing redirect
│   │   ├── home-1.html         # Main homepage
│   │   ├── service.html        # Services & tools
│   │   ├── sign-in.html        # Authentication
│   │   ├── sign-up.html        # Registration
│   │   ├── css/                # Styles
│   │   ├── js/                 # Client-side logic
│   │   └── img/                # Assets
│   └── views/                  # Templates (future)
├── backend/
│   ├── server/                 # Flask app
│   ├── api/                    # API endpoints
│   ├── models/                 # Data models
│   └── middleware/             # Auth, validation, etc.
├── docs/
│   ├── deployment/             # Deployment guides
│   ├── api/                    # API documentation
│   └── arch/                   # Architecture & design
└── package.json                # Project config
```

---

## 🚀 Quick Start

### Prerequisites
- Node.js 14+
- Python 3.10+
- Modern browser with camera access

### Installation

```bash
# Clone repository
git clone <repo-url>
cd Graduation-502-main

# Install dependencies
npm install

# Start frontend server
npm start

# Start backend (in separate terminal)
cd backend/server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Configuration

Update `frontend/public/js/config.js`:
```javascript
window.__ASL_CONFIG__ = {
    BACKEND_URL: 'https://your-backend.modal.run'
};
```

---

## 🔧 Development

### Frontend
- **Entry**: `frontend/public/home-1.html`
- **Styles**: `frontend/public/css/`
- **Scripts**: `frontend/public/js/`

### Backend
- **App**: `backend/server/app.py`
- **Endpoints**: `/health`, `/detect`, `/chat`

---

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/detect` | POST | Image/ASL detection |
| `/detect-frame` | POST | Live webcam detection |
| `/predict-video` | POST | Video processing |
| `/chat` | POST | AI chatbot responses |

---

## 🎨 Design System

- **Primary**: `#21899F` (Pharos Blue)
- **Accent**: `#F7941E` (Wisdom Gold)
- **Dark**: `#0b1220` (Midnight Navy)
- **Typography**: Inter (headings), Roboto (body)

---

## 🤝 Team

- **Khaled Ghalwash** - Full Stack Developer, ML Specialist
- **Rawan Mohamed** - Machine Learning Engineer
- **Mohamed Gamal** - Embedded Systems
- **Mohamed Hassan** - Embedded Systems
- **Mazen** - Cybersecurity, Backend Dev
- **Naden** - Cybersecurity

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

- Groq for AI chat capabilities
- Roboflow for computer vision models
- Modal.com for scalable backend hosting

---

## 📈 Roadmap

- [ ] User authentication & profiles
- [ ] Job posting & application system
- [ ] Multi-language ASL support
- [ ] Mobile app (React Native)
- [ ] Enterprise dashboard
- [ ] Analytics & reporting

---

## 📧 Contact

**Email**: support@empowerwork.ai  
**Location**: Alexandria, Egypt

---

*Built with ❤️ for inclusive employment*
# k
