import React from 'react';
import { Container, Typography, Box, Button } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

const Home = () => {
  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 8, textAlign: 'center' }}>
        <Typography variant="h2" component="h1" gutterBottom>
          Welcome to HVAC Sales
        </Typography>
        <Typography variant="h5" component="h2" gutterBottom color="textSecondary">
          Your one-stop shop for all HVAC equipment and services
        </Typography>
        <Box sx={{ mt: 4 }}>
          <Button
            variant="contained"
            color="primary"
            size="large"
            component={RouterLink}
            to="/products"
            sx={{ mr: 2 }}
          >
            View Products
          </Button>
          <Button
            variant="outlined"
            color="primary"
            size="large"
            component={RouterLink}
            to="/register"
          >
            Get Started
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default Home;
