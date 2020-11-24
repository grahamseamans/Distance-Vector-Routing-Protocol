'''
Graham Seamans
Written for internetworking protocols, nothing too fancy
'''

import sys
import numpy as np

edges = []

class node:
    def __init__(self, id, neighbors, neighbor_distance, network_size) -> None:
        self.routing_table =  [10000 for i in range(network_size)]
        self.distance_table = np.full((network_size, network_size), 10000)
        for i, n in enumerate(neighbors):
            self.distance_table[n][n] = neighbor_distance[i]
        self.update_queue = []
        self.id = id
        self.neighbors = [n for n in neighbors]
        self.updated = True
    
    def turn(self):
        if self.updated:
            self.broadcast()
        while self.update_queue:
            (sender, senders_routing_table) = self.update_queue.pop(0)
            self.update(sender, senders_routing_table)
        self.update_routing()

    def broadcast(self):
        for n in self.neighbors:
            edges[n].update_queue.append((self.id, self.routing_table))
 
    def update(self, sender, senders_routing_table):
        '''
        update:
            find my time to sender (min from senders row) (min_sender)
            for e in senders routing table:
                if e + min_sender < that cell in senders column:
                    set that cell to e + min_sender
        '''
        time_from_sender = min(self.distance_table[sender])
        for i, time in enumerate(senders_routing_table):
            if i != self.id:
                if time_from_sender + time < self.distance_table[sender][i]:
                    self.distance_table[sender][i] = time_from_sender + time

    def update_routing(self):
        self.updated = False
        trans = np.transpose(self.distance_table)
        for i, row in enumerate(trans):
            fastest = min(row)
            if fastest < self.routing_table[i]:
                self.updated = True
                self.routing_table[i] = fastest

    def print_node(self):
        print('\nmy id is', self.id)
        print(np.transpose(self.distance_table))
        print('routing table', self.routing_table)

def pos_to_char(pos):
    return chr(pos + 97)

if __name__ == "__main__":
    network_size = 8
    t = {pos_to_char(a): a for a in range(10)}

    # for i in range(network_size):
        # def __init__(self, id, neighbors, neighbor_distance, network_size) -> None:
    # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g'), (7, 'h'), (8, 'i'), (9, 'j')]


    edges.append(node(0, [1, 2], [14,2], network_size))
    edges.append(node(1, [0,2,5,4], [14,8,3,1], network_size))
    edges.append(node(2, [0,1,6], [2,8,1], network_size))
    edges.append(node(3, [4,5], [7,10], network_size))
    edges.append(node(4, [1,3,5], [1,7,1], network_size))
    edges.append(node(5, [1,3,4,6,7], [3,10,1,3,1], network_size))
    edges.append(node(6, [2,5,7], [1,3,5], network_size))
    edges.append(node(7, [5,6], [1,5], network_size))

    for e in edges:
        e.print_node()

    print('\nINITED\n')

    # for i in range(5):
    while edges[0].updated:
        print(edges[0].routing_table)
        for e in edges:
            e.turn()
    '''
    for e in edges:
        e.turn()
    '''
    print('\nDONE\n')
    for e in edges:
        e.print_node()



