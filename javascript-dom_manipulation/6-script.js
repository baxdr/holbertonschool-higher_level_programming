#!/usr/bin/node
// JS script

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.querySelector('header').textContent = data.name;
  });