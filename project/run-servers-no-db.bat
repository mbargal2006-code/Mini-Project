@echo off
echo Starting Backend...
cmd /k "cd /d C:/Users/ADMIN/Downloads/project/project/backend && venv311\Scripts\activate.bat && python main.py"
echo Starting Frontend...
start powershell -NoExit -ExecutionPolicy Bypass -Command "cd 'C:/Users/ADMIN/Downloads/project/frontend'; npm start"
echo Servers starting - Backend: http://localhost:5000 Frontend: http://localhost:3000
pause
