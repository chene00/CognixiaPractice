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
    const userId = getUserIdFromToken();
    if (!userId) {
      navigate('/login');
      return;
    }

    const fetchDashboardData = async () => {
      try {
        const [customerData, accountsData] = await Promise.all([
          customerApi.getById(userId),
          accountApi.getByCustomerId(userId),
        ]);
        setCustomer(customerData);
        setAccounts(accountsData);
      } catch (err: any) {
        setError(err.message || 'Failed to load dashboard.');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, [navigate]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-slate-400 text-sm">Loading your dashboard...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-4 bg-red-50 border border-red-200 text-red-700 rounded-xl text-sm">
        {error}
      </div>
    );
  }

  if (!customer) return null;

  const totalBalance = accounts.reduce((sum, acct) => sum + acct.balance, 0);
  const firstName = customer.name.split(' ')[0];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-slate-900">Hello, {firstName}</h1>
          <p className="text-slate-500 text-sm mt-0.5">{customer.email}</p>
        </div>
        <Link
          to="/create-account"
          className="bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold px-4 py-2 rounded-lg transition-colors no-underline"
        >
          + Open Account
        </Link>
      </div>

      {/* Total Balance Card */}
      <div className="bg-indigo-950 rounded-2xl p-6 text-white shadow-lg">
        <p className="text-indigo-400 text-xs font-semibold uppercase tracking-widest">Total Balance</p>
        <p className="text-4xl font-bold mt-2 tracking-tight">
          {totalBalance.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}
        </p>
        <p className="text-indigo-400 text-sm mt-3">
          {accounts.length} {accounts.length === 1 ? 'account' : 'accounts'}
        </p>
      </div>

      {/* Accounts */}
      <div>
        <h2 className="text-base font-semibold text-slate-700 mb-4">Your Accounts</h2>

        {accounts.length === 0 ? (
          <div className="bg-white rounded-2xl border border-slate-200 p-12 text-center">
            <div className="text-4xl mb-3">🏦</div>
            <p className="text-slate-600 font-medium mb-1">No accounts yet</p>
            <p className="text-slate-400 text-sm mb-5">Open your first account to get started.</p>
            <Link
              to="/create-account"
              className="inline-block bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold px-5 py-2.5 rounded-lg transition-colors no-underline"
            >
              Open an Account
            </Link>
          </div>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2">
            {accounts.map((account) => {
              const isSavings = account.type === 'savings';
              return (
                <div
                  key={account.id}
                  className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:shadow-md transition-shadow"
                >
                  <div className="flex items-start justify-between">
                    <div>
                      <span
                        className={`inline-block text-xs font-bold px-2.5 py-1 rounded-full uppercase tracking-wide ${
                          isSavings
                            ? 'bg-emerald-100 text-emerald-700'
                            : 'bg-blue-100 text-blue-700'
                        }`}
                      >
                        {account.type}
                      </span>
                      <p className="text-2xl font-bold text-slate-900 mt-3 tracking-tight">
                        {account.balance.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}
                      </p>
                    </div>
                    <div
                      className={`w-11 h-11 rounded-xl flex items-center justify-center text-xl ${
                        isSavings ? 'bg-emerald-50' : 'bg-blue-50'
                      }`}
                    >
                      {isSavings ? '💰' : '💳'}
                    </div>
                  </div>
                  <p className="text-xs text-slate-400 mt-4 font-mono">
                    ···· {account.id.slice(-8).toUpperCase()}
                  </p>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
