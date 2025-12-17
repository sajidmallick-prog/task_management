# 📝 Task Management System API

This is a robust backend system for a Task Management application built using **Django**, **Django REST Framework**, and **SQLite**. The project features secure authentication and **Role-Based Access Control (RBAC)** to ensure that data is only accessible to authorized users.

## 📦 Features

* **User Authentication**: Secure registration and login using **JWT (JSON Web Tokens)**.
* **Role-Based Access Control (RBAC)**:
    * **Admins**: Can view, edit, and delete tasks belonging to *any* user.
    * **Users**: Can only manage (CRUD) their own tasks.
* **Automatic Role Setup**: Roles (Admin/User groups) are created automatically when migrations are run.
* **CRUD APIs**: Full management for Tasks (Title, Description, Status).
* **Filtering**: Support for filtering tasks (using django-filter).

## 🛠️ Tech Stack

* **Python 3.x**
* **Django 4.x / 5.x**
* **Django REST Framework**
* **SimpleJWT** (Authentication)
* **SQLite** (Development Database)

---

## 🚀 How to Run This Project

### 1. Create a Virtual Environment
python -m venv venv
# For Windows
venv\Scripts\activate
# For Linux/macOS
source venv/bin/activate

📮 API Endpoints
🔐 Authentication
Endpoint,Method,Description,Data Required (JSON)
/api/auth/register/,POST,Create a new account,"username, password"
/api/auth/login/,POST,Get Access & Refresh tokens,"username, password"

📝 Task Management
All task endpoints require a Bearer Token in the Authorization header.
Endpoint,Method,Description,Functionality
/api/tasks/,GET,List Tasks,Admins see all; Users see their own.
/api/tasks/,POST,Create Task,"{""title"": ""..."", ""description"": ""..."", ""status"": false}"
/api/tasks/<id>/,GET,View Task,Retrieve details of a specific task.
/api/tasks/<id>/,PUT,Update Task,Full update of task details.
/api/tasks/<id>/,PATCH,Partial Update,"Update specific fields (e.g., just the status)."
/api/tasks/<id>/,DELETE,Remove Task,Permanently delete a task.

🧪 Testing with Postman (Importing the Collection)
I have included a Postman collection file named Task_management.postman_collection.json in the root of this repository.

1. Import: Open Postman, click Import, and select the .json file.

2. Environment:

The registration request is set to GET (update to POST for actual use).

The Login request is pre-configured for the user sumanakhatun.

3. Tokens:

After logging in, copy the access token.

In the Task requests, go to the Auth tab, select Bearer Token, and paste the value.

📧 Contact
If you want to suggest improvements or have any issues, feel free to reach out to me 😄

📩 Email:sajidmallick204@gmail.com

💼 LinkedIn: www.linkedin.com/in/sajid-mallick-444215248
📱 Phone: +91-9749371880
