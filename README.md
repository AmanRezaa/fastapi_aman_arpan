# FastAPI CRUD Application

A basic CRUD API built using FastAPI, demonstrating modular route handling, validation, and clean branching workflow.

# Team Members
- Aman Reza
- Arpan Koley

# Features

- **Create User (POST)** → id, Name and Address
- **Get Users (GET)** → List all users
- **Update User (PATCH)** → Update name for an existing id
- **Delete User (DELETE)** → Remove user by id

# Project Structure
```
fastapi_aman_arpan/
├── main.py
├── models.py
├── routes/
│       ├── create_user.py   # POST endpoint
│       ├── get_user.py     # GET endpoint
│       ├── update_user.py   # PATCH endpoint
│       ├── delete_user.py   # DELETE endpoint
├── requirements.txt
├── README.md
```

# Setup Instructions

# 1.Clone the Repository
git clone <repository-url>
cd fastapi_aman_arpan
# 2.Create Virtual Environment
python3 -m venv venv
source venv/bin/activate   
# 3.Install Dependencies
pip install -r requirements.txt


# Running the App
uvicorn main:app --reload


# API Endpoints
| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| POST   | `/users`         | Create a new user    |
| GET    | `/users`         | List all users       |
| PATCH  | `/users/{phone}` | Update user name     |
| DELETE | `/users/{phone}` | Delete user by phone |

#
