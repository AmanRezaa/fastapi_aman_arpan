


## Project Structure
```
backend/
├── app/
│   ├── auth/                    # Auth utilities (e.g., JWT helpers)
│   ├── controllers/             # actual crud operation services
│   ├── database/                # DB config and helpers
│   ├── middleware/              # Custom auth middleware
│   ├── models/                  # Pydantic models & DB schemas
│   ├── routes/                  # API route definitions
│   ├── utils/                   # Utility functions
│   ├── main.py                  # FastAPI app initialization
│               
├── scripts/
│   └── docker.sh                # Docker helper script
├── run.py                       # uvicorn start server script
├── .env                         # Environment variables
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── README.md
```

##  Installation

```bash
git clone <your-repo-url>
cd backend

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the root directory with:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/blogdb
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
---

## Run the Application

```bash
uvicorn app.main:app --reload
```

##  Docker 

###  Build

```bash
docker build -t fastapi-blog-app:latest .
```

###  Run

```bash
docker run --env-file .env -p 8000:8000 fastapi-blog-app:latest
```

##  References
1. FastApi Tutorial and Features: [link](https://fastapi.tiangolo.com/)
2. Docker Tutorial : [link](https://www.geeksforgeeks.org/devops/docker-tutorial/)
3. SQLAlchemy Documentation : [link](https://docs.sqlalchemy.org/en/20/)
4. How to Add JWT Authentication in FastAPI – A Practical Guide : [link](https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/)
5. Connect an SQLAlchemy application to Neon : [link](https://neon.com/docs/guides/sqlalchemy)
