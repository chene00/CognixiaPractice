// src/pages/Login.tsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { authApi } from '../api/authApi';

interface LoginProps {
  onLoginSuccess: () => void;
}

export default function Login({ onLoginSuccess }: LoginProps) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    try {
      const data = await authApi.login(email, password);
      localStorage.setItem('access_token', data.access_token);
      
      // Notify App.tsx that the token has changed so it updates dynamically
      onLoginSuccess();
      
      // Now navigate will work perfectly!
      navigate('/');
    } catch (err: any) {
      setError(err.message || "Failed to log in.");
    }
  };
  
  return (
    <div style={{ maxWidth: '300px', margin: '0 auto', textAlign: 'left' }}>
      <h2>Login</h2>
      {error && <p style={{ color: '#ff4d4d' }}>{error}</p>}
      
      <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <div>
          <label>Email (Username):</label>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
            required 
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div>
          <label>Password:</label>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <button type="submit" style={{ padding: '0.75rem' }}>Login</button>
      </form>
    </div>
  );
}