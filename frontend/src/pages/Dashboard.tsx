// src/pages/Dashboard.tsx
import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { customerApi } from '../api/customerApi';
import { accountApi } from '../api/accountApi';
import { getUserIdFromToken } from '../api/authApi';
import type { Customer, Account } from '../types'; 

export default function Dashboard() {
  const [customer, setCustomer] = useState<Customer | null>(null);
  const [accounts, setAccounts] = useState<Account[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    // 1. Get the ID from the local session securely
    const userId = getUserIdFromToken();
    
    if (!userId) {
      navigate('/login');
      return;
    }

    const fetchDashboardData = async () => {
      try {
        const [customerData, accountsData] = await Promise.all([
          customerApi.getById(userId),
          accountApi.getByCustomerId(userId)
        ]);

        setCustomer(customerData);
        setAccounts(accountsData);
      } catch (err: any) {
        setError(err.message || "Failed to load dashboard.");
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, [navigate]);

  if (loading) return <p>Loading dashboard...</p>;
  if (error) return <p style={{ color: '#ff4d4d' }}>{error}</p>;
  if (!customer) return <p>Customer not found.</p>;

  return (
    <div>
      <h2>Welcome back, {customer.name}</h2>
      <p style={{ color: 'var(--text)', marginBottom: '2rem' }}>Contact: {customer.email}</p>

      <h3>Your Bank Accounts</h3>
      {accounts.length === 0 ? (
        <p>You have no open accounts. <Link to="/create-account">Open one now</Link>.</p>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginTop: '1rem' }}>
          {accounts.map((account) => (
            <div key={account.id} style={{ border: '1px solid var(--border)', padding: '1rem', borderRadius: '8px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ textTransform: 'capitalize', fontWeight: 'bold' }}>
                  {account.type} Account
                </span>
                <span style={{ fontSize: '1.25rem', color: 'var(--accent)' }}>
                  ${account.balance.toLocaleString('en-US', { minimumFractionDigits: 2 })}
                </span>
              </div>
              <small style={{ color: 'var(--text)', display: 'block', marginTop: '0.5rem' }}>
                Account ID: {account.id}
              </small>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}