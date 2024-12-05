import React from "react";
import { Link } from "react-router-dom";
import "./LinkButton.css";

const LinkButton = ({ to, children, variant = "primary" }) => {
  return (
    <Link to={to} className={`link-button ${variant}`}>
      {children}
    </Link>
  );
};

export default LinkButton;
