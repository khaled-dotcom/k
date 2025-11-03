# 🚀 Modal.com Deployment Guide

## EmpowerWork ASL Detection Backend on Modal.com

This guide will help you deploy the EmpowerWork sign language detection backend to Modal.com.

---

## Prerequisites

1. **Modal Account**: Sign up at [modal.com](https://modal.com)
2. **Modal CLI**: Install with `pip install modal`
3. **API Keys**: You'll need your Modal token

---

## Quick Start

### 1. Install Modal CLI

```bash
pip install modal
modal token new
```

This will open your browser to authenticate.

### 2. Navigate to Backend Directory

```bash
cd backend
```

### 3. Deploy to Modal

```bash
modal deploy modal_app.py
```

### 4. Get Your Deployment URL

After deployment, Modal will give you a URL like:
```
https://your-username--empowerwork-backend-flask-app.modal.run
```

---

## Configuration

### Update Frontend

Edit `frontend/public/js/config.js`:

```javascript
window.__ASL_CONFIG__ = {
    BACKEND_URL: 'https://your-username--empowerwork-backend-flask-app.modal.run'
};
```

---

## Testing the Deployment

### Health Check

```bash
curl https://your-username--empowerwork-backend-flask-app.modal.run/health
```

Expected response:
```json
{
  "status": "ok",
  "message": "EmpowerWork API is running",
  "features": ["asl_detection", "chat"]
}
```

### Test ASL Detection

```bash
curl -X POST https://your-username--empowerwork-backend-flask-app.modal.run/detect-frame \
  -H "Content-Type: application/json" \
  -d '{"frame": "data:image/jpeg;base64,/9j/4AAQ..."}'
```

---

## Environment Variables

If you need to set environment variables in Modal:

```bash
modal secret create empowerwork-secrets \
  GROQ_API_KEY=your_groq_key \
  OTHER_VAR=value
```

Then update `modal_app.py` to use the secret:

```python
@app.function(image=image, secrets=[modal.Secret.from_name("empowerwork-secrets")])
```

---

## Local Testing

Test your Modal app locally:

```bash
modal run modal_app.py::main
```

This runs your Flask app locally for testing.

---

## Monitoring

### Logs

```bash
modal app logs empowerwork-backend
```

### Metrics

Visit Modal dashboard to see:
- Request latency
- Cold start times
- Error rates
- Resource usage

---

## Troubleshooting

### Cold Start Delays

Modal apps have cold starts on first request. Use `keep_warm=1` in `modal_app.py`:

```python
@app.function(image=image, keep_warm=1)
```

### CORS Issues

Ensure `flask-cors` is installed and enabled in `app.py`:

```python
from flask_cors import CORS
CORS(app)
```

### Model Loading Issues

Check that `hand_gesture_classifier.joblib` is in `backend/server/artifacts/`:

```bash
ls -lh backend/server/artifacts/
```

### Import Errors

Ensure all dependencies are in `pyproject.toml` and `requirements.txt`.

---

## Deployment Workflow

```bash
# 1. Make changes to code
# 2. Test locally
modal run modal_app.py::main

# 3. Deploy
modal deploy modal_app.py

# 4. Check logs
modal app logs empowerwork-backend

# 5. Update frontend config if URL changed
# Edit frontend/public/js/config.js
```

---

## Production Considerations

1. **Scaling**: Modal auto-scales based on demand
2. **Costs**: Pay only for compute time used
3. **Security**: Use Modal secrets for API keys
4. **Monitoring**: Set up alerts in Modal dashboard
5. **Backups**: Keep local copies of all code and models

---

## Support

- **Modal Docs**: https://modal.com/docs
- **Community**: Modal Discord
- **Issues**: GitHub Issues

---

**Ready to deploy! 🚀**

