import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer

from app.core.config import EMBEDDING_DIMENSION


class LocalEmbeddingModel:
    def __init__(self) -> None:
        self.vectorizer = HashingVectorizer(
            n_features=EMBEDDING_DIMENSION,
            alternate_sign=False,
            norm=None
        )

    def embed(self, text: str) -> list[float]:
        vector = self.vectorizer.transform([text]).toarray()[0]
        norm = np.linalg.norm(vector)

        if norm > 0:
            vector = vector / norm

        return vector.astype(float).tolist()


embedding_model = LocalEmbeddingModel()