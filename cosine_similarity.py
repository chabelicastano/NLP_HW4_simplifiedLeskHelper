import numpy as np
from numpy.linalg import norm

# ‘run’: {0, 2, 1}
# ‘sun’: {2, 0, 3}
# ‘eat’: {1, 2, 0}

# define the vectors
run_vector = np.array([0, 2, 1])
sun_vector = np.array([2, 0, 3])
eat_vector = np.array([1, 2, 0])


def cosine_sim(vector_1, vector_2):
    cosine = np.dot(vector_1, vector_2) / (norm(vector_1) * norm(vector_2))
    print('Cosine similarity between: {} and {} is {:.8f}'.format(vector_1, vector_2, cosine))


cosine_sim(run_vector, eat_vector)
