import os
import sys
import string
import numpy as np

class Node:  # tree sturcture
    def __init__(self):
        self.num_children = 0
        self.children = []
        self.parent = None
        self.times = 0
        self.item = ''


def cal_Min_Sup(s, minSupp):
    file = open(s, mode='r', encoding='utf8')
    C1 = {}
    Real_line = 0
    for line in file:
        Real_line += 1
        for item in line.split(","):
            if item != "" and item != "\n":
                for i in item:
                    if i != "\n":
                        if i in C1:
                            C1[i] += 1
                        else:
                            C1[i] = 1
    minSupp1 = round(minSupp / 100 * Real_line)
    for key, value in C1.items():
        if int(value) < minSupp1:
            del C1[key]
    sorted_keys = sorted(C1, key=C1.get, reverse=True)
    d = {}
    for r in sorted_keys:
        d[r] = C1[r]
    return (d)


def Ordered_items(s, item_list):
    file = open(s, mode='r', encoding='utf8')
    output_file = open("Fp-Tree_Output.txt", "w+")
    for line in file:
        for key, value in item_list.items():
            for item in line:
                if key == item:
                    output_file.write(key + ",")
        output_file.write("\n")
    output_file.close()


def BuildTree(node, list, element):
    if (len(list) == 0):
        return
    for child in node.children:
        if (child.item == element):
            child.times += 1
            del list[0]
            if (len(list) == 0):
                return
            BuildTree(child, list, list[0])
            if (len(list) == 0):
                return
            break
    new_node = Node()
    node.num_children += 1
    new_node.item = element
    new_node.times += 1
    new_node.parent = node
    node.children.append(new_node)
    del list[0]
    if (len(list) == 0):
        return
    BuildTree(new_node, list, list[0])


def Draw_tree(node, prefix, isTail):
    if (isTail):
        temp = prefix + "└── " + node.item
    else:
        temp = prefix + "├── " + node.item
    print(temp)
    for n in range(0, len(node.children) - 1):
        if (isTail):
            Draw_tree(node.children[n], prefix + "    ", False)
        else:
            Draw_tree(node.children[n], prefix + "│   ", False)
    if (len(node.children) >= 1):
        if (isTail):
            prefix = prefix + "    "
        else:
            prefix = prefix + "│   "
        Draw_tree(node.children[-1], prefix, True)
#
# def Query(tree):  # main function of finding common buyers
#     temp = raw_input("Please input two items: ")
#     a = temp[0]
#     b = temp[1]
#     for element in sample_list:  # swap the sequence of user's input, make it fit the OFI sequence
#         if (element == a):
#             break
#         elif (element == b):
#             temp = a
#             a = b
#             b = temp
#             break
#     result = 0
#     A_list = []
#     B_list = []
#     FindA(tree, a, A_list)
#     for node in A_list:
#         FindB(node, b, B_list)
#     for node in B_list:
#         result += node.times
#     return result
#
# def FindA(node, a, list):
#     if (len(node.children) == 0):
#         return
#     if (node.item == a):
#         list.append(node)
#     else:
#         for child in node.children:
#             FindA(child, a, list)
#
# def FindB(node, b, list):
#     if (node.item == b):
#         list.append(node)
#     else:
#         for child in node.children:
#             FindB(child, b, list)
#         if (len(node.children) == 0):
#             return

if __name__ == "__main__":
    filename = input('Please enter file name: ')
    while True:
        try:
            minSupport = int(input('Please enter minimum support(%): '))
            break
        except ValueError:
            print('Min Support is a number!!!')
    dirname, tenfile = os.path.split(os.path.abspath(sys.argv[0]))
    s = os.path.join(dirname, filename)
    Item_List = []
    Item_List = cal_Min_Sup(s, minSupport)
    print("C1 = {0} {1} ".format(Item_List, Ordered_items(s, Item_List)))
    OFI_list = open("Fp-Tree_Output.txt", "r")
    root = Node()
    totalline = 0
    for line in OFI_list:
        print(line)
        totalline += 1
    i = totalline

    print("Your tree has been succefully built, shown as follow:  ")
    Draw_tree(root, "", True)
    fff = open('Fp-Tree_Output.txt')
    triplets=fff.read().split()
    for iii in range(0,len(triplets)):
        triplets[iii]=triplets[iii].split(',')
    print(triplets)
    print("Tree Building...... Wait please....")
    for n in triplets:
        BuildTree(root, n, n[0])