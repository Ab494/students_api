# 📚 Students API

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-success?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST-Framework-red?logo=django)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/GitHub-Actions-blue?logo=githubactions)](https://github.com/features/actions)
[![Sentry](https://img.shields.io/badge/Sentry-Integrated-critical?logo=sentry)](https://sentry.io)

> A Django RESTful API for managing student data — built for scalability, role-based access, and production readiness. Developed for the PLP Hackathon.

---

## 🚀 Features

- 🔐 User authentication and role-based access (Admin, Teacher, Student)
- 📋 Student registration and profile management
- ✅ Attendance tracking and grade submission
- 📊 API Documentation using Swagger
- 🐳 Dockerized for easy deployment
- ⚙️ CI/CD via GitHub Actions
- 🛡️ Sentry integration for error tracking

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Framework:** Django, Django REST Framework
- **Database:** PostgreSQL
- **CI/CD:** GitHub Actions
- **Error Monitoring:** Sentry
- **Containerization:** Docker
- **Hosting Ready For:** Render / Railway / Heroku

---

## 📂 Project Structure

```
students_api/
│
├── core/                   # Main app for student operations
├── users/                  # Authentication and roles
├── templates/              # Swagger UI templates
├── Dockerfile              # Docker config
├── docker-compose.yml
├── manage.py
└── requirements.txt
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ab494/students_api.git
cd students_api
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root and add:

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=your_postgresql_database_url
SENTRY_DSN=your_sentry_dsn
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 🔄 API Documentation

Once the server is running, access:

```
http://127.0.0.1:8000/swagger/
```

Interactive Swagger UI lets you explore all endpoints.

---

## 🐳 Docker Setup

Build and run the project using Docker:

```bash
docker-compose up --build
```

To run migrations and create a superuser inside the container:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

---

## ✅ Continuous Integration (CI)

CI is configured using **GitHub Actions**:

- Linting
- Testing
- Build checks
- Docker image validation

CI config is in `.github/workflows/ci.yml`.

---

## 🛡️ Sentry Integration

Sentry is integrated for real-time error tracking.

To enable it:

1. Sign up at [https://sentry.io](https://sentry.io)
2. Get your DSN key
3. Add it to your `.env`:

```env
SENTRY_DSN=https://your_dsn_key@o123456.ingest.sentry.io/project_id
```

---

## 🌐 Deployment

You can deploy to Render, Railway, or Heroku. Ensure `DATABASE_URL`, `ALLOWED_HOSTS`, and `SENTRY_DSN` are set correctly.

Docker is supported for smoother deployment pipelines.

---

## 🙌 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Sentry](https://sentry.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Swagger/OpenAPI](https://swagger.io/tools/swagger-ui/)
- [PLP Hackathon Community](https://powerlearnproject.org)

---

## 👨‍💻 Author

**Evans Cheruiyot**  
Backend Developer | Django Specialist  
📫 [GitHub](https://github.com/Ab494)

---

## 📄 License

MIT License © 2025 Evans Cheruiyot

