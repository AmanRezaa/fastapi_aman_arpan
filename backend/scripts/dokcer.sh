#build 
docker build -t fastapi-blog-app:1.0.0 -t fastapi-blog-app:latest .

# run 
docker run -p 8000:8000 --env-file .env  fastapi-blog-app:1.0.0