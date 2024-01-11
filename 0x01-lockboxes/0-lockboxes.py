#!/usr/bin/python3
"""Lockboxess solution file"""


def addKeys(box, keyArr, totalBox):
    """Add a key to an array"""
    for key in box:
        if key < totalBox and key not in keyArr and key > 0:
            keyArr.append(key)
    return keyArr


def canUnlockAll(boxes):
    """Lockboxes funcion"""
    count = 0
    boxLen = len(boxes)
    keys = []
    keys = addKeys(boxes[0], keys, boxLen)
    index = 0
    while index < len(keys):
        keys = addKeys(boxes[keys[index]], keys, boxLen)
        index += 1
    if len(keys) == boxLen - 1:
        return True
    else:
        return False
