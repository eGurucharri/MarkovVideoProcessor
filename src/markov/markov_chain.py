import numpy as np
import random

def create_markov_matrix(num_segments):
    markov_matrix = np.ones((num_segments, num_segments)) / num_segments
    return markov_matrix

def get_next_segment(current_segment, markov_matrix):
    probabilities = markov_matrix[current_segment]
    next_segment = np.random.choice(range(len(probabilities)), p=probabilities)
    return next_segment
