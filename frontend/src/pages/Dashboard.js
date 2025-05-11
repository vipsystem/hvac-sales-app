import React from 'react';
import { Container, Grid, Paper, Typography, Box } from '@mui/material';

const Dashboard = () => {
  const stats = [
    { title: 'Total Sales', value: '$15,890', color: '#1976d2' },
    { title: 'Active Quotes', value: '12', color: '#2e7d32' },
    { title: 'Products Sold', value: '45', color: '#ed6c02' },
  ];

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        {stats.map((stat) => (
          <Grid item xs={12} sm={4} key={stat.title}>
            <Paper
              sx={{
                p: 3,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                bgcolor: stat.color,
                color: 'white',
              }}
            >
              <Typography variant="h6" gutterBottom>
                {stat.title}
              </Typography>
              <Typography variant="h4">{stat.value}</Typography>
            </Paper>
          </Grid>
        ))}
      </Grid>
      
      <Box sx={{ mt: 4 }}>
        <Paper sx={{ p: 3 }}>
          <Typography variant="h5" gutterBottom>
            Recent Activity
          </Typography>
          <Typography variant="body1" color="text.secondary">
            No recent activity to display.
          </Typography>
        </Paper>
      </Box>
    </Container>
  );
};

export default Dashboard;
