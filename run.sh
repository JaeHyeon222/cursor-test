#!/bin/bash
# pip install -r backend/requirements.txt

# 백엔드 실행
echo "백엔드 서버를 시작합니다..."
cd backend
uvicorn app.main:app --reload &

# 프론트엔드 실행
echo "프론트엔드 서버를 시작합니다..."
cd ../frontend
python -m http.server 3000 