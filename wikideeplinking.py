from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import time

"""Deep linking in wikipedia to find relevant tags."""

class Node:

    def __init__(self,root_node, distance=0, prev_node=None):
        self.distance = distance #distance from root node
        self.root_url = "https://en.wikipedia.org"
        self.root_node = root_node #url of node
        self.prev_nodes = prev_node #[[nodeClass, distance],[nodeClass2,distance],etc]
        self.branch = {}

    def buildTree(self, branches=1):
        while branches > 0:
            branches -= 1
            link = urlopen(self.root_url + self.root_node)
            soup = BeautifulSoup(link)
            content_wrapper = 'mw-content-text'
            content = soup.find('div',{'id':content_wrapper})
            for x in content.findAll('a'):
                content = str(x.contents)
                url = str(x['href'])
                if url.startswith('/wiki'):
                    if url.endswith(('.png','.svg')):
                        pass
                    elif self.fillWeb(content) == True:
                        print('web filled')
                        pass
                    else:
                        self.branch[content] = Node(url,distance = self.distance + 1,
                                                    prev_node=[[self,self.distance]])
            for x in self.branch:
                self.branch[x].buildTree(branches)

    def fillWeb(self, content, **kwargs):
        if 'retreat' in kwargs:
            curr_node = kwargs['retreat']
        else:
            curr_node = self
            if content in curr_node.branch.keys():
                return True
        node = self
        if curr_node.prev_nodes != None:
            self.fillWeb(content, node=node,retreat=curr_node.prev_nodes[0][0])
        else:
            return self.scourTree(content,node,curr_node)

    def scourTree(self,content,node,curr_node):
        for x in curr_node.branch:
            if content == x:
                print(content)
                print(curr_node.root_node)
                print(node)
                print(node.distance)
                curr_node.branch[content].prev_nodes.append([node,node.distance])
                return True
            if len(curr_node.branch[x].branch) > 0:
                self.scourTree(content,node,curr_node.branch[x])
            else:
                return False

        return False









if __name__ == "__main__":
    time1 = time()
    node = Node("/wiki/Branches_of_physics")

    tree = node.buildTree(2)
    time2 = time()
    finaltime = time2 - time1
    print(finaltime)








