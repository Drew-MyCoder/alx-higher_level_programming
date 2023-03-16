#!/usr/bin/node
/* Prints 3 lines as 1-multti_langs but
 * by using an array of string and loops
 */

const langs = 'C is fun';

if (isNaN(process.argv[1])){
	console.log('Missing number of occurences');
} else {
	for (let x = 0; x < parseInt(process.argv[1]); x ++){
		console.log(langs);
	}
}
