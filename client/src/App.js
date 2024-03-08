// In src/App.js
import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
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
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/profile" component={Profile} />
          <Route path="/signup" component={SignUp} />
          <Route path="/login" component={Login} />
          <Route path="/logout" component={Logout} />
        </Switch>
      </div>
      <Footer />
    </Router>
  );
}

export default App;
