# -*- coding: utf-8 -*-
"""
# @file name  : Python_BinaryTree.py
# @author     : Ares
# @date       : 2020-07-19
# @brief      : Pythonic way to create a Binarytree
"""
class Node(object):
    def __init__(self,item):
        '''
        We should first create a node element
        and 'self' is the 'node'
        node has the attribution 'item' 'left' right
        :param item: the element to be a node
        '''
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item) # only need this

class Tree(object):
    def __init__(self):
        '''
        only use the root to be the sentienl
        '''
        self.root = Node('root')

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node # 二叉树为空，则作者为根节点
        else:
            q = [self.root] # 最终以列表形式实现
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = None
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self,item):
        '''
        :param item:
        :return: parent_node_list
        '''
        if self.root.item == item:
            return None # 根节点没有父节点
        temp = [self.root]
        while temp:
            # 不断pop直到空的思想，一直贯穿整个数据结构
            pop_node = temp.pop(0)
            if pop_node.left and pop_node.left.item == item:
                return pop_node
            if pop_node.right and pop_node.right.item == item:
                return pop_node
            if pop_node.left is not None:
                temp.append(pop_node.left)
            if pop_node.right is not None:
                temp.append(pop_node.right)
        return None

    def delete(self,item):
        if self.root is None:
            return False
        parent_node = self.get_parent(item)
        if parent_node:
            del_node = parent_node.left if parent_node.left.item == item else parent_node.right
            if del_node.left is None:
                if parent_node.left.item == item:
                    parent_node.left = del_node.right
                else:
                    parent_node.right = del_node.right
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent_node.left.item == item:
                    parent_node.left = tmp_next
                else:
                    parent_node.right = tmp_next
                del del_node
                return True
        else:
            return False

