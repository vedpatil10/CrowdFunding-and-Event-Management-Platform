@echo off
REM Crowdfunding Platform Setup Script for Windows

echo 🚀 Setting up Crowdfunding ^& Event Management Platform...

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install Python dependencies
echo 📥 Installing Python dependencies...
pip install -r requirements.txt

REM Setup environment variables
echo ⚙️ Setting up environment variables...
if not exist backend\.env (
    copy backend\env.example backend\.env
    echo 📝 Please update backend\.env with your configuration
)

REM Setup MySQL database
echo 🗄️ Setting up MySQL database...
echo Please ensure MySQL is running and create a database named 'crowdfunding_db'

REM Run Django migrations
echo 🔄 Running Django migrations...
cd backend
python manage.py makemigrations
python manage.py migrate

REM Create superuser
echo 👤 Creating superuser...
python manage.py createsuperuser

REM Collect static files
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

cd ..

REM Setup React frontend
echo ⚛️ Setting up React frontend...
cd frontend
npm install

echo ✅ Setup complete!
echo.
echo To start the development servers:
echo Backend: cd backend ^&^& python manage.py runserver
echo Frontend: cd frontend ^&^& npm start
echo.
echo Don't forget to:
echo 1. Update backend\.env with your database and Razorpay credentials
echo 2. Create a MySQL database named 'crowdfunding_db'
echo 3. Configure Razorpay keys for payment processing

pause
