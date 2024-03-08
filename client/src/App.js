// In src/App.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignUp from "./pages/SignUp.js";
import Login from "./pages/Login.js";
import Home from "./pages/Home.js";
import Profile from "./pages/Profile.js";
import NavBar from "./components/NavBar.js";
import Footer from "./components/Footer.js";
import Logout from "./pages/Logout.js";

function App() {
  return (
    <Router>
      <NavBar />
      <div className="min-h-screen">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>
      </div>
      <Footer />
    </Router>
  );
}

export default App;
