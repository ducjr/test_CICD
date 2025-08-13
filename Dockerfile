# syntax=docker/dockerfile:1
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DJANGO_SETTINGS_MODULE=cicd_demo.settings \
    DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY:-change-me}
RUN python manage.py collectstatic --noinput || true
EXPOSE 8000
CMD ["gunicorn", "cicd_demo.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
