class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root # Initializing Node
        for c in word:
            if c not in node.children:
                # iF the current character is not in the children
                # Create new TrieNode from there and insert value
                node.children[c] = TrieNode()
            # Iterate over each node one by one
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        node = self._get_node(word)
        return node is not None and node.is_end

    def _get_node(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
    

    def delete(self, word):
        if not self.search(word):
            return
        
        node = self.root
        stack = []

        for char in word:
            stack.append((node, char))
            node = node.children[char]

        node.is_end = False
        for curr_node, char in reversed(stack):
            if not curr_node.children[char].children and not curr_node.children[char].is_end:
                del curr_node.children[char]
            else:
                break


trie = Trie()

trie.insert("Orange")
trie.insert("Oracle")

# #print(trie.root.children['O'].children['r'].children['a'].children)

trie.delete("Oracle")







