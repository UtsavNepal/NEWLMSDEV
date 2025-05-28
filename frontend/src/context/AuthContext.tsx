import React, { createContext, useState, useContext, useEffect } from 'react';
import { Tokens } from '../types/model';
import { TokenService } from '../services/tokenManagement/TokenService';
import { isTokenExpired } from '../services/Utils/tokenUtils';

interface AuthContextType {
  tokens: Tokens | null;
  userId: string | null;
  username: string | null;
  login: (tokens: Tokens, username: string) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [tokens, setTokens] = useState<Tokens | null>(TokenService.getTokens());
  const [userId, setUserId] = useState<string | null>(() => sessionStorage.getItem('userId'));
  const [username, setUsername] = useState<string | null>(() => sessionStorage.getItem('username'));

  const login = (newTokens: Tokens, newUsername: string) => {
    setTokens(newTokens);
    setUserId(newTokens.userId?.toString() || null);
    setUsername(newUsername);
    TokenService.setTokens(newTokens);
    sessionStorage.setItem('userId', newTokens.userId?.toString() || '');
    sessionStorage.setItem('username', newUsername);
  };

  // ... rest of the component remains the same

  const logout = () => {
    setTokens(null);
    setUserId(null);
    setUsername(null);
    TokenService.clearTokens();
    setTimeout(() => {
      if (window.location.pathname !== '/login') {
        window.location.href = '/login';
      }
    }, 100);
  };

  useEffect(() => {
    const validateTokens = () => {
      const currentTokens = TokenService.getTokens();
      if (!currentTokens || !currentTokens.refreshToken || isTokenExpired(currentTokens.refreshToken)) {
        logout();
      } else if (currentTokens.accessToken && isTokenExpired(currentTokens.accessToken)) {
        setTokens(currentTokens);
      } else {
        setTokens(currentTokens);
        setUserId(sessionStorage.getItem('userId'));
        setUsername(sessionStorage.getItem('username'));
      }
    };

    validateTokens();
    window.addEventListener('storage', validateTokens);
    return () => window.removeEventListener('storage', validateTokens);
  }, []);

  return (
    <AuthContext.Provider value={{ tokens, userId, username, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};