// src/api/accountApi.ts
import { apiClient } from './client';
import type { Account, AccountType } from '../types'; 

export const accountApi = {
  // GET /api/accounts/{custID}
  getByCustomerId: (custID: string) => 
    apiClient(`/accounts/${custID}`) as Promise<Account[]>,

  // POST /api/accounts/{custID}
  // We pass both the URL parameter (custID) and the JSON body data (type, balance)
  create: (custID: string, data: { type: AccountType; balance: number }) => 
    apiClient(`/accounts/${custID}`, { 
      method: 'POST', 
      body: JSON.stringify(data) 
    }) as Promise<Account>,
};