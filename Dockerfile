# Gunakan base image resmi Python 3.10
FROM python:3.10-slim

# Install git dan beberapa tools dasar
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Buat direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Buat virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependensi
RUN pip install --upgrade pip && pip install -r requirements.txt

# Salin semua file project ke container
COPY . .

# Expose port untuk Streamlit
EXPOSE 8501

# Jalankan Streamlit
CMD ["streamlit", "run", "dashboard/dashboard.py", "--server.address=0.0.0.0", "--server.port=8501"]
