import { createSelector } from 'reselect';
import { RootState } from '../store'; // Adjust path to your RootState

// Input selectors
const getStudentsState = (state: RootState) => state.students.students;
const getBooksState = (state: RootState) => state.books.books;

// Memoized selector
export const selectStudentsAndBooks = createSelector(
  [getStudentsState, getBooksState],
  (students, books) => ({ students, books })
);