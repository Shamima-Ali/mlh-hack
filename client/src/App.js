//import './App.css';
import * as React from 'react';
import { useState, useEffect } from 'react';
import Lottie from 'react-lottie';
import waterData from './water-animation.json';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import DisplayData from './DisplayData/DisplayData';

function App() {
  const [location, setLocation] = React.useState('');
  const [locationData, setLocationData] = React.useState([{}]);

  const defaultOptions = {
    loop: true,
    autoplay: true, 
    animationData: waterData,
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  };

  const handleChange = (event) => {
    setLocation(event.target.value);
    fetchData(event.target.value);
  };

  const fetchData = (value) => {
    console.log(String(`/${value}`));
    fetch(`http://127.0.0.1:5000/${value}`)
    .then(response => response.json())
    .catch(function (err) {
      console.log(err)
    })
    .then(
        data => {
          setLocationData(data);
          console.log(data);
    })
  }

  const displayData = () => {
    if (locationData !== null) {
    return (
      <DisplayData data={locationData} />
    )
  }
}
   
  return (
    <div className="container">

    <Lottie 
        background="transparent" 
        options={defaultOptions}
        height={200}
        width={200}
      />

    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel>Select a location</InputLabel>
        <Select
          value={location}
          label="Select a location"
          onChange={handleChange}
        >
          <MenuItem value={1}>Middle Cove</MenuItem>
          <MenuItem value={2}>Rotary Topsail</MenuItem>
        </Select>
      </FormControl>
    </Box>
{displayData()}
    </div>

  );
}

export default App;
