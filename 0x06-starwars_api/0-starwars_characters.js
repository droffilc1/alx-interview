#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.log('Please provide a Movie ID');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error: Received status code', response.statusCode);
    return;
  }

  // Parse the response body as JSON
  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;

  charactersUrls.forEach(url => {
    request(url, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error: Received a status code', charResponse.statusCode);
        return;
      }
      // Parse the character response body as JSON
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
