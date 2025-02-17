# Django REST Framework Blog API

🚀 A fully functional REST API for a blog application built using Django REST Framework.

## 📌 Features
- User authentication with **dj-rest-auth** & **Token Authentication**
- CRUD operations for blog posts
- User registration and login
- API documentation using **drf-spectacular**

## 🛠 Technologies Used
- **Django** & **Django REST Framework**
- **dj-rest-auth** for authentication
- **drf-spectacular** for API documentation
- **PostgreSQL / SQLite** (depending on your configuration)

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/shreif-abdullah/django-rest-blog-api.git
cd django-rest-blog-api
```

### 2️⃣ Setup Virtual Environment
```bash
pipenv install --dev
pipenv shell
```

### 3️⃣ Configure Environment Variables
Create a `.env` file and add your database credentials and secret key:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Change for PostgreSQL
```

### 4️⃣ Apply Migrations & Run Server
```bash
python manage.py migrate
python manage.py createsuperuser  # Optional: Create admin user
python manage.py runserver
```

### 5️⃣ API Documentation
Access the API documentation at:
- **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
- **Redoc:** `http://127.0.0.1:8000/api/redoc/`

## 🛠 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/v1/posts/` | List all blog posts |
| POST | `/api/v1/posts/` | Create a new post |
| GET | `/api/v1/posts/{id}/` | Retrieve a single post |
| PUT | `/api/v1/posts/{id}/` | Update a post |
| DELETE | `/api/v1/posts/{id}/` | Delete a post |
| POST | `/api/v1/dj-rest-auth/login/` | User login |
| POST | `/api/v1/dj-rest-auth/logout/` | User logout |
| POST | `/api/v1/dj-rest-auth/registration/` | User registration |

## 🌟 Contributing
Pull requests are welcome! Feel free to fork the repo and submit a PR.

## 📜 License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it with proper attribution.

---
🔥 Happy Coding! 🚀

