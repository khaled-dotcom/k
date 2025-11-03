# ⚡ Quick Start Guide

Get EmpowerWork running in 5 minutes!

---

## 1️⃣ Clone & Install

```bash
git clone <your-repo-url>
cd Graduation-502-main
npm install
```

---

## 2️⃣ Backend Setup

```bash
cd backend/server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
echo "GROQ_API_KEY=your_key" > .env
echo "ROBOFLOW_API_KEY=your_key" >> .env

# Run backend
python app.py
```

✅ Backend running at `http://localhost:5000`

---

## 3️⃣ Frontend Setup

In a new terminal:

```bash
npm start
```

✅ Frontend at `http://localhost:3000`

---

## 4️⃣ Configure

Edit `frontend/public/js/config.js`:

```javascript
window.__ASL_CONFIG__ = {
    BACKEND_URL: 'http://localhost:5000'
};
```

---

## 5️⃣ Test

- Visit homepage: `http://localhost:3000/home-1.html`
- Try the chatbot
- Upload image for detection
- Test ASL webcam detection

---

## 🚀 Deploy to Production

See `docs/deployment/README.md` for:
- GitHub Pages (frontend)
- Modal.com (backend)
- Environment variables
- SSL/HTTPS setup

---

## ❓ Troubleshooting

**Port already in use?**
```bash
# Backend: Change PORT in .env
# Frontend: Different port in package.json
```

**CORS errors?**
- Check backend allows frontend origin
- Verify CORS middleware enabled

**API keys?**
- Get Groq key: https://groq.com
- Get Roboflow key: https://roboflow.com

---

**Ready! 🎉**

Need help? Check `README.md` or open an issue.

