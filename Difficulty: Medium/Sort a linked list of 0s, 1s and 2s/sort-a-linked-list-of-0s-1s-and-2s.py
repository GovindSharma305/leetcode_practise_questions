'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        # Create three dummy nodes to start three separate lists
        zeroD = Node(0)   # Dummy node for 0s list
        oneD = Node(1)    # Dummy node for 1s list  
        twoD = Node(2)    # Dummy node for 2s list

        # Initialize pointers to track the end of each list
        zero = zeroD      # Current end of 0s list
        one = oneD        # Current end of 1s list
        two = twoD        # Current end of 2s list

        curr_node = head  # Pointer to traverse original list
        
        # Traverse the original list and distribute nodes
        while curr_node:
            # Check current node's value and add to appropriate list
            if curr_node.data == 0:
                zero.next = curr_node  # Add to 0s list
                zero = zero.next       # Move 0s list pointer
            elif curr_node.data == 1:
                one.next = curr_node   # Add to 1s list
                one = one.next         # Move 1s list pointer
            else:
                two.next = curr_node   # Add to 2s list
                two = two.next         # Move 2s list pointer
            curr_node = curr_node.next

        # Connect the three lists: 0s -> 1s -> 2s
        if oneD.next:
            zero.next = oneD.next      # Connect 0s to 1s if 1s exist
        else:
            zero.next = twoD.next      # Connect 0s to 2s if no 1s exist
        
        one.next = twoD.next           # Connect 1s to 2s
        two.next = None                # End the final list

        return zeroD.next              # Return head of sorted list (skip dummy)