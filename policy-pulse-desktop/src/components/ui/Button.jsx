import React from 'react';

/**
 * Reusable button component with different variants
 */
const Button = ({ children, variant = 'primary', onClick, disabled = false }) => {
  const getVariantClass = () => {
    switch (variant) {
      case 'secondary':
        return 'btn-secondary';
      case 'danger':
        return 'btn-danger';
      default:
        return 'btn-primary';
    }
  };

  return (
    <button
      className={`btn ${getVariantClass()}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};

export default Button;