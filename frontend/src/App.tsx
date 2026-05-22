// src/App.tsx
import { useState } from 'react';
import { Routes, Route, Link, Navigate } from 'react-router-dom';
import CreateCustomer from './pages/CreateCustomer';
import CreateAccount from './pages/CreateAccount';
import Dashboard from './pages/Dashboard'; 
import Login from './pages/Login';
import { authApi } from './api/authApi';

function App() {
  // Manage token state dynamically
  const [token, setToken] = useState<string | null>(localStorage.getItem('access_token'));

  const handleLogout = () => {
    authApi.logout(); // Wipes localStorage
    setToken(null);   // Updates state to instantly re-route
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto', textAlign: 'left' }}>
      
      <nav style={{ marginBottom: '2rem', display: 'flex', gap: '1rem', borderBottom: '1px solid #ccc', paddingBottom: '1rem', alignItems: 'center' }}>
        {token ? (
          <>
            <Link to="/">My Dashboard</Link>
            <Link to="/create-account">Open Account</Link>
            <div style={{ marginLeft: 'auto' }}>
              <button onClick={handleLogout} style={{ background: 'transparent', border: '1px solid var(--accent)', color: 'var(--accent)', cursor: 'pointer', padding: '0.5rem 1rem', borderRadius: '4px' }}>
                Logout
              </button>
            </div>
          </>
        ) : (
          <>
             <Link to="/login" style={{ color: 'var(--accent)', fontWeight: 'bold' }}>Login</Link>
             <Link to="/register">Register</Link>
          </>
        )}
      </nav>

      <Routes>
        <Route path="/login" element={<Login onLoginSuccess={() => setToken(localStorage.getItem('access_token'))} />} />
        <Route path="/register" element={<CreateCustomer />} />
        
        <Route path="/" element={token ? <Dashboard /> : <Navigate to="/login" />} />
        <Route path="/create-account" element={token ? <CreateAccount /> : <Navigate to="/login" />} />
      </Routes>
    </div>
  );
}

export default App;