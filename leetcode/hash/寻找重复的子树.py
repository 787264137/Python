class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def hierarchicalTraversal(root,ans):
            if not root:
                return '#'
            seq = str(root.val) + hierarchicalTraversal(root.left,ans)+hierarchicalTraversal(root.right,ans)
            if seq not in hashmap:
                hashmap[seq] = root
            else:
                ans.add(hashmap[seq])
            return seq

        hashmap = {}
        ans = set()
        hierarchicalTraversal(root,ans)
        return list(ans)

