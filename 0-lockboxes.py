#!/usr/bin/python3
"""
This module contains a function to check if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Args:
        boxes (list of lists): List where each box contains keys to other boxes.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked.
    
    keys = boxes[0]  # Start with keys from the first box.

    for key in keys:
        if key < len(boxes) and not unlocked[key]:
            unlocked[key] = True
            keys.extend(boxes[key])  # Add keys from the newly unlocked box.

    # Check if all boxes have been unlocked
    for i in range(len(boxes)):
        if not unlocked[i]:
            return False

    return True

