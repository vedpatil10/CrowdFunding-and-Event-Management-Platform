
# Crowdfunding & Event Management Platform

A comprehensive web platform for technical fest registrations and payments, built with ReactJS frontend and Django backend.

## 🚀 Features

- **Event Management**: Browse and register for technical fest events
- **Secure Payments**: Integrated Razorpay payment gateway
- **Admin Dashboard**: Committee management with participant tracking
- **Real-time Progress**: Live fund tracking and campaign monitoring
- **Fraud Prevention**: Advanced security measures and validation
- **User Authentication**: JWT-based secure authentication
- **Responsive Design**: Mobile-friendly Material-UI interface

## 🛠️ Tech Stack

- **Frontend**: ReactJS, Material-UI, Axios, React Router
- **Backend**: Django REST Framework, Python
- **Database**: MySQL
- **Payment Gateway**: Razorpay
- **Authentication**: JWT tokens
- **State Management**: React Context API

## 📁 Project Structure

```
Crowndfunding/
├── frontend/              # ReactJS application
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── pages/         # Page components
│   │   ├── contexts/      # React contexts
│   │   ├── services/     # API services
│   │   └── utils/        # Utility functions
│   └── public/           # Static assets
├── backend/              # Django REST API
│   ├── crowdfunding/     # Main Django project
│   ├── events/          # Event management app
│   ├── campaigns/       # Campaign management app
│   ├── payments/        # Payment processing app
│   └── users/           # User management app
├── requirements.txt     # Python dependencies
├── setup.sh            # Linux/Mac setup script
├── setup.bat           # Windows setup script
└── README.md           # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- MySQL 8.0+
- Git

### Installation

#### Option 1: Automated Setup (Recommended)
```bash
# For Linux/Mac
chmod +x setup.sh
./setup.sh

# For Windows
setup.bat
```

#### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Crowndfunding
   ```

2. **Backend Setup**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Linux/Mac:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Setup environment variables
   cp backend/env.example backend/.env
   # Edit backend/.env with your configuration
   
   # Setup database
   cd backend
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

### Configuration

1. **Database Configuration**
   - Create MySQL database: `crowdfunding_db`
   - Update `backend/.env` with database credentials

2. **Razorpay Configuration**
   - Get Razorpay keys from [Razorpay Dashboard](https://dashboard.razorpay.com/)
   - Update `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET` in `backend/.env`

3. **Email Configuration** (Optional)
   - Update email settings in `backend/.env` for notifications

### Running the Application

1. **Start Backend Server**
   ```bash
   cd backend
   python manage.py runserver
   ```
   Backend will be available at `http://localhost:8000`

2. **Start Frontend Server**
   ```bash
   cd frontend
   npm start
   ```
   Frontend will be available at `http://localhost:3000`

## 📚 API Documentation

### Authentication Endpoints
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `GET /api/auth/profile/` - Get user profile

### Event Endpoints
- `GET /api/events/` - List all events
- `POST /api/events/` - Create event (Admin only)
- `GET /api/events/{id}/` - Get event details
- `POST /api/events/registrations/` - Register for event

### Campaign Endpoints
- `GET /api/campaigns/` - List all campaigns
- `POST /api/campaigns/` - Create campaign
- `GET /api/campaigns/{id}/` - Get campaign details
- `POST /api/campaigns/donations/` - Make donation

### Payment Endpoints
- `POST /api/payments/razorpay/create-order/` - Create payment order
- `POST /api/payments/razorpay/verify-payment/` - Verify payment

## 🔐 User Roles

- **Student**: Can browse events, register, and make donations
- **Committee Member**: Can create events and manage registrations
- **Admin**: Full access to admin dashboard and all features

## 🛡️ Security Features

- JWT-based authentication
- Password validation
- CSRF protection
- Payment verification
- Fraud detection algorithms
- Input validation and sanitization

## 🧪 Testing

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

## 📦 Deployment

### Backend Deployment
1. Set `DEBUG=False` in production
2. Configure production database
3. Set up static file serving
4. Configure email settings
5. Set up SSL certificates

### Frontend Deployment
1. Build production bundle: `npm run build`
2. Serve static files through web server
3. Configure API endpoints for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

=======
# CrowndFunding-and-Event-Management-Platform
Crowdfunding &amp; Event Management Platform – Full-stack web app with ReactJS, Django, and MySQL. Students can browse fest events, register, and pay via Razorpay. Includes admin dashboard for event management, real-time tracking, and fraud prevention.
