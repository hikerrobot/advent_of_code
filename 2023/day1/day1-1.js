import fs from 'node:fs';
import { stringify } from 'node:querystring';
var debug = 1

function logMessage(message) {
  if (debug) {
    console.log(message);
  }
}

function extractInput(input, separator) {
    let debug = 0;

    let startPos = 0, foundSepPos = 0;
    let extract = [];
    logMessage(input)
    logMessage(input.length)

    let iteration = 0;
    while (foundSepPos <= input.length) {
      logMessage("searching from pos "+ startPos)
        foundSepPos = input.indexOf(separator, startPos)
        logMessage("foundSepPos " +foundSepPos)
        if (foundSepPos === -1) {
          logMessage("* not found -ret")
          if (startPos < input.length) {
            console.log('final token = ' + input.substring(startPos, input.length))
            extract.push(input.substring(startPos, input.length))
          }
          break;
        }
        // logMessage(input.substring)
        // logMessage("foundSepPos", foundSepPos, "startPos", startPos);
        const foundStr = input.substring(startPos, foundSepPos)
        logMessage("storing " + foundStr)
        // move beyond last found separator - vital!
        startPos = foundSepPos + 1;
        extract.push(foundStr)
        iteration++
        // if (iteration === 3) {
        //     break;
        // }
    }
    
    // logMessage(extract)
    return extract
    // console.log("separator found at ",foundSepPos);
}

function getNumbers(numbers) {
  logMessage('in getNumbers'+'length = '+numbers.length)
  // get first number
  const firstNum = numbers[0];
  const lastNum = numbers[numbers.length-1]
  const foundNums =  String(firstNum).concat(lastNum);
  logMessage('foundNums = '+foundNums)
  return foundNums
}

function getCalibrationValues(inputLine) {
  // need to get first and last numbers and combine them
  // nb not always 2 numbers in line

  let numMatch = inputLine.match(/\d{1}/g);
  if (!numMatch) {
    throw "no numbers found in line :-/"
  }
  // console.log(numMatch)
  return Number(getNumbers(numMatch));
}

fs.readFile('./input-d1', 'utf8', (err, data) => {
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
  // console.log(extract);
  console.log('extract len' + extract.length)
  
  let total = 0;

  extract.forEach((line) => {

    logMessage('line = ' + line)
    total = total + getCalibrationValues(line)
  })
  logMessage('total = ' + total)

});