from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
class TrieNode(): 
    def __init__(self): 
        self.children = {} 
        self.is_word = False
  
class Trie(): 
    def __init__(self): 
        self.root = TrieNode() 
  
    def formTrie(self, keys): 
        for key in keys: 
            self.insert(key)
  
    def insert(self, key): 
        node = self.root 
  
        for a in list(key): 
            if not node.children.get(a): 
                node.children[a] = TrieNode() 
  
            node = node.children[a] 
  
        node.is_word = True
  
    def find(self, key): 
        node = self.root 
        found = True
  
        for a in list(key): 
            if not node.children.get(a): 
                found = False
                break
  
            node = node.children[a] 
  
        return node and node.is_word and found 
  
    def suggestionsRec(self, node, word,llist):
        if node.is_word:
             llist.append(word)
        for a,n in node.children.items(): 
            self.suggestionsRec(n, word + a,llist) 
        return llist
    def suffixes(self, key): 
        node = self.root 
        not_found = False
        temp_word = '' 
        llist=[]
        for a in list(key): 
            if not node.children.get(a): 
                not_found = True
                break
            node = node.children[a]
        if not_found: 
            return 0
        llist=self.suggestionsRec(node, temp_word,llist)
        return llist
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.suffixes(prefix)
        if prefixNode:
            print('\n'.join(prefixNode))
        else:
            print(prefix + " not found")
    else:
        print('')
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
interact(f,prefix='');
