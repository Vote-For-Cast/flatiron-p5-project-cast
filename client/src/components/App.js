// App.js

import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import HomePage from "./HomePage";
import ViewElectionsPage from "./ViewElectionsPage";
import AddElectionPage from "./AddElectionPage";

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/elections/view" component={ViewElectionsPage} />
        <Route path="/elections/add" component={AddElectionPage} />
      </Switch>
    </Router>
  );
}

export default App;
