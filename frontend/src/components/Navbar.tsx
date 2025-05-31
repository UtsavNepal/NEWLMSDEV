import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { MdDashboard, MdPerson, MdBook, MdPeople, MdSwapHoriz, MdAssignmentReturn, MdLogout } from 'react-icons/md';
import Nav from '../assets/NAV.svg';
import { logout } from '../store/slices/authSlice';
import { useAppDispatch } from '../hooks/useAppDispatch';

const navLinks = [
  { path: '/dashboard', icon: <MdDashboard size={20} />, label: 'Dashboard' },
  { path: '/author', icon: <MdPerson size={20} />, label: 'Author' },
  { path: '/book', icon: <MdBook size={20} />, label: 'Books' },
  { path: '/student', icon: <MdPeople size={20} />, label: 'Students' },
  { path: '/transaction-view', icon: <MdSwapHoriz size={20} />, label: 'Transactions' },
  { path: '/issue', icon: <MdAssignmentReturn size={20} />, label: 'Issuing' },
];

const Navbar: React.FC = () => {
  const navigate = useNavigate();
  const dispatch = useAppDispatch();

  const handleLogout = () => {
    dispatch(logout());
    navigate('/');
  };

  return (
    <nav className="fixed top-0 left-0 w-[222px] h-screen bg-[#255D81] text-white flex flex-col items-center pt-[51px] shadow-[2px_0_5px_rgba(0,0,0,0.2)] z-[1030]">
      <div>
        <img src={Nav} alt="Logo" className="w-[152px] h-[62px]" />
      </div>

      <div className="flex flex-col items-start w-full mt-5">
        {navLinks.map((link) => (
          <Link
            key={link.path}
            to={link.path}
            className="flex items-center w-full p-3 text-white hover:bg-white hover:text-black transition-all duration-300"
          >
            <span className="w-5 h-5 mr-2">{link.icon}</span>
            {link.label}
          </Link>
        ))}
      </div>

      <div className="group mt-auto w-full">
        <button
          onClick={handleLogout}
          className="flex items-center w-full p-3 text-white hover:bg-white hover:text-black transition-all duration-300"
        >
          <span className="w-5 h-5 mr-2"><MdLogout size={20} /></span>
          Logout
        </button>
      </div>
    </nav>
  );
};

export default Navbar;