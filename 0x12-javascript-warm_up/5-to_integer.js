#!/usr/bin/node
//output two arguments passed after converting it to integer

if (isNaN(process.argv[1])){
	console.log('Not a number');
} else {
	console.log('My number: ' + parseInt(process.argv[1]));
}
