// src/pages/CreateCustomer.tsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { customerApi } from '../api/customerApi';

export default function CreateCustomer() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState(''); // 1. Add password state
  const [error, setError] = useState<string | null>(null);
  
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    try {
      // 2. Pass the password to your API call
      await customerApi.create({ name, email, password });
      navigate('/login'); // Redirect to login page after successful registration
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h2>Create New Customer Account</h2>
      {error && <p style={{ color: '#ff4d4d' }}>{error}</p>}
      
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem', maxWidth: '300px' }}>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Name: </label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} required style={{ width: '100%', padding: '0.5rem' }} />
        </div>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Email: </label>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required style={{ width: '100%', padding: '0.5rem' }} />
        </div>
        {/* 3. Add Password Input Field */}
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Password: </label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required style={{ width: '100%', padding: '0.5rem' }} />
        </div>
        <button type="submit" style={{ padding: '0.75rem', cursor: 'pointer', marginTop: '0.5rem' }}>Register</button>
      </form>
    </div>
  );
}