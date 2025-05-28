import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { toast } from 'react-toastify';
import DashboardHeader from '../components/dashboard/DashboardHeader';
import PieChart from '../components/dashboard/PieChart';
import StatsCard from '../components/dashboard/StatsCard';
import OverdueBorrowers from '../components/dashboard/OverdueBorrowers';
import TotalBook from '../assets/DashBook.svg';
import TotalUser from '../assets/DashUser.svg';
import TotalTrans from '../assets/DashTrans.svg';
import { fetchDashboardData } from '../store/slices/dashboardSlice';
import { useAppDispatch } from '../hooks/useAppDispatch';
import { useAppSelector } from '../hooks/useAppSelector';

const DashboardPage: React.FC = () => {
  const dispatch = useAppDispatch();
  const { data, overdueBorrowers, loading, error } = useAppSelector((state) => state.dashboard);
  const { user_name } = useAppSelector((state) => state.auth);
  const location = useLocation();

  useEffect(() => {
    if (location.state?.showLoginToast) {
      toast.success('Successfully logged in!', {
        position: 'top-right',
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
      });
    }
    dispatch(fetchDashboardData());
  }, [location.state, dispatch]);

  if (loading) {
    return <div className="flex justify-center items-center h-screen">Loading...</div>;
  }

  if (error || !data) {
    return <div className="flex justify-center items-center h-screen text-red-500">{error || 'No data available'}</div>;
  }

  return (
    <div className="ml-[222px] pt-[65px]">
      <DashboardHeader username={user_name || 'User'} />
      <div className="bg-[#F2F2F2] p-5">
        <div className="flex flex-wrap -mx-3">
          <div className="w-full lg:w-1/2 px-3">
            <PieChart total_borrowed_books={data.total_borrowed_books} total_returned_books={data.total_returned_books} />
          </div>
          <div className="w-full lg:w-1/2 px-3">
            <StatsCard icon={TotalUser} count={data.total_student_count} label="Total Student" />
            <StatsCard icon={TotalBook} count={data.total_book_count} label="Total Book Count" />
            <StatsCard icon={TotalTrans} count={data.total_transaction_count} label="Transactions Count" />
            <OverdueBorrowers borrowers={overdueBorrowers} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;