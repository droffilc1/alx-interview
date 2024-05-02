#!/usr/bin/python3
""" 0-lockboxes """


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened
    Returns True if all boxes can be opened, else return False
    """
    # Number of boxes
    n = len(boxes)

    # Initialize a set with the first box, that's always unlocked
    unlocked_box = {}

    for index, box in enumerate(boxes):
        if len(box) == 0 or index == 0:
            unlocked_box[index] = index
        for key in box:
            if key < len(boxes) and key != index:
                unlocked_box[key] = key
    return len(unlocked_box) == n
