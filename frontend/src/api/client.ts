// src/api/client.ts

const BASE_URL = "https://6ylmqvqxt5.execute-api.us-east-1.amazonaws.com/api" || 'http://localhost:8000/api';

// This is a wrapper around the native browser fetch()
export const apiClient = async (endpoint: string, options: RequestInit = {}) => {
  const token = localStorage.getItem('access_token');

  // FIX: Use the native Headers object for safe, dynamic manipulation
  const headers = new Headers(options.headers);
  
  // Provide a default Content-Type if one wasn't passed in options
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  // Safely set the authorization header
  if (token) {
    headers.set('Authorization', `Bearer ${token}`);
  }

  const response = await fetch(`${BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (!response.ok){
    if (response.status === 401) {
      localStorage.removeItem('access_token');
      window.location.href = '/login'; // Force them to the login page
    }
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || `Server error: ${response.status}`);
  }
  return response.json();
};