# 📱 Phonestore – Django Web Application

A Django-based web application for managing a phone store, including product listings and customer contact management. This project demonstrates clean Django architecture, database modeling, migrations, and basic CRUD functionality.

---

## 🚀 Project Overview
**Phonestore** is a practical Django project built to simulate a real-world phone retail platform. It focuses on backend fundamentals such as models, migrations, admin customization, and environment setup, making it ideal for showcasing Django proficiency.

---

## 🧩 Key Features
- 📦 Product / phone listing system
- 📩 Customer contact form (stored in database)
- 🗂 Django Admin dashboard
- 🛠 Clean app-based project structure
- 🧪 Database migrations handled correctly
- 🔐 Environment-isolated setup using virtualenv

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default)
- **Environment:** Python venv
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
```
Phonestore/
│
├── phonestore/          # Main app
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── Phonestore/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/phonestore.git
cd phonestore
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv phone_env
phone_env\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py migrate
```

### 5️⃣ Create admin user (optional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 🧠 What Recruiters Will Notice
- Proper use of virtual environments
- Correct migration workflow
- Clean Django app separation
- Readable, well-documented code
- Git-ready project structure

---

## 🌱 Possible Improvements
- REST API with Django REST Framework
- Authentication system
- Product categories & search
- Image upload for phones
- Deployment (Render / Railway / DigitalOcean)

---

## 📸 Screenshots
> _Screenshots help recruiters quickly understand your project visually._

### 🔹 Homepage
_Add a screenshot showing the main page or product listing._

```
/screenshots/homepage.png
```

### 🔹 Contact Page / Form
_Show the contact form or user interaction page._

```
/screenshots/contact.png
```

### 🔹 Admin Dashboard
_Demonstrate Django Admin with your models registered._

```
/screenshots/admin.png
```

**How to add screenshots:**
1. Create a folder named `screenshots` in your project root
2. Take screenshots while the server is running
3. Save them with clear names (e.g. `homepage.png`)
4. GitHub will automatically render them in this section

---

## 👨‍💻 Author
**Emeka Dennis**  
Backend Developer (Django) & Graphics Designer

---

## 📜 License
This project is for learning and portfolio demonstration purposes.

