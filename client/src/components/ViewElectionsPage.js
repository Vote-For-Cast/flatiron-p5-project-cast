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
        <pre>{JSON.stringify(elections, null, 2)}</pre>
      ) : (
        "Loading..."
      )}
    </div>
  );
};

export default ViewElectionsPage;
