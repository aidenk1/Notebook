---
toc: true
comments: false
layout: post
title: Algorithm Notes
description: alg Notes
type: hacks
courses: { compsci: {week: 9} }
---
# Developing Algorithms

## How to do simple operators in JS

### Use the “+” operator to add two numbers in JavaScript

### Use the “-“ operator to subtract two numbers in JavaScript

### Use the “*” operator to multiply two numbers in JavaScript

### Use the “/” operator to divide two numbers in JavaScript

### Use the “%” operator to get the remainder of a division operation in JavaScript

## Iterating

Iteration is going through a set of laws or objectives for the loops to complete. This allows for the desired objective to be completed.

## Randomization

Randomization is used to generate a random number. For example, RANDOM(a,b) would generate any number from a to b. Each result from randomization is equally likely to occur. Each execution might produce a different result.

## How to find the mean in JS
```javascript
// Define an array
var arry = [4, 62, 3, 38];

// Define a function to calculate the mean using an inputted array
function calculateAverageOfArray(array) {
    var total = 0;
    var count = 0;

    // Add all the values of the array
    jQuery.each(arry, function(index, value) {
        total += value;
        count++;
    });

    // Take the sum of the array and divide it by the length of the array
    return total / count;
}

console.log("The average of your list is " + calculateAverageOfArray(arry));
