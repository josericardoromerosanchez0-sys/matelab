# Imagen base de Python (Debian 12 slim)
FROM python:3.11-slim

# No generar .pyc y logueo sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# --------- Instalar dependencias de sistema + driver ODBC 17 ---------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    apt-transport-https \
    unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/12/prod.list \
    > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y --no-install-recommends \
    msodbcsql17 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# --------- Instalar dependencias de Python ---------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --------- Copiar código del proyecto ---------
COPY . .

# Variables por defecto dentro del contenedor
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV PORT=8000

# --------- Collectstatic (usa tus settings de STATIC_ROOT) ---------
RUN python manage.py collectstatic --noinput

# --------- Comando de arranque ---------
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]