// src/api/customerApi.ts
import { apiClient } from './client';
import type { Customer } from '../types'; 

// We export an object containing all the customer-related network requests
export const customerApi = {
  // GET /api/customers/
  getAll: () => apiClient('/customers/') as Promise<Customer[]>,
  
  // POST /api/customers/
  create: (data: { name: string; email: string , password: string}) => 
    apiClient('/customers/', { method: 'POST', body: JSON.stringify(data) }) as Promise<Customer>,
      
  // GET /api/customers/{id}  <-- We will use this one next for the View Customer page!
  getById: (id: string) => apiClient(`/customers/${id}`) as Promise<Customer>,
};