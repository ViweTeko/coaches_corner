import React, { useState, useEffect } from "react";
import axios from "axios";

const Data = () => {
  const [players, setPlayers] = useState([]);

  // Function to fetch player data from Django API
  const fetchPlayers = async () => {
    try {
      const response = await axios.get("/api/players/"); // Replace with your API endpoint
      setPlayers(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  // Function to handle player deletion (replace with your Django DELETE logic)
  const deletePlayer = async (playerId) => {
    try {
      const response = await axios.delete(`/api/players/${playerId}/`);
      setPlayers(players.filter((player) => player.id !== playerId));
    } catch (error) {
      console.error(error);
    }
  };

  // Fetch data on component mount
  useEffect(() => {
    fetchPlayers();
  }, []);

  return (
    <div>
      <h1>Players Data</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Weight</th>
            <th>Height</th>
            <th>School</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {players.map((player) => (
            <tr key={player.id}>
              <td>{player.name}</td>
              <td>{player.age}</td>
              <td>{player.weight}</td>
              <td>{player.height}</td>
              <td>{player.school}</td>
              <td>
                <button onClick={() => deletePlayer(player.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Data;
