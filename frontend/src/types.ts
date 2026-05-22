export enum AccountType {
    SAVINGS = "savings",
    CHECKING = "checking"
}

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