@echo off
echo.
echo 🧠 EmoChat — Emotion-Aware AI Chatbot
echo ======================================
echo.

IF NOT EXIST "backend\.env" (
  echo Copying .env.example to .env...
  copy backend\.env.example backend\.env
  echo Please edit backend\.env and add your HF_API_KEY
  echo.
)

echo Starting FastAPI backend on port 8000...
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt -q
start "EmoChat Backend" cmd /k "call venv\Scripts\activate && uvicorn main:app --reload --port 8000"
cd ..

timeout /t 3 /nobreak >nul

echo Starting React frontend on port 3000...
cd frontend
start "EmoChat Frontend" cmd /k "npm install && npm start"
cd ..

echo.
echo Both servers starting...
echo   Frontend: http://localhost:3000
echo   Backend:  http://localhost:8000
echo   API Docs: http://localhost:8000/docs
echo.
pause
