import connexion
import six
import logging
import json
import os

from application.models.requirement import Requirement  # noqa: E501
from application.entities import requirement
from application.preprocessing import preprocessing
from application.unsupervised import svd
from application.util import helper
from pprint import pprint


_logger = logging.getLogger(__name__)


def recommend_similar_requirements(body):  # noqa: E501
    """Retrieve a list with values for given set of requirements indicating their popularity for the crowd on twitter.

     # noqa: E501

    :param body: Requirement objects for which the social popularity should be measured
    :type body: list | bytes

    :rtype: List[Requirement]
    """
    response_list = []
    if connexion.request.is_json:
        content = connexion.request.get_json()
        assert isinstance(content, list)
        requs = [Requirement.from_dict(d) for d in content]  # noqa: E501

        train_requirements = list(filter(lambda r: not r.predict, requs))
        predict_requirements = list(filter(lambda r: r.predict, requs))

        train_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), train_requirements)
        predict_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), predict_requirements)
        train_requs = preprocessing.preprocess_requirements(train_requs,
                                                            enable_pos_tagging=False,
                                                            enable_lemmatization=False,
                                                            enable_stemming=False)
        predict_requs = preprocessing.preprocess_requirements(predict_requs,
                                                              enable_pos_tagging=False,
                                                              enable_lemmatization=False,
                                                              enable_stemming=False)

        _logger.info("SVD...")

        if len(train_requs) > 100:
            k = 10
        elif len(train_requs) > 50:
            k = 8
        elif len(train_requs) > 30:
            k = 5
        elif len(train_requs) > 10:
            k = 3
        elif len(train_requs) > 5:
            k = 2
        else:
            k = 1

        predictions_map = svd.svd(train_requs, predict_requs, k=k)
        for subject_requirement, similar_requirements in predictions_map.items():
            requ = Requirement.from_dict({
                "id": subject_requirement.id,
                "title": subject_requirement.title,
                "description": subject_requirement.description,
                "predict": True
            })
            requ.predictions = list(set(map(lambda r: r.id, similar_requirements)))
            response_list += [requ]
            for similar_requirement in similar_requirements:
                print("{} -> {}".format(subject_requirement, similar_requirement))

        """
        for idx, requ in enumerate(requirements):
            response_list.append(Requirement.from_dict({
                "id": requ.id,
                "title": requ.title,
                "description": requ.description
            }))
        """

    return response_list


def perform_svd():
    with open(os.path.join(helper.APP_PATH, "data", "requirements.json")) as f:
        requs = json.load(f)
    pprint(requs)
    requs = list(map(lambda r: Requirement.from_dict(r), requs))
    train_requirements = list(filter(lambda r: not r.predict, requs))
    predict_requirements = list(filter(lambda r: r.predict, requs))

    train_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), train_requirements)
    predict_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), predict_requirements)
    train_requs = preprocessing.preprocess_requirements(train_requs,
                                                        enable_pos_tagging=False,
                                                        enable_lemmatization=False,
                                                        enable_stemming=False)
    predict_requs = preprocessing.preprocess_requirements(predict_requs,
                                                          enable_pos_tagging=False,
                                                          enable_lemmatization=False,
                                                          enable_stemming=False)

    _logger.info("SVD...")
    predictions_map = svd.svd(train_requs, predict_requs, k=3)
    for subject_requirement, similar_requirements in predictions_map.items():
        for similar_requirement in similar_requirements:
            print("{} -> {}".format(subject_requirement, similar_requirement))

