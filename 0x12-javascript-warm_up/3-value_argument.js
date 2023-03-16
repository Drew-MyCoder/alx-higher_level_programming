#!/usr/bin/node
//output the first argument that is passed

if (process.argv[1] === undefined){
	console.log('No argument');
} else {
	console.log(process.argv[1]);
