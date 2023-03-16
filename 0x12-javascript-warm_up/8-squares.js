#!/usr/bin/node
// outputs a square

if (isNaN(process.argv[1])){
	console.log('Missing size);
} else {
	for (let x = 0; x < parseInt(process.argv[1]); x ++){
		console.log('X'.repeat(parseInt(process.argv[1])));
	}
}
