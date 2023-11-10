class Node(objects):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
    
class Trie:
    def __init__(self):
        self.head = None(None)
        
    def insert(self, string):
        current_node = self.head
        
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string        
    
    def search(self, string):
        current_node = self.head
        
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        
        if current_node.data:
            return True
        else:
            return False
        
    def starts_with(self, prefix):
        current_node = self.head
        words = []
        
        for p in prefix:
            