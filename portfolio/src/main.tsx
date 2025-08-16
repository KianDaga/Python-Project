import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import GitProfile from './components/gitprofile.tsx';
import Splash from './components/splash/index.tsx';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path={CONFIG.base} element={<Splash />} />
        <Route path="home" element={<GitProfile config={CONFIG} />} />
      </Routes>
    </BrowserRouter>
    <GitProfile config={CONFIG} />
  </React.StrictMode>,
);
