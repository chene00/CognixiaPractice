// src/types.ts

// FIX: Replaced 'enum' with a const object and derived type to satisfy 'erasableSyntaxOnly'
export const AccountType = {
    SAVINGS: "savings",
    CHECKING: "checking"
} as const;

export type AccountType = (typeof AccountType)[keyof typeof AccountType];


// Interface in TypeScript is a contract. 
// If we say something is a Customer, TypeScript will guarentee that it has these attributes
export interface Customer {
    id: string;
    name: string;
    email: string;
}

export interface Account {
    id: string;
    customer_id: string;
    type: AccountType;
    balance: number; 
}