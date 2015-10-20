'''
Created on Aug 30, 2015

@author: mianmianba
'''
import argparse

titleNum = 47;

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
elif titleNum == 2:
    from AddTwoNumbers import AddTwoNumbers # Add Two Numbers
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
elif titleNum == 18:
    from FourSum import FourSum # 4sum, Hard, use hash table
elif titleNum == 29:
    from DivideTwoIntegers import Divide # Divide Two Integers
elif titleNum == 31:
    from NextPermutation import NextPermutation # Next Permutation, Hard, not that h.a.r.d
    np = NextPermutation()
    nums = [3, 2, 1]
    np.solution(nums)
    print nums
elif titleNum == 43:
    from MultiplyStrings import Multiply # Multiply Strings
elif titleNum == 46:
    from Permutations import Permute # Permutations
elif titleNum == 47:
    from PermutationsII import PermuteUnique # Permutations II
elif titleNum == 49:
    from GroupAnagrams import GroupAnagrams # Group Anagrams, Hard, Beautiful coding use dictionary
elif titleNum == 53:
    from MaximumSubarray import MaxSubArray # Maximum Subarray, Hard, for the best solution
    ms = MaxSubArray()
    print ms.solutions([-2, -1])
    print ms.solutions([-2,1,-3,4,-1,2,1,-5,4]), ms.solutions([1])
elif titleNum == 54:
    from SpiralMatrix import SpiralOrder # Spiral Matrix
elif titleNum == 60:
    from PermutationSequence import GetPermutation # Permutation Sequence
    gp = GetPermutation()
    print gp.solution(3, 3)
elif titleNum == 61:
    from RotateList import RotateRight # Rotate List
elif titleNum == 69:
    from SqrtOfX import MySqrt # Sqrt(x), Hard, binary search algorithm actually is better than Newton Algorithm
    ms = MySqrt()
    print ms.solution(120)
    print ms.solutionFast(120)
elif titleNum == 71:
    from SimplifyPath import SimplifyPath # Simplify Path, Implementation not efficient
    sp = SimplifyPath()
    print sp.solution('/.')
