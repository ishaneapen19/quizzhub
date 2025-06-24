# 🎓  Quiz Hub

 Quiz Hub is a full-stack quiz web application designed for students at Galtech School of Technology. It enables students to take quizzes based on categories like General Aptitude, Programming, and Logic, while administrators can manage questions and track student performance.

---

## 🚀 Features

- 🔐 Role-Based Login (Admin & Student) using JWT Authentication
- 📚 Multiple Quiz Categories
- ❓ Admin MCQ Management with Explanations
- 🧠 Quiz Attempt Functionality with Scoring
- 📊 Student Performance Tracking by Admin
- ⚙️ Backend: Django REST Framework
- 💻 Frontend: React.js with Axios
- 🎨 Fully Custom Styled with CSS

---

## 🛠 Tech Stack

| Layer     | Technology            |
|-----------|------------------------|
| Frontend  | React.js, Axios        |
| Backend   | Django REST Framework  |
| Auth      | JWT (JSON Web Token)   |
| Database  | SQLite (default)       |

---

## 🏃 Getting Started

### ✅ Backend Setup (Django)

```bash
cd quizhub_backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
