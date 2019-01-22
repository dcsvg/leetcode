# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.childs = []

class Solution(object):
    def invertTree(self, root):
        for i in root.childs:
            self.invertTree(i)
        root.childs.reverse()

if __name__ == "__main__":
    root = TreeNode(0)
    vsn1 = [2, 7, 12]
    vs1 = [ TreeNode(x) for x in vsn1]
    vsn2 = [1, 3, 11]
    vs2 = [TreeNode(x) for x in vsn2]
    vsn3 = [6, 9]
    vs3 = [TreeNode(x) for x in vsn3]
    root.childs = vs1
    root.childs[0].childs = vs2
    root.childs[1].childs = vs3

    solution = Solution()
    solution.invertTree(root)

    print(root)
