const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://hvac-sales-app.herokuapp.com';

export const API_ENDPOINTS = {
  login: `${API_BASE_URL}/api/auth/login/`,
  register: `${API_BASE_URL}/api/auth/register/`,
  products: `${API_BASE_URL}/api/products/`,
  quotes: `${API_BASE_URL}/api/quotes/`,
  profile: `${API_BASE_URL}/api/users/profile/`,
};

export const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return {
    'Content-Type': 'application/json',
    'Authorization': token ? `Token ${token}` : '',
  };
};
