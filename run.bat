@echo off
echo 백엔드 서버를 시작합니다...
cd backend
start cmd /k "uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --log-level debug"

echo 프론트엔드 서버를 시작합니다...
cd ../frontend
python -m http.server 3000 --bind 0.0.0.0 