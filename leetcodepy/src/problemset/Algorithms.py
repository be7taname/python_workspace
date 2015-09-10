'''
Created on Aug 30, 2015

@author: mianmianba
'''
import argparse

titleNum = 131;

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
elif titleNum == 120:
    from Triangle import MinimumTotal # Triangle, find the minimum path of sum
elif titleNum == 131:
    from PalindromePartitioning import PalindromePartitioning # Palindrome Partitioning, very Hard
    pp = PalindromePartitioning()
    print pp.solution("a")
elif titleNum == 134:
    from GasStation import CanCompleteCircuit # Gas Station, Hard
elif titleNum == 173: # Binary Search Tree Iterator, Interesting
    from common.TreeNode import TreeNode, genTree, genTreeNoVal
    from common.BSTIterator import BSTIterator
    root = genTree([3, 1, 2, 11, 5, 4, 7, 10, 14], [10, 8, 3, 7, 6, 1, 14, 4, 13])
    root.printTree()
    root.printTreeNodeVal()
    bstit, bstls = BSTIterator(root), []
    while bstit.hasNext(): bstls.append(bstit.next())
    print bstls
elif titleNum == 200:
    from NumberOfIslands import NumIslands # Number of Islands, Hard
elif titleNum == 274:
    from HIndex import HIndex # H-Index
else:
    print 'Do nothing'
    
