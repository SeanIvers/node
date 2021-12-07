# Codecademy Node Data Structure

# Nodes - Contain data and a link (or multiple links) to other nodes

# Basic single link node
class Node:
    def __init__(self, value, link_node):
        self.value = value
        self.link_node = link_node

    # Method to get value
    def get_value(self):
        return self.value

    # Method to get link
    def get_link_node(self):
        return self.link_node

    # Method to set link node
    def set_link_node(self, link_node):
        self.link_node = link_node