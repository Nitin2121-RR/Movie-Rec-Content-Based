import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words='english')
data = pd.read_csv("names.csv")
vectors = cv.fit_transform(data['tag']).toarray()
similarity = cosine_similarity(vectors).astype("float32") 


