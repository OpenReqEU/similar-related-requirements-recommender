# coding: utf-8

from __future__ import absolute_import
from flask import json
from six import BytesIO
from application.test import BaseTestCase


class TestRecommendationController(BaseTestCase):
    """RecommendationController integration test stubs"""

    def test_compute_popularity(self):
        """Test case for compute_popularity

        Retrieve a list with values for given set of requirements indicating their popularity for the crowd on twitter.
        """
        body = '''[
            {
                "id": 0,
                "title": "",
                "description": "NOTE 1. The notes containing requirements shall also be considered to be “LC” for implementation of the systems within the project. They are labelled “NOTE” because they do not refer strictly to RBC (I)"
            },
            {
                "id": 1,
                "title": "",
                "description": " NOTE 2. The RBC notes and requirements in this document are rated as follows: (I) M – mandatory; the fulfilment of the conformity requirement must be proven in the tender; LC –mandatory conformity requirement; the requirement must be fulfilled until system commissioning; it is not required to be proven in the tender; I – Informative. The notes are generally provided for information purposes;   I/LC-EI – informative for RBC and LC for the EI installation;   LC/LC-EI – LC for RBC and LC for the EI installation."
            },
            {
                "id": 2,
                "title": "",
                "description": "NOTE 3 Other elements that will be taken into account (I)  - train coupling and decoupling shall be done by shunting. This is why the description of the related operations shall not be subject to this document;   - no temporary shunting areas shall be used."
            },
            {
                "id": 3,
                "title": "",
                "description": "NOTE 8. The transition from SRS 222 to SRS 230d is a minor and recent update of the software version used for the ETCS equipment (OBU, RBC, LEU, balises). Because the update is minor, the maturity of the solutions based on SRS 230d may include the maturity of the solutions based on SRS 222 and 230. Because the update is recent, at the time of the launch of this call for tenders, there are very few actual implementations of SRS 230d-based solutions. Therefore, for the assessment of the proposed solution, CFR accepts the inclusion of solutions based on SRS 222 and 230. (I)"
            },
            {
                "id": 4,
                "title": "",
                "description": "RBC 1 If the Contractor intends to introduce new functions and/or to propose improved solutions compared to those proposed in this document, they must be approved by CFR. (LC)"
            },
            {
                "id": 5,
                "title": "",
                "description": "RBC 2 This document shall be the basis for the preparation of the RBC CRS final version. (LC)"
            },
            {
                "id": 6,
                "title": "",
                "description": "RBC 3 If several RBCs are to be installed, each of them must meet the following values. (LC)"
            },
            {
                "id": 7,
                "title": "",
                "description": "RBC 4 MTBSF. For total failure, MTBSF for RBC (including the interfaces with the electronic interlocking installations and GSM-R) must be of at least 760,000 hours (M). The tender must include relevant documents proving this value. These documents must be drafted by independent bodies (e.g. EBA, Certifier, etc.)"
            },
            {
                "id": 8,
                "title": "",
                "description": "RBC 5 MTTR. For total failure, MTTR for RBC (including interfaces with the electronic interlocking installations and GSM-R) must be of at most 340 minutes (M). The tender must present relevant documents proving this value."
            },
            {
                "id": 9,
                "title": "",
                "description": "RBC 6 The tenderer must present in its tender the principles used for calculating MTBF and MTTR (M)."
            },
            {
                "id": 10,
                "title": "",
                "description": "RBC 7 The Tenderer must show in its tender how the RBC complies with the above MTBSF and MTTR values (LC)."
            },
            {
                "id": 11,
                "title": "",
                "description": "RBC 8 Availability. An availability of at least 99,955% must be provided for RBC (including interfaces with the electronic interlocking installations and GSM-R) (M). The tender must include relevant documents Relevant documents proving this value must be presented in the offer."
            },
            {
                "id": 12,
                "title": "",
                "description": "NOTE 5. Availability shall be calculated using the formula:"
            },
            {
                "id": 13,
                "title": "",
                "description": "RBC 9 The values above must be valid throughout the entire service life of the equipment (25 years). (LC)"
            },
            {
                "id": 14,
                "title": "",
                "description": "RBC 10 SIL4 The software and hardware equipment must be designed according to SIL 4, as described in the relevant CENELEC standards (EN 50126, EN 50128 and ENV 50129) (M). Relevant documents proving this value must be presented in the tender. These documents must be prepared by independent bodies (e.g. EBA, Certifer, etc.) (M)."
            },
            {
                "id": 15,
                "title": "",
                "description": "RBC 11 “Software and hardware equipment” shall mean, for the purposes of this document, RBC s, including the interfaces with the electronic interlocking installations and GSM-R (LC)."
            },
            {
                "id": 16,
                "title": "",
                "description": "RBC 12The RBC tender must comply with ENV 50129, paragraph B.2.6 „Fulfilment of specific environmental conditions” and with Appendix B4 „Operation under external influence conditions”. For B.4.6., the tenderer must submit its proposal. (LC)"
            },
            {
                "id": 17,
                "title": "",
                "description": "RBC 13 Environment-1 All the equipment must meet the relative humidity requirement: maximum 85% without condensation. (LC)"
            },
            {
                "id": 18,
                "title": "",
                "description": "RBC 14 Environment-2 All equipment must function in ambient temperatures:  a) -40°C to +70°C for outdoor equipment  b) -10°C to +50°C for outdoor equipment. Air conditioning systems may be used, in accordance with the standards in force, for situations where the equipment in the tender does not meet the specified limits. In this case, the availability indicated for the assembly formed of electronic equipment and air conditioning system must be higher than or equal to the availability indicated for the electronic equipment."
            },
            {
                "id": 19,
                "title": "",
                "description": "RBC 15 The outdoor equipment must be protected by means of safety measures against: (LC) theft, vandalism and sabotage vibrations water infiltrations dust infiltration For this purpose, the containers, cabinets, pickets and outdoor equipment cases must be provided with: an appropriate protection system against humidity an efficient locking system for containers and cabinets -doors with contacts, which signal their opening at the central post, water-sensitive equipment must be placed at least 1 meter above ground."
            },
            {
                "id": 20,
                "title": "",
                "description": "RBC 16 The RBC and the interfaces with the EI and GSM-R installations must be mounted in containers. It is allowed to install the ETCS equipment in the same container as the one intended for the EI installations. (LC)"
            },
            {
                "id": 21,
                "title": "",
                "description": "RBC 17 The tenderer must take into account the fact that the outdoor equipment is installed in the proximity of the 27 kV / 50 Hz contact line. (LC)"
            },
            {
                "id": 22,
                "title": "",
                "description": "RBC 18 EMC Electromagnetic compatibility must be ensured between the proposed solution and the INDUSI system available in the field and on the current locomotives. The tenderer must provide supporting documents in this regard. (M)"
            },
            {
                "id": 23,
                "title": "",
                "description": "RBC 19 RBC capacity. RBC (and GSM-R) must operate with at least 40 OBU located simultaneously in the area under its control (M)."
            },
            {
                "id": 24,
                "title": "",
                "description": "RBC 20 An IP/MPLS transmission network must be used between the RBC and MSC (LC)."
            },
            {
                "id": 25,
                "title": "",
                "description": "NOTE 6. This chapter refers to train operation when the interlocking, train detector and train integrity systems function properly, without disturbances. (I)"
            },
            {
                "id": 26,
                "title": "",
                "description": "RBC 21 The CMI must be of the vital MMI type, similar to the requirements presented in the EI installation specifications. The details on vital issues shall be presented in the CMI-RBC document. (LC)"
            },
            {
                "id": 27,
                "title": "",
                "description": "NOTE 7. In this document, the controller shall be the Traffic Regulator operator. (I)"
            },
            {
                "id": 28,
                "title": "",
                "description": "RBC 22 Any indication intended for the controller must be displayed on the CMI (LC)"
            },
            {
                "id": 29,
                "title": "",
                "description": "RBC 23 When an OBU enters in the area of a new EI in the RBC’s area of responsibility, the RBC must send the train number received from OBU to the EI installation (LC)"
            },
            {
                "id": 30,
                "title": "",
                "description": "RBC 24 If the train numbers are different, on CMI and MMI an error message must be displayed: “Train number error”. (LC/LC-EI)"
            }
        ]'''
        response = self.client.open(
            '/v1/recommend',
            method='POST',
            data=body,
            content_type='application/json')
        self.assert200(response, 'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
