import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { Box } from '@mui/material';

import Navbar from './components/Navbar';
import Home from './pages/Home';
import Events from './pages/Events';
import Campaigns from './pages/Campaigns';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import AdminDashboard from './pages/AdminDashboard';
import EventDetails from './pages/EventDetails';
import CampaignDetails from './pages/CampaignDetails';
import { useAuth } from './contexts/AuthContext';

function App() {
  const { user } = useAuth();

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <Navbar />
      <Box component="main" sx={{ flexGrow: 1 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/events" element={<Events />} />
          <Route path="/events/:id" element={<EventDetails />} />
          <Route path="/campaigns" element={<Campaigns />} />
          <Route path="/campaigns/:id" element={<CampaignDetails />} />
          <Route 
            path="/login" 
            element={user ? <Navigate to="/" /> : <Login />} 
          />
          <Route 
            path="/register" 
            element={user ? <Navigate to="/" /> : <Register />} 
          />
          <Route 
            path="/profile" 
            element={user ? <Profile /> : <Navigate to="/login" />} 
          />
          <Route 
            path="/admin" 
            element={user?.user_type === 'admin' ? <AdminDashboard /> : <Navigate to="/" />} 
          />
        </Routes>
      </Box>
    </Box>
  );
}

export default App;
