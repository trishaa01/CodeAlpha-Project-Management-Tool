# ⚡ TaskFlow — Project Management Tool

> A full-stack collaborative project management tool built with Django, similar to Trello and Asana.

---

## 🌐 Live Demo

```
https://project-management-tool-7gh1.onrender.com
```

---

## ✨ Features

- 🔐 **User Authentication** — Register, login, logout, and profile management
- 📋 **Project Management** — Create projects, invite members, manage roles
- ✅ **Task Boards** — Kanban-style board with To Do, In Progress, and Done columns
- 💬 **Comments** — Comment and communicate within tasks
- 🔔 **Notifications** — In-app notifications for task assignments and comments
- 👥 **Team Collaboration** — Invite members to projects, assign tasks to teammates
- ⚡ **Real-time Updates** — Live task and comment updates using WebSockets

---

## 🛠️ Tech Stack

```
Backend     : Django 4.x, Python 3.x
Real-time   : Django Channels + Redis (WebSockets)
Database    : SQLite (development)
Frontend    : HTML5, CSS3, Vanilla JavaScript
Auth        : Django built-in authentication
Deployment  : Render (Daphne ASGI server)
```

---

## 📁 Project Structure

```
CodeAlpha-Project-Management-Tool/
├── accounts/            # User auth and profiles
├── projects/            # Project and membership management
├── tasks/               # Task CRUD and Kanban board
├── comments/            # Task comments
├── notifications/       # In-app notification system
├── core/                # Django project settings and ASGI config
├── templates/           # HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── projects/
│   ├── tasks/
│   ├── comments/
│   └── notifications/
├── static/              # CSS and JS files
│   ├── css/main.css
│   └── js/main.js
├── manage.py
├── requirements.txt
├── build.sh
└── render.yaml
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/trishaa01/CodeAlpha-Project-Management-Tool.git
cd CodeAlpha-Project-Management-Tool
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

### 6. Open in browser
```
http://127.0.0.1:8000
```

---

## 🚀 How to Use

```
1. Register a new account at /accounts/register/
2. Create a new project from the dashboard
3. Invite team members by username
4. Add tasks to the Kanban board
5. Assign tasks to members, set priority and due date
6. Comment on tasks in real-time
7. Get notified when tasks are assigned or commented on
```

---

## ☁️ Deployment

```
Platform      : Render
ASGI Server   : Daphne (for WebSocket support)
Channel Layer : Redis (Render Key Value)
Static Files  : WhiteNoise
```

---

## 👩‍💻 Author

```
Name     : Trisha
GitHub   : https://github.com/trishaa01
```

---