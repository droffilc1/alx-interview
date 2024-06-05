#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const result = JSON.parse(body);
  for (const character of result.characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
