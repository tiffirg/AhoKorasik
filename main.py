class Node:
    def __init__(self):
        self.children = {}
        self.output = []
        self.fail = None

class AhoCorasick:
    def __init__(self):
        self.trie = Node()

    def __build(self, pattern):
        for keyword in pattern:
            node = self.trie
            for char in keyword:
                node = node.children.setdefault(char, Node())
            node.output.append(keyword)

        queue = []
        for node in self.trie.children.values():
            queue.append(node)
            node.fail = self.trie

        while queue:
            current_node = queue.pop(0)
            for key, next_node in current_node.children.items():
                queue.append(next_node)
                fail_node = current_node.fail
                while fail_node and key not in fail_node.children:
                    fail_node = fail_node.fail
                if fail_node:
                    next_node.fail = fail_node.children[key]
                else:
                    next_node.fail = self.trie
                next_node.output += next_node.fail.output
                

    def search(self, text, patterns):

        root = self.__build(patterns)
        result = {pattern: [] for pattern in patterns}

        current_node = self.trie
        for i, char in enumerate(text):
            while current_node and char not in current_node.children:
                current_node = current_node.fail
            if not current_node:
                current_node = root
                continue
            current_node = current_node.children[char]
            for keyword in current_node.output:
                result[keyword].append(i - len(keyword) + 1)

        return result
    

