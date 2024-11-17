#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getReq (url) {
  const res = new Promise(function (resolve, reject) {
    request(url, function (error, response, body) {
      if (error) {
        // pass
      }

      if (response.statusCode === 200) {
        const person = JSON.parse(body);
        resolve(person.name);
      } else {
        reject(response);
      }
    });
  });
  return res;
}

request(url, function (error, response, body) {
  if (error) {
    // pass
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  const promises = characters.map(character => getReq(character));
  Promise.all(promises)
    .then(results => {
      results.forEach(result => console.log(result));
    })
    .catch(error => {
      console.log(error);
    });
});
