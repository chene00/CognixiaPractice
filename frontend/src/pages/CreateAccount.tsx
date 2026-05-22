import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AccountType } from '../types';
import { accountApi } from '../api/accountApi';
import { getUserIdFromToken } from '../api/authApi';

export default function CreateAccount() {
  const [type, setType] = useState<AccountType>(AccountType.CHECKING);
  const [balance, setBalance] = useState<number | ''>('');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    const userId = getUserIdFromToken();
    if (!userId) {
      setError('You must be logged in to do this.');
      return;
    }

    setLoading(true);
    try {
      await accountApi.create(userId, { type, balance: Number(balance) });
      navigate('/');
    } catch (err: any) {
      setError(err.message || 'Failed to open account. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const accountOptions = [
    {
      value: AccountType.CHECKING,
      label: 'Checking',
      icon: '💳',
      description: 'For everyday spending',
    },
    {
      value: AccountType.SAVINGS,
      label: 'Savings',
      icon: '💰',
      description: 'Grow your money',
    },
  ];

  return (
    <div className="min-h-[72vh] flex items-center justify-center">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-2xl border border-slate-200 shadow-sm p-8">
          <div className="mb-7">
            <h1 className="text-2xl font-bold text-slate-900">Open a new account</h1>
            <p className="text-slate-500 text-sm mt-1">Choose a type and set your initial deposit</p>
          </div>

          {error && (
            <div className="mb-5 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg text-sm">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-3">Account Type</label>
              <div className="grid grid-cols-2 gap-3">
                {accountOptions.map((opt) => (
                  <button
                    key={opt.value}
                    type="button"
                    onClick={() => setType(opt.value)}
                    className={`p-4 rounded-xl border-2 text-left transition-all cursor-pointer ${
                      type === opt.value
                        ? 'border-indigo-500 bg-indigo-50'
                        : 'border-slate-200 hover:border-slate-300 bg-white'
                    }`}
                  >
                    <div className="text-2xl mb-1.5">{opt.icon}</div>
                    <div className="text-sm font-semibold text-slate-900">{opt.label}</div>
                    <div className="text-xs text-slate-500 mt-0.5">{opt.description}</div>
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1.5">Initial Deposit</label>
              <div className="relative">
                <span className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm font-medium pointer-events-none">
                  $
                </span>
                <input
                  type="number"
                  step="0.01"
                  min="0"
                  value={balance}
                  onChange={(e) => setBalance(e.target.value === '' ? '' : Number(e.target.value))}
                  required
                  placeholder="0.00"
                  className="w-full pl-8 pr-3.5 py-2.5 border border-slate-300 rounded-lg text-sm text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white font-semibold py-2.5 rounded-lg text-sm transition-colors cursor-pointer border-0"
            >
              {loading ? 'Opening account...' : 'Open Account'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
