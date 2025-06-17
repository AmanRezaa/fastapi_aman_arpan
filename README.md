

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

Here’s the **updated `README.md` attachment content** with the new Docker-related section:

---

### 📦 Docker Support

#### 🐳 Dockerfile

Created a file named `Dockerfile` in project root.

---

#### 📂 .dockerignore

Created a `.dockerignore` file in `backend/` directory to avoid copying unnecessary files:

#### ⚙️ Build and Run

1. **Build Docker image**
   Run this in your terminal:

   ```bash
   docker build -t fastapi-blog-app .
   ```

2. **Run Docker container**

   ```bash
   docker run -p 8000:8000 fastapi-blog-app
   ```

   > If your app needs environment variables like `DATABASE_URL_CLOUD`, use:
   >
   > ```bash
   > docker run --env-file .env -p 8000:8000 fastapi-blog-app
   > ```

---
