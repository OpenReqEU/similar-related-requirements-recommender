import connexion
import six
import logging
import json
import os
import csv
from application.models.requirement import Requirement  # noqa: E501
from application.entities import requirement
from application.preprocessing import preprocessing
from application.unsupervised import svd
from application.util import helper
from pprint import pprint


_logger = logging.getLogger(__name__)
FILTER_CHARACTERS_AT_BEGINNING_OR_END = ['.', ',', '(', ')', '[', ']', '|', ':', ';']


def recommend_similar_requirements(body):  # noqa: E501
    """Retrieve a list with values for given set of requirements indicating their popularity for the crowd on twitter.

     # noqa: E501

    :param body: Requirement objects for which the social popularity should be measured
    :type body: list | bytes

    :rtype: List[Requirement]
    """

    response_list = []
    # TODO: introduce parameter to set language
    lang = "en"

    if connexion.request.is_json:
        content = connexion.request.get_json()
        assert isinstance(content, list)
        requs = [Requirement.from_dict(d) for d in content]  # noqa: E501

        train_requirements = list(filter(lambda r: not r.predict, requs))
        predict_requirements = list(filter(lambda r: r.predict, requs))

        train_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), train_requirements)
        predict_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), predict_requirements)
        train_requs = preprocessing.preprocess_requirements(train_requs,
                                                            enable_pos_tagging=True,
                                                            enable_lemmatization=True,
                                                            enable_stemming=False,
                                                            lang=lang)
        predict_requs = preprocessing.preprocess_requirements(predict_requs,
                                                              enable_pos_tagging=True,
                                                              enable_lemmatization=True,
                                                              enable_stemming=False,
                                                              lang=lang)

        _logger.info("SVD...")

        if len(train_requs) > 100:
            max_distance = 0.1
            k = 10
        elif len(train_requs) > 50:
            max_distance = 0.2
            k = 8
        elif len(train_requs) > 30:
            max_distance = 0.25
            k = 5
        elif len(train_requs) > 10:
            max_distance = 0.3
            k = 3
        elif len(train_requs) > 5:
            max_distance = 0.35
            k = 2
        else:
            max_distance = 0.4
            k = 1

        predictions_map = svd.svd(train_requs, predict_requs, k=k, max_distance=max_distance)
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


def csv_reader(file_content):
    reader = csv.reader(file_content)
    content = []
    for row in reader:
        if row[0].strip() == "10820":
            break
        if row[-1].lower() == "def":
            content += [row[3]]
    return content


def perform_svd():
    enable_tagging = True
    max_distance = 0.35
    with open(os.path.join(helper.APP_PATH, "data", "requirements_en.json")) as f:
        requs = json.load(f)

    """
    max_distance = 0.005
    with open(os.path.join(helper.APP_PATH, "data", "siemens_requirements_en.csv")) as f:
        enable_tagging = False
        plain_requirements = csv_reader(f)
        requs = []
        predict_requirements_idx = len(plain_requirements) - int(len(plain_requirements) * 0.2)
        for (idx, description) in enumerate(plain_requirements):
            requs += [{
                'id': idx,
                'title': '',
                'description': description,
                'predict': idx > predict_requirements_idx
            }]
    """

    #pprint(requs)
    requs = list(map(lambda r: Requirement.from_dict(r), requs))
    train_requirements = list(filter(lambda r: not r.predict, requs))
    predict_requirements = list(filter(lambda r: r.predict, requs))
    lang = "en"

    train_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), train_requirements)
    predict_requs = map(lambda r: requirement.Requirement(r.id, r.title, r.description), predict_requirements)
    train_requs = preprocessing.preprocess_requirements(train_requs,
                                                        enable_pos_tagging=enable_tagging,
                                                        enable_lemmatization=enable_tagging,
                                                        enable_stemming=False,
                                                        lang=lang)
    predict_requs = preprocessing.preprocess_requirements(predict_requs,
                                                          enable_pos_tagging=enable_tagging,
                                                          enable_lemmatization=enable_tagging,
                                                          enable_stemming=False,
                                                          lang=lang)

    _logger.info("SVD...")
    predictions_map = svd.svd(train_requs, predict_requs, k=3, max_distance=max_distance)
    for subject_requirement, similar_requirements in predictions_map.items():
        if len(similar_requirements) == 0:
            continue

        #print("-" * 80)
        #print(subject_requirement.description_tokens)
        for similar_requirement in similar_requirements:
            print("#{}: {} -> #{}: {}".format(subject_requirement.id,
                                              subject_requirement.description[:80],
                                              similar_requirement.id,
                                              similar_requirement.description[:80]))
            #print(similar_requirement.description_tokens)
