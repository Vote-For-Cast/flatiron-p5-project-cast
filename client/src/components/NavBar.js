// In src/components/NavBar.js
import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/cast-logo-white@2x.png";

function NavBar() {
  return (
    <nav
      style={{
        backgroundColor: "var(--text-color)",
        padding: "20px",
        height: "60px",
      }}
    >
      <div className="cast-logo">
        <img src={logo} alt="Cast Logo" />
      </div>
      <ul
        style={{
          listStyle: "none",
          display: "flex",
          gap: "20px",
          margin: "0",
          padding: "0",
        }}
      >
        <li>
          <Link
            to="/"
            style={{ textDecoration: "none", color: "var(--background-color)" }}
          >
            Home
          </Link>
        </li>
        <li>
          <Link
            to="/signup"
            style={{ textDecoration: "none", color: "var(--background-color)" }}
          >
            Sign Up
          </Link>
        </li>
        <li>
          <Link
            to="/login"
            style={{ textDecoration: "none", color: "var(--background-color)" }}
          >
            Login
          </Link>
        </li>
        <li>
          <Link
            to="/profile"
            style={{ textDecoration: "none", color: "var(--background-color)" }}
          >
            Profile
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;
