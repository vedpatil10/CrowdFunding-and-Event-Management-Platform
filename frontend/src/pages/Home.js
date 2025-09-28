import React from 'react';
import {
  Container,
  Typography,
  Grid,
  Card,
  CardContent,
  CardMedia,
  CardActions,
  Button,
  Box,
  Chip,
} from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  const features = [
    {
      title: 'Event Registration',
      description: 'Browse and register for technical fest events with secure payment processing.',
      image: '/api/placeholder/300/200',
      action: () => navigate('/events'),
    },
    {
      title: 'Crowdfunding Campaigns',
      description: 'Support campaigns and contribute to meaningful causes in your community.',
      image: '/api/placeholder/300/200',
      action: () => navigate('/campaigns'),
    },
    {
      title: 'Admin Dashboard',
      description: 'Manage events, campaigns, and participants with comprehensive analytics.',
      image: '/api/placeholder/300/200',
      action: () => navigate('/admin'),
    },
  ];

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box textAlign="center" mb={6}>
        <Typography variant="h2" component="h1" gutterBottom>
          Crowdfunding & Event Management Platform
        </Typography>
        <Typography variant="h5" color="text.secondary" paragraph>
          Empowering technical fests with seamless event registration and crowdfunding capabilities
        </Typography>
      </Box>

      <Grid container spacing={4}>
        {features.map((feature, index) => (
          <Grid item xs={12} md={4} key={index}>
            <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
              <CardMedia
                component="img"
                height="200"
                image={feature.image}
                alt={feature.title}
              />
              <CardContent sx={{ flexGrow: 1 }}>
                <Typography gutterBottom variant="h5" component="h2">
                  {feature.title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {feature.description}
                </Typography>
              </CardContent>
              <CardActions>
                <Button size="small" onClick={feature.action}>
                  Learn More
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Box mt={8} textAlign="center">
        <Typography variant="h4" gutterBottom>
          Key Features
        </Typography>
        <Grid container spacing={2} justifyContent="center">
          <Grid item>
            <Chip label="Secure Payments" color="primary" />
          </Grid>
          <Grid item>
            <Chip label="Real-time Tracking" color="secondary" />
          </Grid>
          <Grid item>
            <Chip label="Fraud Prevention" color="success" />
          </Grid>
          <Grid item>
            <Chip label="Admin Dashboard" color="info" />
          </Grid>
          <Grid item>
            <Chip label="Mobile Responsive" color="warning" />
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default Home;
