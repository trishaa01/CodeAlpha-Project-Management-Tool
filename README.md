# ⚡ TaskFlow — Project Management Tool

A full-stack collaborative project management tool built with Django, similar to Trello and Asana.

## Features

- 🔐 **User Authentication** — Register, login, logout, and profile management
- 📋 **Project Management** — Create projects, invite members, manage roles
- ✅ **Task Boards** — Kanban-style board with To Do, In Progress, and Done columns
- 💬 **Comments** — Comment and communicate within tasks
- 🔔 **Notifications** — In-app notifications for task assignments and comments
- 👥 **Team Collaboration** — Invite members to projects, assign tasks to teammates

## Tech Stack

- **Backend:** Django 4.x, Python 3.x
- **Database:** SQLite (development)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Auth:** Django built-in authentication system

## Project Structure
```
taskflow/

├── accounts/        # User auth and profiles

├── projects/        # Project and membership management

├── tasks/           # Task CRUD and Kanban board

├── comments/        # Task comments

├── notifications/   # In-app notification system

├── core/            # Django project settings

├── templates/       # HTML templates

└── static/          # CSS and JS files
```
## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/trishaa01/project-management-tool.git
cd project-management-tool
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

6. Open your browser at `http://127.0.0.1:8000`

### Dashboard
Clean dark-themed project dashboard showing all your projects.

### Kanban Board
Three-column task board — To Do, In Progress, and Done.

### Notifications
Real-time in-app notifications for task assignments and comments.

## Future Improvements

- WebSocket support for real-time updates
- Drag and drop task cards
- File attachments on tasks
- Due date reminders
- Mobile responsive design improvements
