// src/pages/CustomerList.tsx
import { useEffect, useState } from 'react';
import { type Customer } from '../types';
import { Link } from 'react-router-dom';
import { customerApi } from '../api/customerApi'; // 1. Import our central API service

export default function CustomerList() {
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCustomers = async () => {
      try {
        // 2. We replace the raw fetch() and manual error checking with a single, clean function call!
        const data = await customerApi.getAll();
        
        if (Array.isArray(data)) {
          setCustomers(data);
        } else {
          setCustomers([]);
        }
      } catch (err: any) {
        console.error("Error fetching customers:", err);
        setError(err.message || "Could not connect to the banking server.");
      } finally {
        setLoading(false);
      }
    };

    fetchCustomers();
  }, []);

  if (loading) return <p style={{ padding: '2rem' }}>Loading customers...</p>;
  if (error) return <p style={{ padding: '2rem', color: '#ff4d4d' }}>{error}</p>;

  return (
    <div>
      <h2 style={{ fontSize: '2rem', marginBottom: '1.5rem' }}>Bank App Customers</h2>
      
      {customers.length === 0 ? (
        <p>No customers found in the database. Try creating one!</p>
      ) : (
        <ul style={{ listStyleType: 'square', lineHeight: '1.8' }}>
            {customers.map((customer) => (
            <li key={customer.id} style={{ marginBottom: '0.5rem' }}>
                {/* Make the name clickable, routing to /customer/{their actual ID} */}
                <Link to={`/customer/${customer.id}`} style={{ color: 'var(--text-h)', textDecoration: 'none' }}>
                <strong>{customer.name}</strong>
                </Link> 
                {' '}— <span style={{ color: 'var(--text)' }}>{customer.email}</span>
            </li>
            ))}
        </ul>
      )}
    </div>
  )
}