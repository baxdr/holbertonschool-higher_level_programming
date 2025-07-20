#!/usr/bin/node
// JS script

document.getElementById('#update_header').addEventListener('click', function () {
    document.querySelector('header').textContent = 'New Header!';
});