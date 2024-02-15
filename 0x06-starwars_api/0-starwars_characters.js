#!/usr/bin/node
const request = require('request');

const fetchData = async (id) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  try {
    const { body } = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve({ body });
        }
      });
    });
    const { characters } = JSON.parse(body);
    return characters;
  } catch (error) {
    console.error(error);
  }
};

const fetchCharacter = async (characterUrl) => {
  try {
    const { body } = await new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve({ body });
        }
      });
    });
    return JSON.parse(body);
  } catch (error) {
    console.error(error);
  }
};

const fetchCharacters = async (characterUrls) => {
  try {
    for (const characterUrl of characterUrls) {
      const character = await fetchCharacter(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
};

const main = async () => {
  try {
    const id = process.argv[2];
    const characterUrls = await fetchData(id);
    await fetchCharacters(characterUrls);
  } catch (error) {
    console.error(error);
  }
};

main();
