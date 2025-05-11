import React from 'react';
import { Container, Grid, Card, CardContent, CardMedia, Typography, Button, Box } from '@mui/material';

const Products = () => {
  const products = [
    {
      id: 1,
      name: 'Central AC Unit',
      description: 'High-efficiency central air conditioning system',
      price: '$2,499',
      image: 'https://via.placeholder.com/300x200',
    },
    {
      id: 2,
      name: 'Heat Pump',
      description: 'Dual-function heating and cooling system',
      price: '$3,299',
      image: 'https://via.placeholder.com/300x200',
    },
    {
      id: 3,
      name: 'Smart Thermostat',
      description: 'WiFi-enabled programmable thermostat',
      price: '$199',
      image: 'https://via.placeholder.com/300x200',
    },
  ];

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Our Products
      </Typography>
      <Grid container spacing={4}>
        {products.map((product) => (
          <Grid item key={product.id} xs={12} sm={6} md={4}>
            <Card>
              <CardMedia
                component="img"
                height="200"
                image={product.image}
                alt={product.name}
              />
              <CardContent>
                <Typography gutterBottom variant="h5" component="h2">
                  {product.name}
                </Typography>
                <Typography variant="body2" color="textSecondary" component="p">
                  {product.description}
                </Typography>
                <Box sx={{ mt: 2, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <Typography variant="h6" component="p">
                    {product.price}
                  </Typography>
                  <Button variant="contained" color="primary">
                    Add to Cart
                  </Button>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default Products;
