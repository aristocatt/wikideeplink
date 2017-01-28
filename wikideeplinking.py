from urllib.request import urlopen
from bs4 import BeautifulSoup

"""Deep linking in wikipedia to find relevant tags."""

class Node:

    def __init__(self,root_node, distance=0):
        self.distance = distance #distance from root node
        self.root_url = "https://en.wikipedia.org/"
        self.root_node = root_node
        self.tags = {}

    def buildTree(self):
            url = urlopen(self.root_url + self.root_node)
            soup = BeautifulSoup(url)
            content_wrapper = 'mw-content-text'
            content = soup.find('div',{'id':content_wrapper})
            for x in content.findAll('a'):
                self.tags[x['href']] = x.contents
            return self.tags


if __name__ == "__main__":
    node = Node("wiki/Branches_of_physics")
    tree = node.buildTree()
    print(tree)  #returns links such as #cite_ref-4 need to work through and remove these






