# Task API - Flask REST API with SQLite

A simple **REST API** built with **Flask** and **SQLite**, demonstrating **CRUD operations** and clean project structure.

---

## 🗂 Project Structure

task_api/
│
├── app/
│ ├── init.py # App factory
│ ├── routes.py # API endpoints
│ ├── models.py # Database CRUD operations
│ └── database.py # SQLite connection
│
├── main.py # App entry point
├── requirements.txt
├── README.md
└── .gitignore

➕ Create a task
<!-- # i create new task with this code below(Create more tasks via POST):
Invoke-RestMethod `
-Uri http://127.0.0.1:5000/tasks `
-Method POST `
-ContentType "application/json" `
-Body '{"title":"My third API task"}'
 -->
📖 Read tasks
<!-- 
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks -Method GET
 -->
✏️ Update a task
<!-- 2️⃣ Update tasks via PUT:
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1 -Method PUT -ContentType "application/json" -Body '{"completed":1}'

 -->
❌ Delete a task
<!-- Delete tasks via DELETE:
Invoke-RestMethod -Uri http://127.0.0.1:5000/tasks/1 -Method DELETE

 -->

 
---

## ⚡ Features

- Create, Read, Update, Delete tasks
- SQLite database (`tasks.db`)
- Modular and scalable structure
- JSON request/response
- Proper HTTP status codes

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/task_api.git
cd task_api
