# Problem

"""

Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de
and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

Asked by: Twitter

"""


# Code Section

class Node:

    def __init__(self, letter=None, is_end_of_word: bool = False):
        self.letter = letter
        self.children = []
        self.is_end_of_word = is_end_of_word

    def add_child(self, child):
        self.children.append(child)


# Utility function to find an element that satisfies a condition
def find_element(input_list: list, condition_fn):
    for element in input_list:
        if condition_fn(element):
            return element

    return None


# Utility method to build a Trie from a set of words
def construct_trie(words: list) -> Node:
    root_node = Node()

    for word in words:

        # For every new word, we add to the root
        current_node = root_node

        for letter in word:

            # Checking if we already have a node with this letter
            if letter not in [child.letter for child in current_node.children]:

                # Create the node
                new_node = Node(letter)

                # Attach it to the current
                current_node.add_child(new_node)

            # Move to the new node
            current_node = find_element(current_node.children, lambda node: node.letter == letter)

        # Mark this word as complete
        current_node.is_end_of_word = True

    return root_node


# Utility method to get the Inorder of a tree
def inorder_to_list(root_node: Node) -> list:

    # Empty lists are Falsy
    if not root_node.children:
        return [root_node.letter]

    all_elements_list = []

    for child in root_node.children:

        # Find child letters
        child_letters = inorder_to_list(child)

        # Append this letter to each one
        mutated_nodes = [root_node.letter + letter for letter in child_letters]

        # Add to the final list
        all_elements_list += mutated_nodes

    return all_elements_list


def suggest_words(words: list, query: str) -> list:
    """
    A Trie is the perfect usage for autocomplete, especially because we can
    pre-process the set of words and then quickly suggest words depending on
    the available nodes.

    A Trie holds a Node for each letter in a word, with a next pointer to the next
    letter of the word. Thus, words sharing the same prefix will have the same node path
    from root, and the remaining children (suggestions) can be found.
    """

    # Construct a Trie from the words
    word_trie_root = construct_trie(words)

    # Keep track of the Node we're traversing
    current_node = word_trie_root

    for letter in query:

        # Search for the letter in the current node's children
        current_node = find_element(current_node.children, lambda node: node.letter == letter)

        # We can't find a matching element
        if current_node is None:
            return []

    # current_node now points to the Node that contains the query as prefix

    # Performing a traversal on this node to get the suggestions
    suggestion_suffix = []

    # If the query is a complete word, append an empty string to be picked up later
    if current_node.is_end_of_word:
        suggestion_suffix.append("")

    # Iterate over children to find the next suggestions
    for child in current_node.children:
        suggestion_suffix += inorder_to_list(child)

    # Adding the prefix query string to each suggestion
    suggestion_words = [query + suggestion for suggestion in suggestion_suffix]

    return suggestion_words


# Test Cases

# Example
assert suggest_words(["dog", "deer", "deal"], "de") == ["deer", "deal"]

# All Suggestions
assert suggest_words(["hello", "hey", "haylo", "heidi"], "he") == ["hello", "hey", "heidi"]

# No Suggestions
assert suggest_words(["abcd", "efgh", "ijkl", "mnop"], "yz") == []

# Find only Prefixes
assert suggest_words(["hello", "heylo", "abclo", "dello"], "lo") == []

# Complete words
assert suggest_words(["hello", "world", "i", "am", "calvin"], "calvin") == ["calvin"]

# Nested words
assert suggest_words(["hello", "world", "i", "am", "calvin", "calvinnor"], "calvin") == ["calvin", "calvinnor"]

# Repeated words - return only a single instance
assert suggest_words(["hello", "hello", "hello", "hello", "hello"], "he") == ["hello"]

# Palindromes
assert suggest_words(["abcdbca", "abba", "defed"], "ab") == ["abcdbca", "abba"]
