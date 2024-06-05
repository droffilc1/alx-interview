#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error('Received status code ' + response.statusCode));
      } else {
        resolve(body);
      }
    });
  });
};

const fetchCharacterName = async (url) => {
  try {
    const charBody = await makeRequest(url);
    const characterData = JSON.parse(charBody);
    return characterData.name;
  } catch (error) {
    console.error('Error fetching character:', error);
  }
};

const printCharacterNames = async () => {
  try {
    const body = await makeRequest(url);
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;

    for (const characterUrl of charactersUrls) {
      const characterName = await fetchCharacterName(characterUrl);
      if (characterName) {
        console.log(characterName);
      }
    }
  } catch (error) {
    console.error('Error fetching film data:', error);
  }
};

printCharacterNames();
