@echo off
echo Quick Docker Deployment
echo =====================
echo.

echo Checking Docker installation...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not installed or not in PATH
    echo Please install Docker Desktop first
    pause
    exit /b 1
)

echo Creating .env file from template...
if not exist .env (
    copy .env.production .env
    echo.
    echo IMPORTANT: Edit .env file with your production settings:
    echo   - OPENROUTER_API_KEY=your_production_key
    echo   - FRONTEND_URL=https://your-domain.com
    echo   - SECRET_KEY=your_32_character_secret
    echo.
    pause
)

echo Building and starting containers...
docker-compose up -d --build

echo.
echo Deployment complete!
echo.
echo Access your application:
echo   Frontend: http://localhost:3000
echo   Backend API: http://localhost:5000
echo.
echo To view logs: docker-compose logs -f
echo To stop: docker-compose down
echo.
pause
