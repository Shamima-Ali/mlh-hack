import * as React from 'react';
import { useState, useEffect } from 'react';
import { Chart } from "react-google-charts";

function DisplayData({data}) {

    var info = [
        ["Recorded hour - current hour", "Tide Height"],
    ];

    const convertTime = (time) => {
        var timeSinceinHours = Math.round(((Date.now() - Date.parse(time)) / 1000)/ 60 / 60, 2);
        console.log(timeSinceinHours);
        return timeSinceinHours;
    }


    if (data.data !== undefined) {
        // console.log(data.data[0].height);
        
        data.data.forEach(element => {
            info.push([convertTime(element.time), element.height*100]);
        })
    
    }

console.log(info);
    

    return data.data && (
        <Chart
            chartType="LineChart"
            data={info}
            width="100%"
            height="400px"
            />
    )

}

export default DisplayData;
