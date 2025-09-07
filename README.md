# Sudoku API v1

## Description

A simple Sudoku API built with FastAPI to count user scores and store them in a PostgreSQL database.

## Tech Stack

- PostgreSQL >= v16.1
- Python == v3.12

# How to run

#### Clone the repository

```
git clone https://github.com/savelychercov/sudoku-backend-py.git
cd sudoku-backend-py
```

#### Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate \ source venv/Scripts/activate \ venv/Scripts/activate.bat
pip install -r requirements.txt

# if psycopg2 not installing run this command:
sudo apt-get update
sudo apt-get install libpq-dev python3-dev
pip install psycopg2
```

#### Create .env file

```
cp .env.example .env
sudo nano .env
```

#### Create the database

```
python create_db.py
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
