class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._get_node(word)
        return node is not None and node.is_end
    
    def _get_node(self, word):
        node = self.root
        for char in word:
            if not char in node.children:
                return None
            node = node.children[char]
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

        for current_node, char in reversed(stack):
            if not current_node.children[char].children and not current_node.children[char].is_end:
                del current_node.children[char]
            else:
                break

    

trie = Trie()

trie.insert("Oracle")
trie.insert("Orange")

trie.delete("Orange")

print(trie.search("Orange"))