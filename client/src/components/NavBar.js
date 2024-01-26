// NavBar.js

import React from "react";
import { NavLink } from "react-router-dom";

const NavBar = () => {
  return (
    <nav
      style={{ backgroundColor: "#000000" /* Black from your color palette */ }}
    >
      <NavLink
        to="/"
        exact
        activeClassName="active"
        style={{ color: "#FFFFFF" /* White from your color palette */ }}
      >
        Home
      </NavLink>
      <NavLink
        to="/elections/view"
        activeClassName="active"
        style={{ color: "#FFFFFF" }}
      >
        View Elections
      </NavLink>
      <NavLink
        to="/elections/add"
        activeClassName="active"
        style={{ color: "#FFFFFF" }}
      >
        Add Election
      </NavLink>
      {/* Removed NavLink to "/other" */}
    </nav>
  );
};

export default NavBar;
