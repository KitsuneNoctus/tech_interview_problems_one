''' Problem: Given a string containing digits from 2-9 inclusive, return all
possible letter combinations that the number could represent. A mapping of
digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters. '''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        phone_pad = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m''n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        combinations = []

        if digits:
            for digit in digits

        # def create_map():
        #     for digit in digits:
        #
        #     pass

        # if digits:
        #     create_map()
        return combinations

def main():
    pass

if __name__ == '__main__':
    main()
