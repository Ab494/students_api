# Base python image
FROM python:3.12-slim

# environment variables
ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONNUNBUFFERED=1

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# run gunicorn for production
CMD ["gunicorn", "students_api.wsgi:application", "--bind", "0.0.0:8000"]
# collectstatic
RUN python manage.py collectstatic --noinput