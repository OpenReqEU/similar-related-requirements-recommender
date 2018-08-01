import connexion
import six

from application.models.requirement import Requirement  # noqa: E501
from application.models.requirement_popularity import RequirementPopularity  # noqa: E501
from application.entities import requirement
from application.preprocessing import preprocessing


def recommend_similar_requirements(body):  # noqa: E501
    """Retrieve a list with values for given set of requirements indicating their popularity for the crowd on twitter.

     # noqa: E501

    :param body: Requirement objects for which the social popularity should be measured
    :type body: list | bytes

    :rtype: List[RequirementPopularity]
    """
    response_list = []
    if connexion.request.is_json:
        content = connexion.request.get_json()
        assert isinstance(content, list)
        requirements = [Requirement.from_dict(d) for d in content]  # noqa: E501
        requirements = map(lambda r: requirement.Requirement(r.id, r.title, r.description), requirements)
        """
        requirements = preprocessing.preprocess_requirements(requirements,
                                                             enable_pos_tagging=True,
                                                             enable_lemmatization=False,
                                                             enable_stemming=False)
        """

        for idx, requ in enumerate(requirements):
            response_list.append(Requirement.from_dict({
                "id": requ.id,
                "title": requ.title,
                "description": requ.description
            }))

    return response_list

