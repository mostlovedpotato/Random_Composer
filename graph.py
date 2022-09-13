# markov chain representation

import random


class Vertex:
    def __init__(self, value):  # values as words
        self.value = value
        self.adjacent = {}  # nodes connected to the current vertex
        self.neighbors = []
        self.neighbors_weight = []

    def add_edge_to(self, vertex, weight=0):  # adding edge to the vertex
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):  # increment the edge from the curr vertex
        # If the vertex exist in the adjacent if doesn't exist we default the value to zero
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_prob_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weight.append(weight)

    def next_word(self):
        # random selection of the next vertex
        return random.choices(self.neighbors, weights=self.neighbors_weight)[0]


class Graph:
    def __init__(self):
        # whenever we encounter a new word we can lookup in the dictionary
        # and get the vertex object from this dictionary
        # This is string to vertex mapping
        self.vertices = {}

    def get_vertex_values(self):
        # we return all the possible words we can have in the graph
        return set(self.vertices.keys())

    def add_vertex(self, value):
        # whenever we encounter a new word we add a new vertex
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # If value is not present
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, curr):
        return self.vertices[curr.value].next_word()

    def generate_prob_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_prob_map()
