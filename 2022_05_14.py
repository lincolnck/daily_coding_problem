# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a binary tree, return the level of the tree with minimum sum.
class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def depth_first_recursive(root, level, tree):
	if len(tree) == level:
		tree.append([])
	tree[level].append(root.data)
	if root.left is not None:
		depth_first_recursive(root.left, level+1, tree)
	if root.right is not None:
		depth_first_recursive(root.right, level+1, tree)

	return [sum(x) for x in tree].index(min([sum(x) for x in tree]))

if __name__ == '__main__':
	root = Node(1000)
	root.left = Node(10000)
	root.right = Node(100000)
	root.left.left = Node(16)
	root.left.right = Node(2)
	root.right.right = Node(122*10000)

	tree = []
	print(depth_first_recursive(root, 0, tree))
