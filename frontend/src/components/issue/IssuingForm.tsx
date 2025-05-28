import { useState, useEffect, FormEvent } from 'react';
import { IssuingTransaction } from '../../types/issuing';
import { useNavigate } from 'react-router-dom';
import { useAppSelector } from '../../hooks/useAppSelector';
import { selectStudentsAndBooks } from '../../hooks/selectors';

interface IssuingFormProps {
  onSubmit: (transaction: IssuingTransaction) => void;
}

const IssuingForm: React.FC<IssuingFormProps> = ({ onSubmit }) => {
  const { tokens, userId, user_name } = useAppSelector((state) => state.auth);
  const { students, books } = useAppSelector(selectStudentsAndBooks); 
  const navigate = useNavigate();

  const [formData, setFormData] = useState<IssuingTransaction>({
    studentid: 0,
    user: userId || '',
    bookid: 0,
    transaction_type: 'borrow',
    date: new Date().toISOString().split('T')[0], 
  });
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!tokens || !userId || !user_name) {
      navigate('/login');
    } else {
      setFormData((prev) => ({ ...prev, user: userId })); 
    }
  }, [tokens, userId, user_name, navigate]);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (formData.studentid === 0 || formData.bookid === 0 || !formData.user) {
      setError('Please fill all required fields.');
      return;
    }
    onSubmit(formData);
    setFormData({
      studentid: 0,
      user: userId || '',
      bookid: 0,
      transaction_type: 'borrow',
      date: new Date().toISOString().split('T')[0],
    });
    setError(null);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === 'studentid' || name === 'bookid' ? Number(value) : value,
    }));
  };

  return (
    <div
      className="card mb-4"
      style={{
        background: '#E3E3E3',
        padding: '22px 34px',
        border: 'none',
        borderRadius: '8px',
        boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.1)',
      }}
    >
      {error && <div style={{ color: 'red', marginBottom: '10px' }}>{error}</div>}
      <form onSubmit={handleSubmit}>
        <div className="row mb-3">
          <div className="col-md-8">
            <label className="form-label" style={{ fontSize: '14px', fontWeight: 'bold', color: '#333' }}>
              Student
            </label>
            <select
              name="studentid"
              value={formData.studentid}
              onChange={handleChange}
              required
              style={{
                height: '65px',
                backgroundColor: '#D9D9D9',
                border: 'none',
                borderRadius: '4px',
                width: '100%',
                padding: '0 10px',
              }}
            >
              <option value={0} disabled>
                Select a Student
              </option>
              {students.map((student) => (
                <option key={student.studentid} value={student.studentid}>
                  {student.name}
                </option>
              ))}
            </select>
          </div>
          <div className="col-md-4">
            <label className="form-label" style={{ fontSize: '14px', fontWeight: 'bold', color: '#333' }}>
              Librarian
            </label>
            <input
              type="text"
              name="user"
              value={user_name || 'Unknown'}
              readOnly
              style={{
                height: '65px',
                backgroundColor: '#D9D9D9',
                border: 'none',
                borderRadius: '4px',
                width: '100%',
                padding: '0 10px',
                color: '#333',
                cursor: 'not-allowed',
              }}
            />
          </div>
        </div>

        <div className="row mb-3">
          <div className="col-md-6">
            <label className="form-label" style={{ fontSize: '14px', fontWeight: 'bold', color: '#333' }}>
              Book
            </label>
            <select
              name="bookid"
              value={formData.bookid}
              onChange={handleChange}
              required
              style={{
                height: '65px',
                backgroundColor: '#D9D9D9',
                border: 'none',
                borderRadius: '4px',
                width: '100%',
                padding: '0 10px',
              }}
            >
              <option value={0} disabled>
                Select a Book
              </option>
              {books.map((book) => (
                <option key={book.bookid} value={book.bookid}>
                  {book.title}
                </option>
              ))}
            </select>
          </div>
          <div className="col-md-6">
            <label className="form-label" style={{ fontSize: '14px', fontWeight: 'bold', color: '#333' }}>
              Transaction Type
            </label>
            <select
              name="transaction_type"
              value={formData.transaction_type}
              onChange={handleChange}
              required
              style={{
                height: '65px',
                backgroundColor: '#D9D9D9',
                border: 'none',
                borderRadius: '4px',
                width: '100%',
                padding: '0 10px',
              }}
            >
              <option value="borrow">Borrow</option>
              <option value="return">Return</option>
            </select>
          </div>
        </div>

        <div className="mb-3">
          <label className="form-label" style={{ fontSize: '14px', fontWeight: 'bold', color: '#333' }}>
            Date
          </label>
          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            required
            style={{
              height: '65px',
              backgroundColor: '#D9D9D9',
              border: 'none',
              borderRadius: '4px',
              width: '100%',
              padding: '0 10px',
            }}
          />
        </div>

        <button
          type="submit"
          className="btn"
          style={{
            backgroundColor: '#255D81',
            fontSize: '15px',
            fontWeight: 800,
            width: '160px',
            color: 'white',
            padding: '21px 56px',
            border: 'none',
            borderRadius: '20px',
          }}
        >
          ISSUE
        </button>
      </form>
    </div>
  );
};

export default IssuingForm;