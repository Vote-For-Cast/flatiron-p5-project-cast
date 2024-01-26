import React from "react";
import { NavLink } from "react-router-dom";

const NavBar = () => {
  const linkStyle = {
    color: "#FFFFFF", // White from your color palette
    marginRight: "10px", // Adjust as needed
    textDecoration: "none", // Optional, for removing underline from links
  };

  return (
    <nav
      style={{ backgroundColor: "#000000" /* Black from your color palette */ }}
    >
      <NavLink to="/" exact activeClassName="active" style={linkStyle}>
        Home
      </NavLink>
      <NavLink to="/elections/view" activeClassName="active" style={linkStyle}>
        View Elections
      </NavLink>
      <NavLink to="/elections/add" activeClassName="active" style={linkStyle}>
        Add Election
      </NavLink>
      {/* Removed NavLink to "/other" */}
    </nav>
  );
};

export default NavBar;
