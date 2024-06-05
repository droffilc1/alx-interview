#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request-promise-native');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.log('Usage: ./0-starwars_character MovieID');
  process.exit(1);
}

async function fetchCharacterName (characterUrl) {
  try {
    const characterBody = await request(characterUrl);
    const characterData = JSON.parse(characterBody);
    return characterData.name;
  } catch (error) {
    console.error('Error fetching character:', error);
  }
}

async function printCharacterNames () {
  try {
    const body = await request(url);
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    for (const characterUrl of characterUrls) {
      const characterName = await fetchCharacterName(characterUrl);
      if (characterName) {
        console.log(characterName);
      }
    }
  } catch (error) {
    console.error('Error fetching film data:', error);
  }
}

printCharacterNames();
