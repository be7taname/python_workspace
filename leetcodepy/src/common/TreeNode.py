'''
Created on Sep 6, 2015

@author: mianmianba
'''
class NodeLocation(object):
    def __init__(self, level=None, offset=None):
        self.level = level
        self.offset = offset
        
    def toIndex(self):
        return (1 << self.level) + self.offset

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x=-99):
        self.val = x
        self.left = None
        self.right = None
        
    def setIndex(self, index): self.index = index
        
    def insertNode(self, index):
        """
        :type index: int
        :rtype: TreeNode
        """
        loc = index2Location(index)
        prevLoc = NodeLocation(loc.level-1, loc.offset>>1)
        parentNode = self.obtainNode(prevLoc.toIndex());
        
        if parentNode == None: return None
        
        if (loc.offset & 1) == 0:
            parentNode.left = TreeNode()
            parentNode.left.setIndex(index)
            return parentNode.left
        else:
            parentNode.right = TreeNode()
            parentNode.right.setIndex(index)
            return parentNode.right
            
    def obtainNode(self, index):
        """
        :type index: int
        :rtype: TreeNode
        """
        tmp = self
        loc = index2Location(index)
        for i in range(loc.level-1, -1, -1):
            thisBit = (loc.offset >> i) & 1
            if thisBit == 0:
                tmp = tmp.left
            else:
                tmp = tmp.right
            if tmp == None: return None
        return tmp
        
    def compDepth(self):
        """
        :rtype: int
        """
        if self == None: return 0
        if self.left != None: 
            leftDepth = self.left.compDepth()
        else: 
            leftDepth = 0
        if self.right != None: 
            rightDepth = self.right.compDepth()
        else:
            rightDepth = 0
        return (rightDepth if rightDepth >= leftDepth else leftDepth) + 1
    
    def existNode(self, index):
        return (False if self.obtainNode(index) == None else True)
    
    def printTree(self):
        treeDepth = self.compDepth()
        for i in range(treeDepth):
            for j in range(1 << i):
                index = (1<<i) + j
                print '{0:5d}'.format(-1 if self.existNode(index) == False else index),
            print
            
    def printTreeNodeVal(self):
        treeDepth = self.compDepth()
        for i in range(treeDepth):
            for j in range(1 << i):
                index = (1<<i) + j
                thisNode = self.obtainNode(index)
                print '{0:5d}'.format(-99 if thisNode == None else thisNode.val),
            print
    
def index2Location(index):
    """
    :type index: int
    :rtype: NodeLocation
    """
    loc = NodeLocation()
    for level in range(1, 31):
        delimit = 1 << level
        if index < delimit:
            break
    loc.level = level - 1
    loc.offset = index - (1 << loc.level)
    return loc
        
def genTree(indexList, valueList):
    """
    :type indexList: List[int]
    :type valueList: List[int]
    :rtype: TreeNode 
    """
    root = TreeNode()
    root.setIndex(1)
    indices = sorted(range(len(indexList)), key=lambda k: indexList[k])
    
    if indexList[indices[0]] != 1: return None
    root.val = valueList[indices[0]]
    
    for i in range(1, len(indexList)):
        newNode = root.insertNode(indexList[indices[i]])
        newNode.val = valueList[indices[i]]
        
    return root

def genTreeNoVal(indexList):
    """
    :type indexList: List[int]
    :rtype: TreeNode 
    """
    root = TreeNode()
    root.setIndex(1)
    
    indexList.sort()
    if indexList[0] != 1: return None
    
    for i in range(1, len(indexList)):
        root.insertNode(indexList[i])
    
    return root    