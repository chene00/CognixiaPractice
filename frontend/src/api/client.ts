// src/api/client.ts

const BASE_URL = 'http://localhost:8000/api';

// This is a wrapper around the native browser fetch()
export const apiClient = async (endpoint: string, options: RequestInit = {}) => {
  const token = localStorage.getItem('access_token');

  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    ...options.headers,
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
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