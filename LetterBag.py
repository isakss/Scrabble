from Letter import Letter
from Bag import Bag
from random import Random

class LetterBag:
    def __init__(self):
        self.letters = [] # To keep track on how many letters are left
        self.root = None
        for i in range(65,91):
            self.letters.append(chr(i))
        self.empty = False
        self.populate_bag()
        
    def populate_bag(self):
        """Gets the letters from Bag as (letter,points,amount) then populates the tree and tries to get good spread by placing the middle first and then random"""
        the_bag = Bag().get_bag()
        the_current_value = the_bag.pop(len(self.letters)//2)
        self.insert(the_current_value)
        highest_index = len(the_bag) - 1

        for i in range(0,len(the_bag)):
            random_number = Random().randint(0,highest_index)
            the_current_value = the_bag.pop(random_number)
            self.insert(the_current_value)
            highest_index -= 1

    def insert(self, key):
        """Makes a letter case and puts it in the tree"""
        if self.root == None:
            self.root = Letter(key[0], key[1], key[2])
            return

        new_node = self._find_node_rec(key[0], self.root)

        if new_node.key == key[0]:
            return
        else:
            if new_node.key < key[0]:
                new_node.right = Letter(key[0], key[1], key[2])
            else:
                new_node.left = Letter(key[0], key[1], key[2])
    
    def _find_node_rec(self, key, node):
        """Either returns the node or the parent node where that key should be under"""
        if key > node.key and node.right != None:
            return self._find_node_rec(key, node.right)
        elif key < node.key and node.left != None:
            return self._find_node_rec(key, node.left)
        else:
            return node

    def draw_letters(self, amount):
        ret_list = []
        while amount != 0:
            random = Random().randint(0,len(self.letters)-1)
            the_letter = self._find_node_rec(self.letters[random], self.root)
            ret_list.append(the_letter)
            the_letter.amount -= 1
            amount -= 1
            
            if the_letter.amount == 0:
                self.letters.remove(the_letter.key)
                self.remove(the_letter)
                if len(self.letters) == 0:
                    print("The bag is empty")
                    self.empty = True

        return ret_list

    def swap_letters(self, letters):
        swap_amount = len(letters)

        for i in letters:
            if i.amount == 0: # If the letter was removed from the tree
                self.insert_back(i)
            
            i.amount += 1

        ret_lis = self.draw_letters(swap_amount)
        return ret_lis

    def insert_back(self, letter_class):
        """Works like insert but just expects the letter class instead of a tuple"""
        if self.root == None:
            self.root = letter_class
            return

        new_node = self._find_node_rec(letter_class.key, self.root)

        if new_node.key == letter_class.key:
            return
        else:
            if new_node.key < letter_class.key:
                new_node.right = letter_class
            else:
                new_node.left = letter_class
    
    def remove(self, node):
        if node.left != None and node.right != None:
            replacement_node = self._find_right_most_of_left(node.left)
            parent_node = self._get_parent_node(self.root, replacement_node)
            self._remove_helper(parent_node, replacement_node)

            parent_node = self._get_parent_node(self.root, node)

            if parent_node != None:
                if parent_node.left == node:
                    parent_node.left = replacement_node
                else:
                    parent_node.right = replacement_node
            else:
                self.root = replacement_node

            replacement_node.left = node.left
            replacement_node.right = node.right
        else:
            parent_node = self._get_parent_node(self.root, node)
            self._remove_helper(parent_node, node)

    def _remove_helper(self, parent, child):
        if parent == None:
            if child.left == None and child.right == None:
                self.root = None
            else:
                if child.left == None:
                    self.root = child.right
                else:
                    self.root = child.left
            return

        if parent.left == child:
            if child.left == None:
                parent.left = child.right
            else:
                parent.left = child.left
        else:
            if child.left == None:
                parent.right = child.right
            else:
                parent.right = child.left

    def _find_right_most_of_left(self, the_node):
        if the_node.right == None:
            return the_node
        else:
            return self._find_right_most_of_left(the_node.right)
    
    def _get_parent_node(self, current_node, target_node):
        if current_node.key == target_node.key:
            return None
        
        if current_node.key > target_node.key:
            if current_node.left.key == target_node.key:
                return current_node
            else:
                return self._get_parent_node(current_node.left, target_node)
        else:
            if current_node.right.key == target_node.key:
                return current_node
            else:
                return self._get_parent_node(current_node.right, target_node)

    def _remove_none_or_one_child(self, current_node, target_node):
        if current_node.key == target_node.key:
            if target_node.left == None and target_node.right == None:
                self.root = None
            else:
                if target_node.left == None:
                    self.root = target_node.right
                else:
                    self.root = target_node.left
            return
        
        if current_node.key > target_node.key:
            if current_node.left.key == target_node.key:
                if target_node.left == None:
                    current_node.left = target_node.right
                else:
                    current_node.left = target_node.left
            else:
                self._remove_none_or_one_child(current_node.left, target_node)
        else:
            if current_node.right.key == target_node.key:
                if target_node.left == None:
                    current_node.right = target_node.right
                else:
                    current_node.right = target_node.left
            else:
                self._remove_none_or_one_child(current_node.right, target_node)