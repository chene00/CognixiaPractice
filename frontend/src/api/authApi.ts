// src/api/authApi.ts
import { apiClient } from './client';

export const authApi = {
  login: async (email: string, password: string) => {
    // We MUST use URLSearchParams to format the data correctly for FastAPI's OAuth2 form
    const formData = new URLSearchParams();
    formData.append('username', email); // FastAPI OAuth2 expects 'username'
    formData.append('password', password);

    // Notice we override the Content-Type to application/x-www-form-urlencoded
    const response = await apiClient('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: formData.toString(),
    });

    return response as { access_token: string; token_type: string };
  },

  logout: () => {
    localStorage.removeItem('access_token');
    window.location.href = '/login';
  }
};

export const getUserIdFromToken = (): string | null => {
  const token = localStorage.getItem('access_token');
  if (!token) return null;
  
  try {
    // A JWT is split into 3 parts by periods. The payload is the middle part.
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    
    // Return the 'sub' (subject) which we set as the user's ID on the backend
    return JSON.parse(jsonPayload).sub;
  } catch (e) {
    return null;
  }
};