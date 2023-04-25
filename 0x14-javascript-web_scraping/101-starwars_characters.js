#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log("Please provide a movie ID");
  process.exit(1);
}

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.log("Error getting movie information");
    process.exit(1);
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  const characterNames = [];
  let numCharactersProcessed = 0;
  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        console.log("Error getting character information");
        return;
      }
      const characterData = JSON.parse(body);
      characterNames[index] = characterData.name;
      numCharactersProcessed++;
      if (numCharactersProcessed === characters.length) {
        characterNames.forEach((name) => {
          console.log(name);
        });
      }
    });
  });
});

