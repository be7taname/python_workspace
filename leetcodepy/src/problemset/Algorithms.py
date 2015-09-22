'''
Created on Aug 30, 2015

@author: mianmianba
'''
import argparse

titleNum = 179;

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--title_num', type = int, help = 'the title number of the problem of LeetCode',
                        default = 1)
    args = parser.parse_args()
    print "title number given by argument is {}".format(args.title_num)
    titleNum = args.title_num

print "module name is {}".format(__name__)
print "title number to be used is {}".format(titleNum)

if titleNum == 1:
    from TwoSum import TwoSum # Two Sum, Hard
    ts = TwoSum()
    print ts.solution([2, 7, 11, 15], 9)
elif titleNum == 3:
    from LongestSubStringNoRep import LengthOfLongestSubstring
    lols = LengthOfLongestSubstring()
    print lols.solution('c')
elif titleNum == 5:
    from LongestPalindromicSubstring import LongestPalindrome
    lp = LongestPalindrome() # Longest Palindromic Substring, 
    print lp.solutionRecursive('bb') # recursive solution is good, but there is better one, Hard
elif titleNum == 11:
    from MaxArea import MaxArea # Container With Most Water, Hard
elif titleNum == 15:
    from ThreeSum import ThreeSum # 3Sum, Hard
    thsu = ThreeSum()
    print thsu.solution([0, 0, 0])
elif titleNum == 29:
    from DivideTwoIntegers import Divide # Divide Two Integers
elif titleNum == 53:
    from MaximumSubarray import MaxSubArray # Maximum Subarray, Hard, for the best solution
    ms = MaxSubArray()
    print ms.solutions([-2, -1])
    print ms.solutions([-2,1,-3,4,-1,2,1,-5,4]), ms.solutions([1])
elif titleNum == 91:
    from DecodeWays import NumDecodings
    nds = NumDecodings()
    s = '12006'
    print nds.solutionDP(s) # Decode Ways, Hard, Dynamic Programming
    print nds.solutionDPOnline(s)
elif titleNum == 108:
    from SortedArrayToBST import SortedArrayToBST
elif titleNum == 109:
    from common.ListNode import ListNode
    from common.TreeNode import TreeNode
    from SortedListToBST import SortedListToBST # Convert sorted List to BST, Hard
    ln = ListNode(1)
    ln.next = ListNode(3)
    sltb = SortedListToBST()
    root = sltb.solution(ln)
    root.printTreeNodeVal()
elif titleNum == 120:
    from Triangle import MinimumTotal # Triangle, find the minimum path of sum
elif titleNum == 121:
    from BestTimeBuySellStock import MaxProfit # best time to buy and sell stock
elif titleNum == 130:
    from SurroundedRegions import FlipSurroundedRegions # Surrounded Regions, Hard, BFS loop vs. DFS recursive
    fsr = FlipSurroundedRegions()
    board = [['X','X','X','X'], ['X','O','O','X'], ['X','X','O','X'], ['X','O','X','X']]
    fsr.solutionBFS(board)
    print board
elif titleNum == 131:
    from PalindromePartitioning import PalindromePartitioning # Palindrome Partitioning, very Hard
    pp = PalindromePartitioning()
    print pp.solution("a")
elif titleNum == 134:
    from GasStation import CanCompleteCircuit # Gas Station, Hard
elif titleNum == 136:
    from SingleNumber import SingleNumber # Single Number
elif titleNum == 151:
    from ReverseWordsInString import ReverseWords # Reverse Words In a String, Hard, use function join&split
    rw = ReverseWords()
    print rw.solution("   a   b ")
elif titleNum == 166:
    from Fraction2RecurringDecimal import FractionToDecimal # Fraction to Recurring Decimal, Hard
    ftd = FractionToDecimal()
    print ftd.solution(1, 5)
elif titleNum == 173: # Binary Search Tree Iterator, Interesting
    from common.TreeNode import TreeNode, genTree, genTreeNoVal
    from common.BSTIterator import BSTIterator
    root = genTree([3, 1, 2, 11, 5, 4, 7, 10, 14], [10, 8, 3, 7, 6, 1, 14, 4, 13])
    root.printTree()
    root.printTreeNodeVal()
    bstit, bstls = BSTIterator(root), []
    while bstit.hasNext(): bstls.append(bstit.next())
    print bstls
elif titleNum == 179:
    from LargestNumber import LargestNumber # Largest Number, Hard, Use customized compare function for sorting
elif titleNum == 199:
    from BinaryTreeRightSideView import RightSideView # Binary Tree Right Side view
elif titleNum == 200:
    from NumberOfIslands import NumIslands # Number of Islands, Hard
elif titleNum == 224:
    from BasicCalculator import Calculate # Basic Calculator, Hard, Very
    bc = Calculate()
    print bc.solutionStack("1-1")
elif titleNum == 273:
    from IntegerToEnglishWords import NumberToWords # Integer To English Words
elif titleNum == 274:
    from HIndex import HIndex # H-Index
else:
    print 'Do nothing'
    
