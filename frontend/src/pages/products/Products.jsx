import { useState, useEffect, useContext } from 'react';
import { 
  Box, Typography, Grid, Card, CardMedia, CardContent, 
  CardActions, Button, CircularProgress, Alert 
} from '@mui/material';
import api from '../../API/client';
import AuthContext from '../../authentication/AuthContext';

export default function Products() {
  const { user } = useContext(AuthContext);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Check if user is restricted
  const isEmployee = user?.role === 'Employee';

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await api.get('products/');
        setProducts(response.data);
      } catch (err) {
        setError('Failed to load products.');
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, []);

  if (loading) return <Box sx={{ display: 'flex', justifyContent: 'center', mt: 5 }}><CircularProgress /></Box>;
  if (error) return <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>;

  return (
    <Box sx={{ p: 4 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 4 }}>
        <Typography variant="h4" component="h1" fontWeight="bold">
          Products
        </Typography>
        
        {/* We keep the button visible but disable it if they are an Employee */}
        <Button 
          variant="contained" 
          color="primary" 
          disabled={isEmployee}
          title={isEmployee ? "Only Managers can add products" : ""}
          onClick={() => { /* TODO: Open Add Product Modal */ }}
        >
          + Add Product
        </Button>
      </Box>

      {products.length === 0 ? (
        <Typography variant="body1" color="text.secondary">No products found. Add one to get started!</Typography>
      ) : (
        <Grid container spacing={3}>
          {products.map((product) => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={product.id}>
              <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                <CardMedia
                  component="img"
                  height="200"
                  // Use a placeholder if no image exists yet
                  image={product.image || 'https://placehold.co/400x300?text=No+Image'} 
                  alt={product.name}
                  sx={{ objectFit: 'cover' }}
                />
                <CardContent sx={{ flexGrow: 1 }}>
                  <Typography gutterBottom variant="h6" component="h2" fontWeight="bold">
                    {product.name}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Stock: {product.stock_quantity}
                  </Typography>
                  <Typography variant="h6" color="primary" sx={{ mt: 1 }}>
                    ${product.selling_price}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" disabled={isEmployee}>Edit</Button>
                  <Button size="small" color="error" disabled={isEmployee}>Delete</Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
    </Box>
  );
}
