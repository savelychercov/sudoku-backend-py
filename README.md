# How to run

#### Clone the repository

```
git clone https://github.com/savelychercov/sudokapi.git
cd sudokapi
```

#### Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Create .env file

```
cp .env.example .env
sudo nano .env
```

#### Update the database

```
alembic upgrade head
```

#### Run the application

```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

or

pm2 start "venv/Scripts/python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000" --name fastapi-app
```

---

# Add new migrations

```
alembic revision --autogenerate -m "message"
alembic upgrade head
```

---

# Update project in production

```
cd sudokapi
git pull
source venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
pm2 restart fastapi-app
```
