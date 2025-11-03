"""
EmpowerWork Modal.com Deployment
Serverless ASL Detection Backend
"""

import modal
from pathlib import Path

# Define Modal image with all dependencies
image = (
    modal.Image.debian_slim(python_version="3.10")
    .pip_install_from_pyproject("requirements.txt")
    .copy_local_dir("server", "/root/server")
)

app = modal.App("empowerwork-backend")

@app.function(image=image, keep_warm=1)
@modal.wsgi_app()
def flask_app():
    """Run Flask app in Modal"""
    import sys
    sys.path.insert(0, "/root/server")
    
    from server.app import app
    
    # Monkey-patch for WSGI compatibility
    return app

@app.local_entrypoint()
def main():
    """For local testing"""
    from server.app import app
    app.run(host="0.0.0.0", port=8000, debug=True)

