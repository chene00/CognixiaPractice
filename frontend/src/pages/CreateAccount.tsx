// src/pages/CreateAccount.tsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AccountType } from '../types';
import { accountApi } from '../api/accountApi';
import { getUserIdFromToken } from '../api/authApi'; 

export default function CreateAccount() {
  // Removed customerId state entirely
  const [type, setType] = useState<AccountType>(AccountType.CHECKING);
  const [balance, setBalance] = useState<number | ''>(''); 
  const [error, setError] = useState<string | null>(null);
  
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    // Grab the ID from the token behind the scenes
    const userId = getUserIdFromToken();
    if (!userId) {
      setError("You must be logged in to do this.");
      return;
    }

    try {
      await accountApi.create(userId, { 
        type, 
        balance: Number(balance) 
      });

      // Navigate back to the home dashboard
      navigate('/');
      
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h2>Open New Bank Account</h2>
      {error && <p style={{ color: '#ff4d4d', marginBottom: '1rem' }}>{error}</p>}
      
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem', maxWidth: '300px' }}>
        
        {/* Customer ID input removed completely */}

        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Account Type: </label>
          <select 
            value={type} 
            onChange={(e) => setType(e.target.value as AccountType)} 
            style={{ width: '100%', padding: '0.5rem' }}
          >
            <option value={AccountType.CHECKING}>Checking</option>
            <option value={AccountType.SAVINGS}>Savings</option>
          </select>
        </div>

        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Initial Deposit ($): </label>
          <input 
            type="number" 
            step="0.01"
            value={balance} 
            onChange={(e) => setBalance(e.target.value === '' ? '' : Number(e.target.value))} 
            required 
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>

        <button type="submit" style={{ padding: '0.75rem 1rem', cursor: 'pointer', marginTop: '0.5rem' }}>
          Create Account
        </button>
      </form>
    </div>
  );
}