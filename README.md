#  EmpowerWork

**AI-Powered Inclusive Employment Platform for People with Disabilities**

---

##  Overview

EmpowerWork is a full-stack web platform that leverages AI and assistive technologies to bridge employment gaps for people with disabilities. Built as a graduation project, it provides real-time sign language interpretation, AI-driven accessibility tools, and inclusive hiring resources.

---

### Tech Stack
- **Frontend**: HTML5, CSS3, Vanilla JS, GSAP animations, Swiper.js
- **Backend**: Flask (Python), Groq AI API, Roboflow (ASL detection)
- **Deployment**: GitHub Pages (frontend), Modal.com (backend)

---

##  Project Structure

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


##  Design System

- **Primary**: `#21899F` 
- **Accent**: `#F7941E` 
- **Dark**: `#0b1220` 
- **Typography**: Inter (headings), Roboto (body)

---

##  Team

- **Khaled Ghalwash** - Full Stack Developer, ML Specialist
- **Rawan Mohamed** - Machine Learning Engineer
- **Mohamed Gamal** - Embedded Systems
- **Mohamed Hassan** - Embedded Systems
- **Mazen** - Cybersecurity, Backend Dev
- **Naden** - Cybersecurity

---






##  Contact

**Email**: support@empowerwork.com 
**Location**: Alexandria, Egypt

---

