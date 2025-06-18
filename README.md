


# 🚀 FastAPI CRUD Blog Application

A modular and scalable FastAPI CRUD application for blogs and authentication using asynchronous PostgreSQL integration and clean project structure.

---

## 👤 Author

Developed by Arpan Koley and Aman Reza.

---

## 🧱 Project Structure

```
backend/
├── app/
│   ├── auth/                    # Auth utilities (e.g., JWT helpers)
│   ├── controllers/             # Business logic layer
│   ├── database/                # DB config and helpers
│   ├── middleware/             # Custom auth middleware
│   ├── models/                  # Pydantic models & DB schemas
│   ├── routes/                  # API route definitions
│   ├── utils/                   # Utility functions
│   ├── main.py                  # FastAPI app initialization
│   └── temp.py                  # Temporary/testing script
├── scripts/
│   └── dokcer.sh                # Docker helper script
├── .env                         # Environment variables
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

* 🧩 Modular design with clear separation of concerns
* 🔒 Authentication with JWTs (HTTP-only cookies)
* ⚡ Async PostgreSQL with SQLAlchemy + `asyncpg`
* 🔁 Full CRUD operations for blog resources
* 🔐 Middleware to protect routes (`/blogs` only)
* 🧪 Easy to test, extend, and deploy

---

## 📦 Installation

```bash
git clone <your-repo-url>
cd backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## 🛠️ Environment Setup

Create a `.env` file in the root directory with:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/blogdb
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🏃 Run the Application

```bash
uvicorn app.utils.main:app --reload
```

---

## 🔐 Authentication Flow

### ✅ Signup

**Endpoint:** `POST /auth/signup`
**Description:** Create a new user account.
**Body:**

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

---

### 🔓 Login

**Endpoint:** `POST /auth/login`
**Description:** Authenticate user and return JWT as HTTP-only cookie.
**Body:**

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:** Sets `access_token` in a secure cookie.

---

### 🚪 Logout

**Endpoint:** `POST /auth/logout`
**Description:** Clears the auth cookie.

---

## 🔐 Middleware (JWT-Protected Routes)

All `/blogs` routes are protected via custom middleware (`auth_middleware.py`) that checks the JWT from the request cookie. Unauthorized access returns `401 Unauthorized`.

---

## 📌 API Endpoints

### 📝 Blog Routes (Protected)

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/blogs/`     | List all blogs          |
| POST   | `/blogs/`     | Create a new blog       |
| GET    | `/blogs/{id}` | Get blog by ID          |
| PUT    | `/blogs/{id}` | Update an existing blog |
| DELETE | `/blogs/{id}` | Delete a blog by ID     |

---

## 🐳 Docker Support

### 🏗️ Build

```bash
docker build -t fastapi-blog-app .
```

### 🚀 Run

```bash
docker run -p 8000:8000 fastapi-blog-app
```

For environment variables:

```bash
docker run --env-file .env -p 8000:8000 fastapi-blog-app
```
