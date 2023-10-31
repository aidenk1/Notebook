---
toc: true
comments: false
layout: post
title: Algorithm Teaching Notes
description: Algorithm notes
type: hacks
courses: { compsci: {week: 7} }
---

## Description

This article covers various aspects of algorithms, including algorithm basics, pseudocode, string operations, palindromes, and more.

## Algorithm Basics

- **Sequence**: Follows a sequence of steps.
- **Selection**: Choose different outcomes based on a condition.
- **Iteration**: Repetition of code segments.

## Pseudocode

- A planning language/text conveying algorithm implementation.
- Sample College Board Pseudocode for strings.

## Robot MCQ (Algorithms)

- Develop a general algorithm for guiding a robot around a black rectangular box and back to the starting point.

## String Operations

- Length function for string.
- String concatenation.
- Substring function to extract a range of characters from a string.

# HOMEWORK:

## Palindrome Check
```python
string = input("Enter a word: ")

def palindrome(words):
    for i in words:
        if words[0] != words[len(words)-1]:
            return "It is not a palindrome"
    return "It is a palindrome"

print(palindrome(string))

names = ["Jedd", "Bob", "Dentobot", "Chris", "Kaiyu"]
sorted_names = sorted(names)

print("Names sorted in alphabetical order:")
for name in sorted_names:
    print(name)




