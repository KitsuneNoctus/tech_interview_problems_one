# Technical Interview Problems
## Second Class Homework - April 1, 2020

### Easy Problems:

#### Problem 1
[Problem 1 Link](https://leetcode.com/problems/merge-two-sorted-lists/)

##### Problem: Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

> Example:

> Input: 1->2->4, 1->3->4
> Output: 1->1->2->3->4->4

1. Restate:
    - Merge two sorted linked lists and return a new list that is the two inputs spliced together in sorted order
2. Clarify:
    - Are there negative values in these lists?
    - Are then integers or another data type
3. Assumptions:
    - Assuming they're integers for simplicity sake
    - Size should not be a total factor
4. Think Out Loud:
    - Brainstorm Solution:
        * [Problem Solution](problem_one_easy.py)
        * Go through bother linked lists with a for loop and append the values to a new linked list
    - Explain Rationale:
        * Simple enough to execute
        * It has a low time complexity
    - Tradeoffs:
        * It has a lot of bulk and, being untested, means that it may not work.
    - Improvements:
        * Need some more code comments.
        * There must be an easier way to traverse two lists then the zip and for loop

#### Problem 2

##### Problem: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

> Example 1:

>Input: 121
>Output: true

>Example 2:

>Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

>Example 3:

>Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

>Follow up:

>Coud you solve it without converting the integer to a string?

1. Restate:
    - Return True or False on wether or not the **integer** given is a palindrome / can it be read the same way forwards and backward
2. Clarify:
    - Is there a size limit to the number?
    - Should I make it able to take in floats and doubles later?
    - Do you also want the reverse number returned?
    - Would you want to original number and reverse number shown, to prove the point?
    - Should a negative also flip where the negative symbol is?
3. Assumptions:
    - Based on the examples, the negative symbol will be flipped
    - Any size should be allowed
4. Think Out Loud:
    - Brainstorm Solution:
        * [Problem Solution](problem_two_easy.py)
        * Convert integer to to string, then create a new variable that takes that in reverse
        * Compare the two strings, if equal, then return true
    - Explain Rationale:
        * Easy to execute
        * It has a low time complexity
    - Tradeoffs:
        * None as far as I can tell.
        * It does require the use of strings, but I find thats okay
    - Improvements:
        * Most likely can be broken down to one line.



### Medium Problems: (Unfinished)

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
