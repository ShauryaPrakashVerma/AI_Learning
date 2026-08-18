from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")  # length of vector in this model is 384

# the greater the length of the vector, the higher is the accuracy.

# text1 = "Machine Learning is fun"

# embedding = model.encode(text1)
# print(embedding.shape)
# print(embedding[:10])


def cosine_similarity(a, b):
    return np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))


text1= "I love ice Cream"
text2 = "I like frozen desserts"

v1 = model.encode(text1)
v2 = model.encode(text2)

print(cosine_similarity(v1, v2))