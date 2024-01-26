import React, { useState } from "react";

const AddElectionPage = () => {
  const [formData, setFormData] = useState({
    name: "",
    date: "",
    election_type: "",
    state: "",
    county: "",
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("http://127.0.0.1:5555/elections", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: formData.name,
        date: formData.date,
        election_type: formData.election_type,
        state: formData.state,
        county: formData.county,
      }),
    })
      .then((response) => response.json())
      .then((data) => console.log("Election added:", data))
      .catch((error) => console.error("Error:", error));
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <form onSubmit={handleSubmit} style={{ backgroundColor: "#FFFFFF" }}>
      <input
        type="text"
        name="name"
        onChange={handleChange}
        placeholder="Election Name"
      />
      <input
        type="date"
        name="date"
        onChange={handleChange}
        placeholder="Date"
      />
      {/* Add more inputs for election_type, state, county */}
      <button type="submit">Add Election</button>
    </form>
  );
};

export default AddElectionPage;
