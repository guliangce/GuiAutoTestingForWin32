#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
对两个图片进行对比
"""

from PIL import Image,ImageFile
import imagehash

MAX_DIF=10

def getImageFile(index):
    global imageName
    imagePath=index
    image=Image.open(imagePath)
    return image


# 根据截屏截取的图片和本地的图片hash对比判定两张图片是否一致
def compare_image_with_hash(image_file1, image_file2, max_dif=0):
    """
    max_dif: 允许最大hash差值, 越小越精确,最小为0
    """
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    hash_1 = None
    hash_2 = None
    hash_1 = imagehash.average_hash(image_file1)
    # print(hash_1)
    hash_2 = imagehash.average_hash(image_file2)
    # print(hash_2)
    dif = hash_1 - hash_2
    print("差值 %d" % (dif))
    if dif < 0:
        dif = -dif
    if dif <= max_dif:
        return True
    else:
        return False


def CompareImage(image_file1, image_file2):
    isEqual = compare_image_with_hash(image_file1, image_file2, MAX_DIF)
    return isEqual

