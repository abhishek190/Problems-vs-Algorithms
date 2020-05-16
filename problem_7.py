# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root=RouteTrieNode("root handler")
    def insert(self,llist,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current=self.root
        for word in llist[:-1]:
            if word not in current.children:
                current.children[word]=RouteTrieNode("not found handler")
            current=current.children[word]
        word=llist[-1]
        current.children[word]=RouteTrieNode(handler)
    def find(self,route):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current=self.root
        for word in route:
            if word =='':
                return current.root_handler
            if word not in current.children:
                return "not found handler"
            else:
                current=current.children[word]
        return current.root_handler
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,root_handler):
        # Initialize the node with children as before, plus a handler
        self.children={}
        self.root_handler=root_handler
    def insert(self ):
        # Insert the node as before
        pass
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root=RouteTrie(handler)
    def add_handler(self, route,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        llist=self.split_path(route)
        current_node=self.root
        current_node.insert(llist,handler)
    def lookup(self,route ):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
       
        llist=self.split_path(route)
        return self.root.find(llist)
    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        llist=[]
        route=route.rstrip('/')
        word=""
        for ch in route[1:]:
          x=ord(ch)
          if x!=47:
              word+=ch
              continue
          else:
              llist.append(word)
              word=""
        llist.append(word)
        return llist
        
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/portfolio","about portfolio")
router.add_handler("/home/login/me","Welcome To Udacity")
# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/portfolio"))#should print 'about portfolio'
print(router.lookup("home/login/"))#shoud print 'not found handler'
print(router.lookup("/home/login/me"))#shoud print 'Welcome To Udacity'
