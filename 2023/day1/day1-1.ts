// import * as fs from 'fs';
import { readFile } from 'fs'
// import fs from 'node:fs';

var debug = 1


function logMessage(message: string) {
  if (debug) {
    console.log(message);
  }
}

function extractInput(input: string, separator: string) {
    let debug = 0;

    let startPos = 0, foundSepPos = 0;
    let extract: string[] = []
    logMessage(input)

    let iteration = 0;
    while (foundSepPos < input.length) {
      // logMessage("searching from pos", startPos)
        foundSepPos = input.indexOf(separator, startPos)
        // logMessage("foundSepPos", foundSepPos)
        if (foundSepPos === -1) {
          logMessage("* not found -ret")
            return;
        }
        // logMessage(input.substring)
        // logMessage("foundSepPos", foundSepPos, "startPos", startPos);
        const foundStr = input.substring(startPos, foundSepPos)
        // logMessage("storing ", foundStr)
        // move beyond last found separator - vital!
        startPos = foundSepPos + 1;
        extract.push(foundStr)
        iteration++
        if (iteration === 3) {
            break;
        }
    }
    
    return extract
    // console.log("separator found at ",foundSepPos);
}


function getNumbers(numbers) {
  
}

function getCalibrationValues(inputLine) {
  // need to get first and last numbers and combine them
  // nb not always 2 numbers in line

  let numMatch = inputLine.match(/\d{1}/g);
  if (!numMatch) {
    throw "no numbers found in line :-/"
  }
  console.log(numMatch)
}

readFile('./input-d1', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
//   console.log(typeof data)
//   console.log(data.substring(0,9))
//   console.log(data);
  // for each new line char, using index push into array
//   console.log(data.indexOf("\n"))
  const extract = extractInput(data, "\n")
  console.log(extract);
  console.log('extract len', extract.length)
  
  extract.forEach((line) => {
    getCalibrationValues(line)
  })

});