elif titleNum == 79:
    from WordSearch import Exist # word search
    ew = Exist()
    print ew.solution([["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]], "ABCB")
elif titleNum == 82:
    from RemoveDuplicatesFromSortedListII import DeleteDuplicates # Remove Duplicates from Sorted List II
elif titleNum == 91:
    from DecodeWays import NumDecodings
    nds = NumDecodings()
    s = '12006'
    print nds.solutionDP(s) # Decode Ways, Hard, Dynamic Programming
    print nds.solutionDPOnline(s)
elif titleNum == 93:
    from RestoreIpAddresses import RestoreIpAddresses # Restore IP Addresses
elif titleNum == 98:
    from common.TreeNode import TreeNode, genTree # Valid Binary Search Tree
    from ValidateBST import IsValidBST
    ivb = IsValidBST()
    root = genTree([1, 2, 3, 4, 5, 6, 7], [3, 1, 5, 0, 2, 4, 6])
    print ivb.solutions(root)
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
elif titleNum == 127:
    from WordLadder import LadderLength # Word Ladder, Hard, Very, Smart/Fast way to find words with 1 bit flip
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
elif titleNum == 133:
    from CloneGraph import CloneGraph # Clone Graph, Hard, BFS combining with hash map
elif titleNum == 134:
    from GasStation import CanCompleteCircuit # Gas Station, Hard
elif titleNum == 136:
    from SingleNumber import SingleNumber # Single Number
elif titleNum == 139:
    from WordBreak import WordBreak # Word Break, Hard, Dynamic Programming
elif titleNum == 143:
    from common.ListNode import ListNode
    from ReorderList import ReorderList # Reorder List
    rl = ReorderList()
    ln = ListNode(1); ln.next = ListNode(2); ln.next.next = ListNode(3); ln.next.next.next = ListNode(4)
    rl.solution(ln)
    while ln:
        print ln.val
        ln = ln.next
elif titleNum == 148:
    from common.ListNode import ListNode # Sort List, Hard, Merge Sort, Probably not good implementation
    from SortList import SortList
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(4)
    sl = SortList()
    newhead = sl.solution(head)
    while newhead:
        print newhead.val
        newhead = newhead.next
elif titleNum == 150:
    from EvaluateReversePolishNotation import EvalRPN # Evaluate Reverse Polish Notation
    erpn = EvalRPN()
    print erpn.solution(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
elif titleNum == 151:
    from ReverseWordsInString import ReverseWords # Reverse Words In a String, Hard, use function join&split
    rw = ReverseWords()
    print rw.solution("   a   b ")
elif titleNum == 152:
    from MaxProdSubarray import MaxProduct # Maximum Product Subarray, Dynamic Programming
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
elif titleNum == 187:
    from RepeatedDnaSequences import FindRepeatedDnaSequences # Repeated DNA Sequences, Hard, usage of dict data structure
elif titleNum == 199:
    from BinaryTreeRightSideView import RightSideView # Binary Tree Right Side view
elif titleNum == 200:
    from NumberOfIslands import NumIslands # Number of Islands, Hard
elif titleNum == 207:
    from CourseSchedule import CanFinish # Course Schedule, Hard, check Course Schedule II
    cf = CanFinish()
    print cf.solutions(2, [[1, 0]])
elif titleNum == 208:
    from common.ImplementTrie import Trie, TrieNode # Implement Trie, Hard, New Concept
elif titleNum == 209:
    from MinimumSizeSubarraySum import MinSubArrayLen
    msal = MinSubArrayLen() # Minimum Size Subarray Sum, Hard, another way is to use binary search
    print msal.solution(11, [1, 2, 3, 4, 5])
elif titleNum == 210:
    from CourseScheduleII import FindOrder # Course Schedule II, Hard, Topological Order
elif titleNum == 211:
    from common.AddAndSearchWord import WordDictionary # Add and Search Word, Hard, New way to implement Trie
elif titleNum == 220:
    from ContainsDuplicateIII import ContainsNearbyAlmostDuplicate # Contains Duplicate III, Hard, Very
    cnad = ContainsNearbyAlmostDuplicate()
    nums = [0,10,22,15,0,5,22,12,1,5]
    k = 3
    t = 3
    print cnad.solutionDict(nums, k, t)
    print cnad.solution(nums, k, t)
elif titleNum == 221:
    from MaximalSquare import MaximalSquare # Maximal Square, Dynamic programming, Nice work
elif titleNum == 222:
    from common.TreeNode import TreeNode, genTreeNoVal
    from CountCompleteTreeNodes import CountNodes # Count Complete Tree Nodes, Hard, Efficient Solution
    cn = CountNodes()
    root = genTreeNoVal([1, 2, 3, 4])
    print cn.solutionTwo(root)
elif titleNum == 224:
    from BasicCalculator import Calculate # Basic Calculator, Hard, Very
    bc = Calculate()
    print bc.solutionStack("1-1")
elif titleNum == 227: # Basic Calculator II, Hard, Implementation not efficient
    from BasicCalculatorII import Calculate
    bc2 = Calculate()
    print bc2.solution('0-0')
elif titleNum == 229:
    from MajorityElementII import MajorityElementII # Majority Element II, Hard, Moore's algorithm variation
    me2 = MajorityElementII()
    print me2.solution([8, 8, 7, 7, 7])
elif titleNum == 233:
    from NumberToDigitalOne import CountDigitOne # Number of Digit One, Hard, tricky
elif titleNum == 263:
    from UglyNumber import IsUgly # Ugly Number
elif titleNum == 264:
    from UglyNumberII import NthUglyNumber # Ugly Number II, Hard, Smart way to do it
    nun = NthUglyNumber()
    print nun.solution(7)
elif titleNum == 273:
    from IntegerToEnglishWords import NumberToWords # Integer To English Words
elif titleNum == 274:
    from HIndex import HIndex # H-Index
else:
    print 'Do nothing'
    
