

# 🚀 FastAPI CRUD Blog Application

A modular and scalable FastAPI CRUD application for blogs, using asynchronous PostgreSQL integration and clean project structure.

---

## 🧱 Project Structure

```
backend/
├── app/
│   ├── controllers/       # Business logic layer (e.g., blog logic)
│   ├── models/            # Pydantic models and database schemas
│   ├── routes/            # API route definitions (e.g., /blogs)
│   └── utils/             # Utility scripts and DB setup
│       ├── db.py          # Database session & connection
│       ├── main.py        # FastAPI app initialization
│       └── temp.py        # Temporary/testing script
├── venv/                  # Python virtual environment
├── .env                   # Environment variables (e.g., DB credentials)
├── .gitignore             # Git ignored files
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Features

* 🧩 Modular design for clear code separation
* ⚡ Async PostgreSQL with SQLAlchemy + `asyncpg`
* 🔁 Full CRUD operations on `/blogs` route
* 🛠️ Environment-based configuration with `.env`
* 🧪 Easy to test, extend, and deploy

---

## 📦 Installation

```bash
# Clone the project
git clone <your-repo-url>
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🛠️ Environment Setup

Create a `.env` file in the root directory with:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/blogdb
```

---

## 🏃 Run the Application

```bash
uvicorn app.utils.main:app --reload
```

---

## 📌 API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/blogs/`     | List all blogs          |
| POST   | `/blogs/`     | Create a new blog       |
| GET    | `/blogs/{id}` | Get blog by ID          |
| PUT    | `/blogs/{id}` | Update an existing blog |
| DELETE | `/blogs/{id}` | Delete a blog by ID     |


---


## 👤 Author

Developed by Arpan Koley and Aman Reza.
