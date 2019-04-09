# -*- coding: utf-8 -*-

# Todo : create a way to implement multi-output

class Persistence():

    def __init__(self, persistence_factory=None):
        self.persistence_factory = persistence_factory

    def store(self, data):
        persistence = self.persistence_factory(data)