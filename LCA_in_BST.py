#  for Lowest Common Ancestor in BST

class Node:
    # The constructor to create a new binary search tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

	#  T = tree
	#  r = root
	#  n1 = node - left
	#  n2 = node - right


def L_C_A(T, r, n1, n2):
    if r < 1 or not isinstance(r, int):
        return TypeError("LCA value should be a non-negative integer")

    # If n1 and n2 are smaller than root, the LCA is the left child
    if r > n1 and r > n2:
        return n1

    # If n1 and n2 are greater than root, the LCA is the right child
    if r < n1 and r < n2:
        return n2
    # Otherwise returns root as the least common ancestor
    return r

print L_C_A([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)
# 3

print L_C_A([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 43578, 10, 4067772)
# 43578

print L_C_A([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], " ", 1, 3)
# LCA value should be integers

print L_C_A([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], "a", 1, 3)
# LCA value should be integers

print L_C_A(None, None, None, None)
# None
