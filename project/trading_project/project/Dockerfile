# Dockerfile

# 1. 기본 이미지 설정
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. 의존성 설치
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 5. 소스코드 복사
COPY . /app/

# 6. 환경 변수 파일 복사
COPY .env.prod /app/.env.prod

# 7. 환경 변수 로드 및 static 파일 수집
RUN export $(cat .env.prod | xargs) && \
    python manage.py collectstatic --noinput

# 8. 기본 실행 명령어 (gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
