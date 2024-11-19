# 199. Binary Tree Right Side View
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    
    res = []
    queue = deque()
    queue.append(root)

    while queue:
        nodeCount = len(queue)
        val = 0

        for i in range(nodeCount):
            node = queue.popleft()
            val = node.val

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        res.append(val)

    return res

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    
    res = []
    queue = deque()
    queue.append(root)

    while queue:
        nodeCount = len(queue)
        curLevel = []

        for i in range(nodeCount):
            node = queue.popleft()
            curLevel.append(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        res.append(curLevel[-1])

    return res