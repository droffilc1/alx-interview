#!/usr/bin/node
// prints all characters of a Star Wars movie
const rp = require('request-promise');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function starwarsCharacters (movieId) {
  try {
    const body = await rp(url);
    const result = JSON.parse(body);
    for (const character of result.characters) {
      try {
        const characterBody = await rp(character);
        const characterResult = JSON.parse(characterBody);
        console.log(characterResult.name);
      } catch (characterError) {
        console.error(`Error fetching character: ${characterError}`);
      }
    }
  } catch (error) {
    console.error(`Error fetching movie: ${error}`);
  }
}

starwarsCharacters(movieId);
