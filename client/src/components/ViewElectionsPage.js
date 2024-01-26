import React, { useEffect, useState } from "react";

const ViewElectionsPage = () => {
  const [elections, setElections] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/elections")
      .then((response) => response.json())
      .then((data) => setElections(data))
      .catch((error) => console.error("Error fetching elections:", error));
  }, []);

  return (
    <div style={{ backgroundColor: "#FFFFFF" }}>
      {elections ? (
        <div>
          {elections.map((election, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ccc",
                padding: "10px",
                margin: "10px 0",
                borderRadius: "5px",
              }}
            >
              <h2>{election.name}</h2>
              <p>
                <strong>Date:</strong> {election.date}
              </p>
              <p>
                <strong>Type:</strong> {election.election_type || "N/A"}
              </p>
              <p>
                <strong>State:</strong> {election.state || "N/A"}
              </p>
              <p>
                <strong>County:</strong> {election.county || "N/A"}
              </p>
              {/* You can include other fields like polls and propositions as needed */}
            </div>
          ))}
        </div>
      ) : (
        "Loading..."
      )}
    </div>
  );
};

export default ViewElectionsPage;
