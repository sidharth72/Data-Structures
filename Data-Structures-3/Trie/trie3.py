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
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    

    def remove(self, word):
        if word not in self.search(word):
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

    def autocomplete(self, prefix):
        results = []
        node = self._get_node(prefix)

        if node:
            self._collect_words(node, prefix, results)

        return results
    
    def _collect_words(self, node, current_prefix, results):
        if node.is_end:
            results.append(current_prefix)

        for char, child_node in node.children.items():
            self._collect_words(child_node, current_prefix + char, results)


trie = Trie()

words = ["apple", "app", "apricot", "banana", "bat"]

for word in words:
    trie.insert(word)

prefix = "ba"

autocomplete_results = trie.autocomplete(prefix)

for autocomplete_result in autocomplete_results:
    print(autocomplete_result)
