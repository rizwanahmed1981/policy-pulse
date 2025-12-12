import React from 'react';

/**
 * Header component for the Policy Pulse desktop application
 */
const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <h1>Policy Pulse</h1>
        <nav className="navigation">
          <ul>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="#documents">Documents</a></li>
            <li><a href="#chat">Chat</a></li>
            <li><a href="#settings">Settings</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;