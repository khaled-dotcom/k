# 🚀 Deployment Guide

## Overview

EmpowerWork uses a **serverless backend** (Modal.com) and **static frontend hosting** (GitHub Pages).

---

## Frontend Deployment (GitHub Pages)

### Prerequisites
- GitHub account
- Repository created

### Steps

1. **Push code to GitHub**
```bash
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

2. **Enable GitHub Pages**
- Go to: Repository Settings → Pages
- Source: Deploy from `main` branch
- Folder: `/root` (or configure build)

3. **Update Backend URL**
Edit `frontend/public/js/config.js`:
```javascript
window.__ASL_CONFIG__ = {
    BACKEND_URL: 'https://your-backend.modal.run'
};
```

4. **Verify**
Visit: `https://yourusername.github.io/your-repo/`

---

## Backend Deployment (Modal.com)

### Prerequisites
- Modal account
- Roboflow API key
- Groq API key

### Setup

1. **Install Modal CLI**
```bash
pip install modal
modal token new
```

2. **Deploy**
```bash
cd backend
modal deploy app.py
```

3. **Get URL**
Copy the deployed URL: `https://[your-name]--[service].modal.run`

4. **Environment Variables**
```bash
modal secret create empowerwork-secrets \
  GROQ_API_KEY=your_key \
  ROBOFLOW_API_KEY=your_key
```

---

## Alternative: Traditional Server

### Requirements
- Python 3.10+
- Node.js 14+

### Backend
```bash
cd backend/server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
npm install
npm start
```

---

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GROQ_API_KEY` | Groq AI API key | `gsk_...` |
| `ROBOFLOW_API_KEY` | Roboflow API key | `rf_...` |
| `PORT` | Backend port | `5000` |
| `FLASK_ENV` | Flask mode | `production` |

---

## SSL/HTTPS

For production:
- GitHub Pages: Automatic HTTPS
- Custom domain: Add in settings
- Modal: HTTPS by default

---

## Monitoring

- **Health Check**: `GET /health`
- **Logs**: Modal dashboard or server logs
- **Errors**: Check browser console + server logs

---

## Troubleshooting

**CORS Errors**: Ensure backend allows frontend origin

**API Keys**: Verify secrets are set correctly

**500 Errors**: Check server logs for details

**Slow Responses**: Cold starts on Modal; warm endpoints first

---

*Last updated: January 2025*

