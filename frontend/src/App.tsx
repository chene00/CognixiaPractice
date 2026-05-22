import { useState } from 'react';
import { Routes, Route, Link, Navigate } from 'react-router-dom';
import CreateCustomer from './pages/CreateCustomer';
import CreateAccount from './pages/CreateAccount';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import { authApi } from './api/authApi';

function App() {
  const [token, setToken] = useState<string | null>(localStorage.getItem('access_token'));

  const handleLogout = () => {
    authApi.logout();
    setToken(null);
  };

  return (
    <div className="min-h-screen bg-slate-50">
      <nav className="bg-indigo-950 shadow-lg">
        <div className="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
          <Link to="/" className="flex items-center gap-2.5 no-underline">
            <div className="w-8 h-8 bg-indigo-500 rounded-lg flex items-center justify-center text-white font-bold text-sm">V</div>
            <span className="text-white font-semibold text-lg tracking-tight">Random Bank</span>
          </Link>

          <div className="flex items-center gap-2">
            {token ? (
              <>
                <Link to="/" className="text-indigo-300 hover:text-white px-3 py-1.5 rounded-lg text-sm font-medium transition-colors no-underline">
                  Dashboard
                </Link>
                <Link to="/create-account" className="text-indigo-300 hover:text-white px-3 py-1.5 rounded-lg text-sm font-medium transition-colors no-underline">
                  Open Account
                </Link>
                <button
                  onClick={handleLogout}
                  className="ml-2 bg-indigo-800 hover:bg-indigo-700 text-white px-4 py-1.5 rounded-lg text-sm font-medium transition-colors cursor-pointer border-0"
                >
                  Sign Out
                </button>
              </>
            ) : (
              <>
                <Link to="/login" className="text-indigo-300 hover:text-white px-3 py-1.5 rounded-lg text-sm font-medium transition-colors no-underline">
                  Sign In
                </Link>
                <Link to="/register" className="bg-indigo-500 hover:bg-indigo-400 text-white px-4 py-1.5 rounded-lg text-sm font-medium transition-colors no-underline">
                  Register
                </Link>
              </>
            )}
          </div>
        </div>
      </nav>

      <main className="max-w-5xl mx-auto px-6 py-10">
        <Routes>
          <Route path="/login" element={<Login onLoginSuccess={() => setToken(localStorage.getItem('access_token'))} />} />
          <Route path="/register" element={<CreateCustomer />} />
          <Route path="/" element={token ? <Dashboard /> : <Navigate to="/login" />} />
          <Route path="/create-account" element={token ? <CreateAccount /> : <Navigate to="/login" />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
