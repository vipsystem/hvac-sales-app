export const getErrorMessage = (error) => {
  if (error.response) {
    // Server responded with error
    const data = error.response.data;
    if (typeof data === 'string') {
      return data;
    }
    if (data.detail) {
      return data.detail;
    }
    if (data.message) {
      return data.message;
    }
    if (typeof data === 'object') {
      const firstError = Object.values(data)[0];
      if (Array.isArray(firstError)) {
        return firstError[0];
      }
      return firstError;
    }
    return 'An error occurred';
  }
  
  if (error.request) {
    // Request made but no response
    return 'No response from server. Please check your internet connection.';
  }
  
  // Something else went wrong
  return error.message || 'An unexpected error occurred';
};
