import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { Transaction } from '../../types/transaction';
import { fetchTransactions } from '../../services/transactionService';
import { createTransaction } from '../../services/IssuingService';
import { IssuingTransaction } from '../../types/issuing';
import { RootState } from '../index';

interface TransactionsState {
  transactions: Transaction[];
  loading: boolean;
  error: string | null;
}

const initialState: TransactionsState = {
  transactions: [],
  loading: false,
  error: null,
};

export const fetchTransactionsAsync = createAsyncThunk('transactions/fetchTransactions', async (_, { rejectWithValue }) => {
  try {
    const transactions = await fetchTransactions();
    return transactions;
  } catch (err) {
    return rejectWithValue('Failed to fetch transactions.');
  }
});

export const createTransactionAsync = createAsyncThunk<
  Transaction,
  IssuingTransaction,
  { state: RootState }
>('transactions/createTransaction', async (transaction: IssuingTransaction, { rejectWithValue, getState }) => {
  try {
    // Create the transaction on the backend
    await createTransaction(transaction);

    // Since the backend returns only the transactionId, we need to fetch the full transaction
    // or construct it manually. For now, assume the backend will return the full object
    // via a follow-up GET request (simplified here for demonstration)
    const response = await fetch(`/transactions/`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${getState().auth.tokens?.accessToken}`,
      },
    });

    if (!response.ok) {
      throw new Error('Failed to fetch created transaction');
    }

    const createdTransaction = await response.json() as Transaction;
    return createdTransaction;
  } catch (err: any) {
    const errorMessage = err.response?.data?.message || err.response?.data || err.message || 'Failed to issue book.';
    return rejectWithValue(errorMessage);
  }
});

const transactionsSlice = createSlice({
  name: 'transactions',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchTransactionsAsync.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchTransactionsAsync.fulfilled, (state, action) => {
        state.loading = false;
        state.transactions = action.payload;
      })
      .addCase(fetchTransactionsAsync.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      .addCase(createTransactionAsync.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(createTransactionAsync.fulfilled, (state, action) => {
        state.loading = false;
        state.transactions.push(action.payload);
      })
      .addCase(createTransactionAsync.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

export default transactionsSlice.reducer;