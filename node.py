# Codecademy Node Data Structure

# Nodes - Contain data and a link (or multiple links) to other nodes

# Basic single link node
class Node:
    def __init__(self, value, link_node):
        self.value = value
        self.link_node = link_node

    