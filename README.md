# Technical Interview Problems
## Second Class Homework - April 1, 2020

#### Problem 1
[Problem 1 Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

##### Problem: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

[Image](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

1. Restate:
    - Return all possible letter combinations that a number string with digits inclusive from 2-9, could represent
2. Clarify:
    - Is there a maximum size to the letter combinations?
    - Does the mapping of letters need to be in a particular order?
    - Should mapping be done in order of the string of numbers?
    - What should one do with repeating numbers?
3. Assumptions:
    - There is potential for repeating numbers to occur like in real life with texting
    - Size should not be a total factor
4. Think Out Loud:
    - Brainstorm Solution:
        * [Problem Solution](problem_one.py)
    - Explain Rationale:
        * Simple Enough ...
    - Tradeoffs:
        * Filling ...
    - Improvements:
        * Filling ...

#### Problem 2
[Problem 2 Link](https://leetcode.com/problems/add-two-numbers/)

##### Problem: You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

> Output: 7 -> 0 -> 8

> Explanation: 342 + 465 = 807.


1. Restate:
    - When given two linked lists that have have values within that represent non-negative numbers, return their total. The numbers are stored in reverse order, and each node of the linked list is a single digit of the number. Add the numbers and return it as a linked list. No numbers contain leading zero.
2. Clarify:
    - Can the numbers be of different sizes?
    - Is the output to be the number as a whole, or is it to be the totals of the individual numbers
3. Assumptions:
    - The output should be individual numbers as it looks to be in the output example
    - Numbers should be allowed to differ in sizes in edge cases, but on the general occasion, it would be safe to assume that the two numbers / linked lists are of same length.
4. Think Out Loud:
    - Brainstorm Solution:
        * [Problem Solution](problem_two.py)
    - Explain Rationale:
        * Filling ...
    - Tradeoffs:
        * Filling ...
    - Improvements:
        * Filling ...
