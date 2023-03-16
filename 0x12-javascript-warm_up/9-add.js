#!/usr/bin/node
//prints an addition of two integers

function add(x, y) {
	return parseInt(x) + parseInt(y);
}

console.log(add(process.argv[1], process.argv[3]));
