#!/usr/bin/node
//print output based on argument passed

if (process.argv.length === 0){
	console.log('No argument');
} else if (process.argv.length === 2){
	console.log('Agument found');
} else {
	console.log('Arguments found');
}
