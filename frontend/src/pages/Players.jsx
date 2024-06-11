import React, { useState, useEffect } from "react";
import axios from "axios";
import api from "../api";

const Data = () => {
  const [players, setPlayers] = useState([]);
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [school, setSchool] = useState("");
  const [age, setAge] = useState("");
  const [weight, setWeight] = useState("");
  const [height, setHeight] = useState("");

  // Function to fetch player data from Django API
  const fetchPlayers = (e) => {
    e.preventDefault();
    api
      .post("/api/players/", {
        first_name, last_name, school, age, weight, height})
        .then((res) => {
          if (res.status === 201) alert("Player added");
          else alert("Failed to add player.");
          addPlayer();
        })
        .catch ((error) => alert(error));
  };

  // Function to handle player deletion (replace with your Django DELETE logic)
  const deletePlayer = async (playerID) => {
    api
      .delete(`/api/players/info/${playerID}/`)
      .then((res) => {
        if (res.status === 204) alert("Player deleted");
        else alert("Failed to delete player.");
        fetchPlayers();
      })
      .catch ((error) => alert(error));
  };

  const addPlayer = async () => {
    api
      .get("/api/players/")
      .then((res) => res.data)
      .then((data) => {
        setPlayers(data);
        console.log(data);
      })
      .catch((err) => alert(err));
  };

  useEffect(() => {
    fetchPlayers();
  }, []);

  return (
    <div>
      <h1>Players Data</h1>
      <table>
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Age</th>
            <th>Weight</th>
            <th>Height</th>
            <th>School</th>
          </tr>
        </thead>
        <tbody>
          {players.map((player) => (
            <tr key={player.id}>
              <td>{player.firstName}</td>
              <td>{player.lastName}</td>
              <td>{player.age}</td>
              <td>{player.weight}</td>
              <td>{player.height}</td>
              <td>{player.school}</td>
              <td>
                <button onClick={() => deletePlayer(player.id)}>Delete Player</button>
                <button onClick={() => addPlayer(player.id)}>Add Player</button>
                <button onClick={() => updatePlayer(player.id)}>Update Player</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Data;
