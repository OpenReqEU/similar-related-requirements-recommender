# -*- coding: utf-8 -*-

import logging
import numpy as np
from sklearn.metrics import precision_recall_fscore_support
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import metrics
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.metrics import pairwise_distances
import warnings

_logger = logging.getLogger(__name__)


def svd(train_requirements, k=3, max_distance=0.2):
    X_train = list(map(lambda r: ' '.join(map(lambda t: t.lower(), r.tokens(title_weight=1, description_weight=1))), train_requirements))

    warnings.filterwarnings("ignore", category=DeprecationWarning, module="pandas", lineno=570)
    vectorizer = CountVectorizer(min_df=1) #TfidfVectorizer(min_df=1, ngram_range=(1,1))
    document_term_matrix = vectorizer.fit_transform(X_train)
    n_total_tokens = document_term_matrix.shape[1]
    n_components = min(int(n_total_tokens / 3), 300)

    if n_components == 0:
        return {}

    print("Desired components: {}".format(n_components))
    lsa = TruncatedSVD(n_components=n_components, algorithm='randomized', n_iter=300, random_state=1)
    document_term_matrix_lsa = lsa.fit_transform(document_term_matrix)
    print("Actual components: {}".format(document_term_matrix_lsa.shape[1]))
    #document_term_matrix_lsa = Normalizer(copy=False).fit_transform(document_term_matrix_lsa)

    predictions_for_requirements = {}
    for subject_requirement_idx, transfered_requirement in enumerate(document_term_matrix_lsa):
        transfered_requirement = np.array([transfered_requirement])
        distance_matrix = pairwise_distances(transfered_requirement, document_term_matrix_lsa, metric='cosine', n_jobs=1)

        p_similar_requirements = np.sort(distance_matrix[0])
        similar_train_requirement_idx = np.argsort(distance_matrix[0])

        n_recommended_dependencies = 0
        predictions = []
        subject_requirement = train_requirements[subject_requirement_idx]
        for inner_idx, similar_requirement_idx in enumerate(similar_train_requirement_idx):
            if subject_requirement_idx == similar_requirement_idx:
                continue

            if n_recommended_dependencies >= k or p_similar_requirements[inner_idx] > max_distance:
                break

            similar_requirement = train_requirements[similar_requirement_idx]
            n_recommended_dependencies += 1
            predictions += [similar_requirement]
        predictions_for_requirements[subject_requirement] = predictions

    return predictions_for_requirements
