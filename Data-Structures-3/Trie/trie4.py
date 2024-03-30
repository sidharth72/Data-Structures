import pickle

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root= TrieNode()

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

    def autocomplete(self, prefix):
        results = []
        node = self._get_node(prefix)

        if node:
            self._collect_words(node, prefix, results)

        return results
    
    def _collect_words(self, node, current_prefix, results):
        if node.is_end: # If the end of the node, append until
            results.append(current_prefix)

        for char, child_node in node.children.items():
            self._collect_words(child_node, current_prefix + char, results)




# with open('words.txt', 'r') as file:
#     words = file.readlines()


# words = [line.rstrip('\n') for line in words]

# for word in words:
#     trie.insert(word)


# with open('trie.pkl', 'wb') as pickle_file:
#     pickle.dump(trie, pickle_file)

with open('trie.pkl', 'rb') as pickle_file:
    loaded_trie = pickle.load(pickle_file)

loaded_trie.insert("This is really amazing")

# print(trie.autocomplete("Zui"))

while True:
    prefix = input("Enter the Prefix:")
    if prefix == "q":
        break
    words_matched = loaded_trie.autocomplete(prefix)
    for matched in words_matched:
        print(matched)