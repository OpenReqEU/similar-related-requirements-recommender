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
            },
            {
                "id": 31,
                "title": "",
                "description": "RBC 25 Route configuration (LC) The RBC must include a database containing information about route configuration. The route configuration must comprise at least: Track sections (identification, length) Balises Switches ITN. See MA over a malfunctioning ITN. Declivities Static speed profiles for various train categories Static speed profiles for switches on diverging position Areas where MAs are not allowed to end or trains are not allowed to stop Catenary line characteristics Maximum permitted axle load of the line Kilometric positions National values Temporary speed restrictions Whistle indicators Neutral sections of the contact line (with indication: “main power switch off”) Metallic bridges and other possible large metallic masses (this is part of the balise engineering!)."
            },
            {
                "id": 32,
                "title": "",
                "description": "RBC 26. The ITN shall not be part of the track configuration”. RBC must perform ITN information management (telegrams, text messages, TSR). See also “MA over malfunctioning level crossing” (LC)."
            },
            {
                "id": 33,
                "title": "",
                "description": "RBC 27 Operational data (LC) The RBC must dynamically use a set of operational data. The operational data must comprise at least: The latest position received for all registered trains The latest speed received for all registered trains MODE in which trains are running Other data received by the train It must be possible to display such data on the CMI."
            },
            {
                "id": 34,
                "title": "",
                "description": "RBC 28 At start-up, the RBC must check its configuration and run a self-testing program. (LC)"
            },
            {
                "id": 35,
                "title": "",
                "description": "RBC 29 Disturbances that may lead to unsafe RBC operation must be reported to the controller (LC)."
            },
            {
                "id": 36,
                "title": "",
                "description": "RBC 30 The RBC must recognise its own system’s failure conditions (LC)."
            },
            {
                "id": 37,
                "title": "",
                "description": "RBC 32 TSR after system restart In the event of system failure and system restart, the RBC must preserve/memorise all temporary speed restrictions. After system failure and system restart, the RBC must display all stored TSRs to the controller for confirmation. (LC)"
            },
            {
                "id": 38,
                "title": "",
                "description": "RBC 32 Last conditions memorised The RBC must store and be able to display on the CMI, at start-up, the specific RBC data (route configuration), or others, if necessary (LC)."
            },
            {
                "id": 39,
                "title": "",
                "description": "RBC 33 After restart-1 (LC) After restart, the RBC must determine: The position of trains (after the OBU receives the position reports) The status of objects (from the interlocking installations)"
            },
            {
                "id": 40,
                "title": "",
                "description": "RBC 34 After restart -2 (LC) After restart, the RBC must request each OBU, with which it still has an open communication, to close the session and initiate a new start of mission."
            },
            {
                "id": 41,
                "title": "",
                "description": "RBC 35 After restart - 3) (LC) When the RBC is ready to operate safely, after restart, it must report to the controller and the system maintenance personnel."
            },
            {
                "id": 42,
                "title": "",
                "description": "RBC 36 A valid position is the position obtained after passing over a balise group. The OBU – RBC system must be able to recognise a valid position, as the valid position was previously defined. This requirement is valid for all cases, not just only “after restart” (LC)."
            },
            {
                "id": 43,
                "title": "",
                "description": "RBC 37 The RBC must know the balise groups in its area and the balise groups in its related transition / announcement areas (LC)."
            },
            {
                "id": 44,
                "title": "",
                "description": "RBC 38 The RBC must always be able to determine whether a reported position corresponds to its area or not (LC)."
            },
            {
                "id": 45,
                "title": "",
                "description": "NOTE 8 If the new valid position reported indicates that the OBU is not in its controlled area or in a related announcement/transition area, see the definitions in SRS 230d - 5.4.2.1. (LC)"
            },
            {
                "id": 46,
                "title": "",
                "description": "RBC 39 The RBC must be able to transmit to the corresponding train any modification occurring in the EI installation which affects this train, e.g. by sending conditional/unconditional emergency stop messages, when the conditions for train movement are no longer fulfilled (LC)."
            },
            {
                "id": 47,
                "title": "",
                "description": "RBC 40 When the RBC has registered the train number, the number must be indicated on the controller’s screen so that the controller may easily identify the last track section occupied by the train. This indication must be based on information received from the OBU. (LC)"
            },
            {
                "id": 48,
                "title": "",
                "description": "RBC 41The announcement / transition areas must be indicated on the CMI. (LC)"
            },
            {
                "id": 49,
                "title": "",
                "description": "RBC 42 The start and end conditions (display and deletion) for individual text messages, on DMI, shall be specified as part of data preparation (LC)."
            },
            {
                "id": 50,
                "title": "",
                "description": "RBC 43 The system’s reaction to “linking” related problems must be “no reaction” (LC)."
            },
            {
                "id": 51,
                "title": "",
                "description": "RBC 44 The RBC must accept / register the train, even if the reported position is invalid (LC)."
            },
            {
                "id": 52,
                "title": "",
                "description": "RBC 45 When a train has been registered with an invalid position, the RBC must only be allowed to issue a movement authorisation for that train in the “Staff Responsible” mode (LC)."
            },
            {
                "id": 53,
                "title": "",
                "description": "RBC 46 As soon as the RBC receives the first valid position report from the train, the train and its number must be indicated in the relevant position on the CMI (LC)."
            },
            {
                "id": 54,
                "title": "",
                "description": "RBC 47 If the train is accepted by the RBC, the registration must be made according to the “TSI CCS Annex A” document (LC)."
            },
            {
                "id": 55,
                "title": "",
                "description": "RBC 48 The RBC must not accept / register a train if the valid position reported indicates that the OBU is not in its controlled area or in the announcement / transition areas. A message shall be sent to the train indicating the cancellation (from RBC perspective) and the communication session shall be closed (LC)."
            },
            {
                "id": 56,
                "title": "",
                "description": "RBC 49 The train must not be slowed down as a result of any level transition (LC)."
            },
            {
                "id": 57,
                "title": "",
                "description": "RBC 50. At CFR, the entry point into a level 2 area must be a traffic signal. The announcement/transition area must be the section before that signal (LC). RBC 51 When designing the RBC, account shall be taken of the fact that it is necessary to provide “maintained areas” at the ends, in order to ensure the issuance of movement authorisations in accordance with the requirements of this document."
            },
            {
                "id": 58,
                "title": "",
                "description": "RBC 52 Account must be taken of the fact that the information necessary to the “maintained area” shall be taken from systems implemented outside the project. (LC)"
            },
            {
                "id": 59,
                "title": "",
                "description": "RBC 53 The border between level 0 and level 2 must be a traffic signal, in accordance with the figure. The level change must occur after this signal. (LC)"
            },
            {
                "id": 60,
                "title": "",
                "description": "NOTE 9 The figure shall be deemed indicative, given as an example (I)"
            },
            {
                "id": 61,
                "title": "",
                "description": "RBC 54 The transition procedure must be the one presented in the “TSI CCS Annex A” document, plus the requirements of this document. (LC)"
            },
            {
                "id": 62,
                "title": "",
                "description": "RBC 55 The RBC must not send the same MA to 2 consecutive trains, running from a level 0 area to a level 2 area. (LC)"
            },
            {
                "id": 63,
                "title": "",
                "description": "RBC 56 Trains coming from non-RBC controlled areas (level 0 or 1) must be automatically registered without need of braking for this purpose. (LC)"
            },
            {
                "id": 64,
                "title": "",
                "description": "RBC 57 Even if no route has been set for the train, the transition must be announced by the LTA balise group, but no MA is issued to the train in this case. (LC)"
            },
            {
                "id": 65,
                "title": "",
                "description": "RBC 58. The border between level 1 and level 2 areas must be a traffic signal. (LC)"
            },
            {
                "id": 66,
                "title": "",
                "description": "RBC 59 The border signals shall be connected both to ETCS level 1 (LEU), and to ETCS level 2 (RBC), by means of the EI installation. (LC)"
            },
            {
                "id": 67,
                "title": "",
                "description": "RBC 60 If the border signal is a block signal on “STOP” due to a reason for which RBC could issue MA (burnt lamps, malfunctioning ITN, occupied section, etc.), the RBC must issue this MA which will become active when the transition is completed. (LC)"
            },
            {
                "id": 68,
                "title": "",
                "description": "RBC 61 A MA may be admitted by the ETCS system level 1 over the ETCS level 2 area, in order to prevent the reduction of the speed/braking of the OBU due to the level transition. (LC)"
            },
            {
                "id": 69,
                "title": "",
                "description": "RBC 62 In any situation, after the transition is completed, if it is necessary:   - for RBC to reduce the MA given by the ETCS system level 1 OR   - to introduce a TSR on the existing MA this must be done immediately."
            },
            {
                "id": 70,
                "title": "",
                "description": "RBC 63 If the condition above may not be met due to the lack of communication between the OBU and the RBC, the related T_NVCONTACT functionality must be triggered. See also the chapter “T_NVCONTACT”. (LC)"
            },
            {
                "id": 71,
                "title": "",
                "description": "RBC 64 The requirements are the same as those set out in chapter “Automatic transition from level 0 to level 2”. (LC)"
            },
            {
                "id": 72,
                "title": "",
                "description": "RBC 65. The border between level 2 and level 0 areas must be a traffic signal. The level change must occur before this signal, so that the train may pass the signal in INDUSI mode and the driver may see and follow the signal indications (LC)."
            },
            {
                "id": 73,
                "title": "",
                "description": "NOTE 10 The figure shall be deemed indicative, given as an example. (I)"
            },
            {
                "id": 74,
                "title": "",
                "description": "RBC 66 The transition procedure must be the one presented in the “TSI CCS Annex A” document, plus the requirements in this document. (LC)"
            },
            {
                "id": 75,
                "title": "",
                "description": "RBC 67 The transition to level 0 must be made before the signal, in accordance with the following figure, so that the train may pass the signal with active INDUSI. The length of the issued MA must be until the next signal, over the limits of level 2 area, but will disappear (will be cancelled in the OBU) when the transition to level 0 is completed. (LC)"
            },
            {
                "id": 76,
                "title": "",
                "description": "RBC 68 The MA must be issued over the limits of the level 2 area so that the train may be able to pass the signal without speed restrictions. (LC)"
            },
            {
                "id": 77,
                "title": "",
                "description": "RBC 69 The details regarding the positions of balises for the exit of the OBU from Level 2 to Level 0 shall be specified as part of the data preparation for each particular case. (LC)"
            },
            {
                "id": 78,
                "title": "",
                "description": "RBC 70 The border between level 2 and level 1 must be a traffic signal. (LC)"
            },
            {
                "id": 79,
                "title": "",
                "description": "RBC 71 Border signals shall be connected to both ETCS level 1 (LEU), and ETCS level 2 (RBC), by means of the EI installation. (LC)"
            },
            {
                "id": 80,
                "title": "",
                "description": "RBC 72 If the border-signal is set to STOP, the MA ends at this signal. (LC)"
            },
            {
                "id": 81,
                "title": "",
                "description": "RBC 73 If the border-signal displays a permissive aspect, the MA does not end at this signal. (LC)"
            },
            {
                "id": 82,
                "title": "",
                "description": "RBC 74 The telegram announcing the level change (including the position where the change will occur) must be issued by the RBC and by the balise group announcing the transition (LTA-BG). (LC)"
            },
            {
                "id": 83,
                "title": "",
                "description": "RBC 75. The transition (when the train passes the LT-BG at the latest) shall be completed before the border signal. (LC)"
            },
            {
                "id": 84,
                "title": "",
                "description": "RBC 76. This type of transition is not be requested by CFR. (LC)"
            },
            {
                "id": 85,
                "title": "",
                "description": "RBC 77 The value for the T_NVCONTACT variable is set at 15 seconds and the reaction indicated by the M_NVCONTACT variable is “service braking”. (LC)"
            },
            {
                "id": 86,
                "title": "",
                "description": "RBC 78 The value for the T_NVCONTACT shall also be entered in the balises announcing the transition to level 2 (LTA-BG), as well as in the balises for the transition to level 2 (LTA-BG). (LC)"
            },
            {
                "id": 87,
                "title": "",
                "description": "RBC 79 When the transition to level 2 is completed, the T_NVCONTACT related functionality must be active even if no connection is established with RBC. In this case, the T_NVCONTACT control must be triggered when the transition is completed (LC)."
            },
            {
                "id": 88,
                "title": "",
                "description": "RBC 80 The train must not be slowed down as a result of a handover between the two RBCs. (LC)"
            },
            {
                "id": 89,
                "title": "",
                "description": "RBC 81 The border between the two RBCs must be at a traffic signal. (LC)"
            },
            {
                "id": 90,
                "title": "",
                "description": "RBC 82 The CFR block signals are mounted two per mast, “back-to-back”. If the border between two RBCs is formed of block signals, one of these signals shall represent the border for the first level 2 area, and the second signal – for the second area."
            },
            {
                "id": 91,
                "title": "",
                "description": "RBC 83 The proposed system must (M): - either commercially operated by a railway administration in the European Union, or Switzerland. - when implemented as above, the proposed RBC must perform the HANDOVER function with an RBC produced by another supplier based on the European requirements specified in subset 039 version 2.1.2 or further."
            },
            {
                "id": 92,
                "title": "",
                "description": "RBC 84 Before issuing an MA, the RBC must make sure that the train position is correctly allocated to a location and line and that these are up-to-date. (LC)"
            },
            {
                "id": 93,
                "title": "",
                "description": "RBC 85 The RBC must give the parameters for the OBU request for a new MA. T_MAR = 20 seconds. (LC)"
            },
            {
                "id": 94,
                "title": "",
                "description": "RBC 86 In the station the OBU must not have an MA if the latter does not “mirror” a route locked in the electronic interlocking installation. (LC)"
            },
            {
                "id": 95,
                "title": "",
                "description": "RBC 87 In the case of an OBU MA (with the corresponding route locked) including an interlocking route ahead for which the EIL notifies the RBC that the train is no longer permitted to enter the route, the RBC must immediately revoke the MA with a new EoA at the signal that had authorised the route. The RBC shall ensure by means of requesting an acknowledgement from the OBU, that the shortened MA is being used by the OBU (LC),"
            },
            {
                "id": 96,
                "title": "",
                "description": "NOTE 11. There are several reasons why entering the route is no longer permitted, including the train movement control operator setting the start signal to “STOP”, the cancellation of a route or the loss of detection of a route due to a malfunction (I)"
            },
            {
                "id": 97,
                "title": "",
                "description": "NOTE 12. If a completely locked route is unlocked, the 110 sec. Time-lag in the EI installation ensures the stopping of the train until the route is unlocked. This is the case even when, due to radio communication loss, the RBC is not able to shorten the OBU’s MA, but the reaction of the OBU due to the T_NVCONTACT (15 sec) will lead to the stopping of the train by applying the hand brake (I)."
            },
            {
                "id": 98,
                "title": "",
                "description": "NOTE 13 The unlocking of a previously locked route shall be done immediately, irrespective of whether a new MA is issued for this route or not. The length of the total locking area is calculated in such a manner as to ensure the stopping of the train when the service brake is applied as a result of the T_NVCONTACT, before it reaches the locked route (I/LC-EI)"
            },
            {
                "id": 99,
                "title": "",
                "description": "NOTE 14 The situation when the train has passed a signal and the remaining route until the following signal loses its detection as a result of a failure is described in RBC 115 et seq. (I)"
            },
            {
                "id": 100,
                "title": "",
                "description": "RBC 88 The revocation of an MA (from the OBU) must be executed by the RBC by means of an emergency stopping message sent by the RBC. When it receives an emergency stopping message, the OBU confirms whether the MA revocation has been executed. (LC)"
            },
            {
                "id": 101,
                "title": "",
                "description": "RBC 89 The emergency STOP message, as an independent command initiated by the controller for a specific train, shall be implemented (LC)."
            },
            {
                "id": 102,
                "title": "",
                "description": "NOTE 15 It must be possible to stop all the trains from a certain area (no smaller than a station or open line between two stations), with a single stop command executed in the electronic interlocking installation. (I/LC-EI)"
            },
            {
                "id": 103,
                "title": "",
                "description": "RBC 90 The conditional emergency stop shall be used at CFR. (LC)"
            },
            {
                "id": 104,
                "title": "",
                "description": "RBC 91 The RBC must never issue an MA for an OBU, if one of the following elements is missing: (LC) MA request from OBU route set in the EI installation known ETCS level (the RBC must know the level in which the OBU is running) position report from OBU running direction (in case the OBU is not in the RBC area, but in the approach area)."
            },
            {
                "id": 105,
                "title": "",
                "description": "RBC 92 The length of an MA shall be given in accordance with the signal indications/route setting in the EI (LC)."
            },
            {
                "id": 106,
                "title": "",
                "description": "RBC 93 Because the line in the project is a conventional line with signals, the length of the new MA must depend on the route lengths. (LC)"
            },
            {
                "id": 107,
                "title": "",
                "description": "RBC 94 Under normal circumstances (FS or OS without braking triggered by the system), an MA must always end at a traffic signal (LC)."
            },
            {
                "id": 108,
                "title": "",
                "description": "RBC 95 The EoA shall always be at a traffic signal (LC)."
            },
            {
                "id": 109,
                "title": "",
                "description": "RBC 96 The speed indication on the DMI OBU shall take preference over any speed indications from traffic signals. (LC)"
            },
            {
                "id": 110,
                "title": "",
                "description": "RBC 97 The length of the new MA shall be determined according to the following rules (LC): a. not longer than 6 sectors b. max. 6600 m"
            },
            {
                "id": 111,
                "title": "",
                "description": "RBC 98 In order to determine the length of the MA based on requirement RBC 97, RBC shall start from the value 0 and “add” sections until one of the two conditions is met (either 6 sectors, or a length of 6600 m) (LC)."
            },
            {
                "id": 112,
                "title": "",
                "description": "RBC 99 Based on the routes set in the electronic interlocking installation and the rule above, the RBC must determine an MA of a certain length and to send it to the OBU. (LC)"
            },
            {
                "id": 113,
                "title": "",
                "description": "RBC 100 In order to indicate the time when OBU must request a new MA/an MA extension, pack 57 shall be sent to OBU, once. (LC)"
            },
            {
                "id": 114,
                "title": "",
                "description": "RBC 101 The point where OBU must request a new MA (the extension of the current MA) must be located before the point in which the OBU should start braking, in accordance with the MRSP (Most Restrictive Speed Profile). The “time” between those moments shall be T_MAR=20 sec. (LC)"
            },
            {
                "id": 115,
                "title": "",
                "description": "NOTE 102 Having begun requesting an MA, the OBU must continue its request until it receives the MA. (LC)"
            },
            {
                "id": 116,
                "title": "",
                "description": "RBC 103 When receiving a request for an MA from a train, the RBC must request the EI to create a route for the train in question. (LC)"
            },
            {
                "id": 117,
                "title": "",
                "description": "NOTE 16 The route request in stations will no longer be displayed on the MMI (I/LC-EI): after 110 seconds OR upon the request of the train movement control operator by means of a normal, but recorded command, within the 110 seconds interval."
            },
            {
                "id": 118,
                "title": "",
                "description": "NOTE 17. The request may consist of an indication or a text message displayed on the MMI screen (of the TMCO) (I/LC-EI)"
            },
            {
                "id": 119,
                "title": "",
                "description": "NOTE 18 The EI installation must be able to receive requests from the RBC regarding route initiation (I/LC-EI)"
            },
            {
                "id": 120,
                "title": "",
                "description": "NOTE 19. The EI installation shall not initiate the requested route on its own (except where the automatic route setting function is activated). This is the task of the TMCP. The EI installation must, through the MMI, only inform the TMCO on the request. (I/LC-EI)"
            },
            {
                "id": 121,
                "title": "",
                "description": "RBC 104 When the route was previously set, the RBC must not issue an MA if the OBU has not already requested one. (LC)"
            },
            {
                "id": 122,
                "title": "",
                "description": "NOTE 20. Explanation: after a signal is set to “CLEAR”, a new MA request is required from the OBU, because this is an extension not a shortening of the MA. (I)"
            },
            {
                "id": 123,
                "title": "",
                "description": "RBC 105 When the RBC receives a request: if the route is already set, the MA shall be issued immediately, without an additional request to the EI installation. If the route is not set (the issuance of an MA is not possible), the RBC must request the EI installation to set a route. (LC)"
            },
            {
                "id": 124,
                "title": "",
                "description": "RBC 106 The request for an MA (and whether it was resolved or not) must be displayed on the CMI. (LC)"
            },
            {
                "id": 125,
                "title": "",
                "description": "RBC 107 The CMI must display the length of each MA. The MA must be permanently displayed. (LC)"
            },
            {
                "id": 126,
                "title": "",
                "description": "RBC 108 The MA set over a section with switches (in a station) must take into account all the static speed profiles (SSP) corresponding to the “divergent” positions of the points (smaller speed values compared to the speed on the straight line). (LC)"
            },
            {
                "id": 127,
                "title": "",
                "description": "RBC 109 The issuance of an MA over a signal set to “STOP”: If the signal is displaying “permissive stop” or if it is an “absolute stop” signal and it displays a “calling on locked route” indication, which requires a locked route covered by the signal, the RBC must issue the corresponding MA. (LC)"
            },
            {
                "id": 128,
                "title": "",
                "description": "RBC 110 Depending on the situation, the MA over a signal displaying the STOP indication, can be FS or OS. Issuing the MA must be in accordance with Chapter RBC 268. (LC)"
            },
            {
                "id": 129,
                "title": "",
                "description": "NOTE 21 The EI installations must memorise the reason why a signal display the stopping indication (STOP), especially for signals with “permissive stop” (I/LC-EI)"
            },
            {
                "id": 130,
                "title": "",
                "description": "RBC 111 If more than one motor vehicle (OBU) is on a section and the EI installation executes a route, the RBC must be able to send MAs to the corresponding OBU based on the OBU position report. (LC)"
            },
            {
                "id": 131,
                "title": "",
                "description": "RBC 112 The RBC shall never issue an MA that is not consistent with train orientation. (LC)"
            },
            {
                "id": 132,
                "title": "",
                "description": "RBC 113 It is not acceptable, in any situation, for a train to have an MA over a route/part of a route that is no longer locked. (LC)"
            },
            {
                "id": 133,
                "title": "",
                "description": "RBC 114 A change of the signal indication from “permissive” to “STOP” must trigger the issuance of a new, updated, MA by the RBC. (LC)"
            },
            {
                "id": 134,
                "title": "",
                "description": "RBC 115 If the OBU has passed a signal (which had a permissive indication) and a switch or a level crossing installation in the remaining locked route (previously authorised by the signal in question) loses its control/detection, the RBC must initiate the issuance of a TSR over the element in question (switch/level crossing installation). These considerations shall only be valid in the station (LC)"
            },
            {
                "id": 135,
                "title": "",
                "description": "RBC 116 The system reaction must be triggered only if the loss of control/detection of the system occurs “in front of the train”. (LC)"
            },
            {
                "id": 136,
                "title": "",
                "description": "RBC 117 TSR-related data (LC): a. They will NOT be indicated on the CMI. b. TSRs for level crossing installations shall have the following characteristics: speed: 20 km/h. length equal to road width plus 50 m (the distance to the failure signal, according to the figure at point RBC 206). TSR shall start at the road end, near the locomotive. the restriction shall be observed only by the front end of the train. c. TSRs for switches shall have the following characteristics: speed: 20 km/h. length equal to point length (tip – heel). TSR shall start 1 m from the point tip or 1 m from the point heel. the restriction shall be observed by the rear end of the train."
            },
            {
                "id": 137,
                "title": "",
                "description": "RBC 118 The switches or level crossing installations on overlaps shall not be taken into account for this function. (LC)"
            },
            {
                "id": 138,
                "title": "",
                "description": "NOTE 22. The preliminary information must be given by the EI installation. This means that the EI installation must detect the status of objects locked in a route, even if the OBU has passed the signal authorising the route (I/LC-EI)"
            },
            {
                "id": 139,
                "title": "",
                "description": "NOTE 23. A signal may be set to “STOP” by the TMCO or by the EI installation (I/LC-EI)."
            },
            {
                "id": 140,
                "title": "",
                "description": "NOTE 24 As an effect, the EI installation must inform the RBC and the RBC must issue a new MA, shorter than the current MA, to the OBU (LC)."
            },
            {
                "id": 141,
                "title": "",
                "description": "NOTE 25 This new MA is mandatory, meaning that the OBU must accept it, even if this leads to an emergency braking. (I)"
            },
            {
                "id": 142,
                "title": "",
                "description": "RBC 119 In the case of a switch halfway through the siding line, the following functional requirements shall be taken into account when configuring the RBC/EI (LC/LC-EI):"
            },
            {
                "id": 143,
                "title": "",
                "description": "a) if the train stops on the first section without switch (before the switch, in the running direction), the route shall be unlocked after 180 seconds."
            },
            {
                "id": 144,
                "title": "",
                "description": "b) unlocking must lead to the cancellation of the MA which was to end at the signal."
            },
            {
                "id": 145,
                "title": "",
                "description": "c) The shortening of the MA must be done in such a manner that:"
            },
            {
                "id": 146,
                "title": "",
                "description": " - OBU remains in the mode it was when stopping on the first section."
            },
            {
                "id": 147,
                "title": "",
                "description": " - when the exit signal is set to “CLEAR”, because this command locks behind it the sections of the siding line, an MA (MA1) shall be issued from the signal behind, in order for the"
            },
            {
                "id": 148,
                "title": "",
                "description": "OBU to be able to reach the signal, as follows:"
            },
            {
                "id": 149,
                "title": "",
                "description": "  - if the OBU is in FS mode, it shall receive MA 1 FS until the signal."
            },
            {
                "id": 150,
                "title": "",
                "description": "  - if the OBU is in OS mode, no MA 1 shall be issued. The driver shall activate OVERRIDE and shall move towards the signal in SR mode."
            },
            {
                "id": 151,
                "title": "",
                "description": "  - if the OBU is in SR mode, no MA 1 shall be issued. The driver shall move towards the signal in SR mode."
            },
            {
                "id": 152,
                "title": "",
                "description": " - if any of the two sections between OBU and the exit signal is occupied, or the switch does not have control, the MA 1 shall not be issued."
            },
            {
                "id": 153,
                "title": "",
                "description": " - Also, when the exit signal is set to “CLEAR”, and MA (MA 2) shall be issued from the signal to the maximum distance that may be covered by the system."
            },
            {
                "id": 154,
                "title": "",
                "description": " - when the OBU (in SR mode) enters the TAF window, the RBC shall issue TAF or MA2."
            },
            {
                "id": 155,
                "title": "",
                "description": "NOTE 26 A possible solution is to implement, at the ends of the switch section, certain virtual signals in the EI installation (I/I-EI)"
            },
            {
                "id": 156,
                "title": "",
                "description": "RBC 120 If the OBU is on a route (in a station) and the TMCO activates the DFP for that route, the MA shall be immediately cancelled. (LC)"
            },
            {
                "id": 157,
                "title": "",
                "description": "RBC 121 If the connection between the RBC and the EI installation is lost, the RBC must consider all signals commanded by the EI as set to ”STOP”. (LC)"
            },
            {
                "id": 158,
                "title": "",
                "description": "RBC 122 The RBC shall consider the connection with the EIL as failed, if the duration of the interruption exceeds 5 seconds. (LC)"
            },
            {
                "id": 159,
                "title": "",
                "description": "RBC 123 The RBC shall not issue an MA for any signal in the station or block. (LC)"
            },
            {
                "id": 160,
                "title": "",
                "description": "RBC 124 All level crossing installations and all points in the remaining distance covered by the MA up to the first signal shall receive a TSR of 20 km/h. (LC)"
            },
            {
                "id": 161,
                "title": "",
                "description": "RBC 125 The failure of the EI-RBC connection must be signalled on both CMI and MMI. (LC/LC-EI)"
            },
            {
                "id": 162,
                "title": "",
                "description": "NOTE 27 The signals in the stations shall be passed by calling or traffic order and by activating the OVR button (I)"
            },
            {
                "id": 163,
                "title": "",
                "description": "NOTE 28 The block signals shall be passed by activating the OVR button (I)."
            },
            {
                "id": 164,
                "title": "",
                "description": "RBC 126 If the RBC and the EIL are not synchronised, the RBC must not send an MA to any OBU. (LC)"
            },
            {
                "id": 165,
                "title": "",
                "description": "RBC 127 Any time difference higher than or equal to 5 seconds shall be considered to be a loss of synchronisation. (LC)"
            },
            {
                "id": 166,
                "title": "",
                "description": "RBC 128 A synchronisation procedure must be implemented for the situations when the RBC and the EI are not synchronised. (LC)"
            },
            {
                "id": 167,
                "title": "",
                "description": "RBC 129 Each communication with each OBU shall be handled individually. (LC)"
            },
            {
                "id": 168,
                "title": "",
                "description": "RBC 130 If the communication has failed, the RBC must consider the communication re-established when it receives a new position report from the OBU. (LC)"
            },
            {
                "id": 169,
                "title": "",
                "description": "RBC 131 When the communication with the OBU has been re-established, the RBC must send a new MA only if new elements appear (if the OBU has already requested an MA extension and a new route has been set up in the EI installation). (LC)"
            },
            {
                "id": 170,
                "title": "",
                "description": "RBC 132 When all requirements for train movement (known location of train, route set and locked) are met, the RBC must issue an MA in Full Supervision (FS) mode. (LC)"
            },
            {
                "id": 171,
                "title": "",
                "description": "RBC 133 The conditions for MA FS must be continuously supervised. (LC)"
            },
            {
                "id": 172,
                "title": "",
                "description": "RBC 134 The RBC must, when necessary, intervene with adequate actions, e.g. by issuing an emergency stop message, if the conditions for train movement are no longer met. (LC)"
            },
            {
                "id": 173,
                "title": "",
                "description": "RBC 135 The OS MA must be issued by the RBC only if the train position and running direction are known and if the route is set and locked. Also, the train must be in its own area or in the announcement / transition area. (LC)"
            },
            {
                "id": 174,
                "title": "",
                "description": "RBC 136 The conditions for TAF are defined in chapter “Track ahead free (TAF)”. (LC)"
            },
            {
                "id": 175,
                "title": "",
                "description": "RBC 137The distance from where the driver may provide confirmation for OS mode is 200 m before the signal. (LC)"
            },
            {
                "id": 176,
                "title": "",
                "description": "RBC 138 OS MA confirmation must be requested from the driver irrespective of the OBU mode at the time of receipt of the OS MA (OBU may be in FS, OS or SR when it receives OS MA) (LC)."
            },
            {
                "id": 177,
                "title": "",
                "description": "RBC 139 The distance indicated for the Staff Responsible (SR) mode must be a national value. (LC)"
            },
            {
                "id": 178,
                "title": "",
                "description": "RBC 140 The RBC must display to the controller via the CMI that the OBU is running in SR mode. (LC)"
            },
            {
                "id": 179,
                "title": "",
                "description": "NOTE 29. While it is running in SR mode, the OBU must report its position to the RBC, as predefined (e.g. every 5 seconds). This is necessary especially if a STOP signal has been passed and the next signal is set to “CLEAR”, so that it may be possible or OBU to receive from RBC a possible TAF request . (LC)"
            },
            {
                "id": 180,
                "title": "",
                "description": "RBC 141 The conditions for TAF are defined in chapter “Track Ahead Free (TAF)”. (LC)"
            },
            {
                "id": 181,
                "title": "",
                "description": "RBC 142 All traffic signals shall be provided with a balise group “STOP if in SR”. This balise group shall be positioned at the signal. For back-to-back signals the same balise group will be valid for both running directions. (LC)"
            },
            {
                "id": 182,
                "title": "",
                "description": "RBC 143 Requirements for the issuance of a TAF by the RBC (LC): OBU has a valid position. RBC can validate the position. The signal is set to “CLEAR” RBC is able to send an MA (OS or FS) OBU is in one of the modes SB, OS or SR. The front of the train has not passed the signal"
            },
            {
                "id": 183,
                "title": "",
                "description": "RBC 144 The RBC shall issue the TAF request, which shall be displayed on the DMI when the OBU is located in the TAF window (starting from 200 m before the signal). A balise group shall be placed at this distance. The same balise group shall also have the function of resetting the errors accumulated on board the engine. (LC)"
            },
            {
                "id": 184,
                "title": "",
                "description": "RBC 145 When the TAF is acknowledged by the train driver, the RBC will issue an MA up to the signal, followed by an MA issued according to the signal indication / state. (LC)"
            },
            {
                "id": 185,
                "title": "",
                "description": "RBC 146 The controller must be able to enter and revoke a TSR, via the CMI. (LC)"
            },
            {
                "id": 186,
                "title": "",
                "description": "RBC 147 It is allowed to introduce a TSR even if MAs are set over the respective area or even if there are occupied sections in that area. (LC)"
            },
            {
                "id": 187,
                "title": "",
                "description": "RBC 148 It must be possible to specify at least the following for the TSR (LC): Maximum speed value TRS limits (start / end) Text messages associated to the TSR (automatically sending a text message with the TSR, in order to inform the driver). The text message will be: “Speed restriction”. This message will be transmitted when the OBU is at a distance of 1000 m from the TSR. This is a message without confirmation."
            },
            {
                "id": 188,
                "title": "",
                "description": "RBC 149 The RBC must check and validate the TSR entered by the controller (from the point of view of plausibility). (LC)"
            },
            {
                "id": 189,
                "title": "",
                "description": "RBC 150 Entering/removing a TSR must be immediately taken into account by the system. It must also be immediately transmitted to the OBU (existing MAs must be updated). (LC)"
            },
            {
                "id": 190,
                "title": "",
                "description": "RBC 151 It must be possible to define the TSR limits (LC): either through the track section identification or through the track position (every 10 m)"
            },
            {
                "id": 191,
                "title": "",
                "description": "RBC 152 The RBC must allow the revocation (cancellation) of a TSR by the Controller. (LC)"
            },
            {
                "id": 192,
                "title": "",
                "description": "RBC 153 It must be possible to individually set/activate and cancel each TSR individually. (LC)"
            },
            {
                "id": 193,
                "title": "",
                "description": "RBC 154 It must be possible to set a TSR with any value, with a resolution of 5 km/h. (LC)"
            },
            {
                "id": 194,
                "title": "",
                "description": "RBC 155 It must be possible to have overlapping TSRs. (LC)"
            },
            {
                "id": 195,
                "title": "",
                "description": "RBC 156 Each TSR must be distinctly displayed on the CMI. At the controller’s request, its geographical limits will be displayed. (LC)"
            },
            {
                "id": 196,
                "title": "",
                "description": "RBC 157 If 2 or more TSRs overlap on one section, the CMI shall indicate the lowest value, referring to speed indications. (LC)"
            },
            {
                "id": 197,
                "title": "",
                "description": "RBC 158 If 2 or more TSRs overlap, the cancellation of one restriction must not lead to the annulment of another TSR. (LC)"
            },
            {
                "id": 198,
                "title": "",
                "description": "RBC 159 The corresponding TSR speed must be indicated at the controller’s request. (LC)"
            },
            {
                "id": 199,
                "title": "",
                "description": "RBC 160 In case of RBC reset, the registered TSRs must not be deleted or lost. (LC)"
            },
            {
                "id": 200,
                "title": "",
                "description": "RBC 161 The definition and display of TSR shall be done in accordance with the CFR catalogue for CMI. The catalogue shall be sent when the contract is signed, as it is currently being completed. This catalogue is unique for all ETCS level 2 implementations at CFR. (LC)"
            },
            {
                "id": 201,
                "title": "",
                "description": "RBC 162 For an OBU in SR mode, TSR must always be sent if the OBU is on the line block. In the station, the TSR shall be transmitted only in association with an MA. (LC)"
            },
            {
                "id": 202,
                "title": "",
                "description": "RBC 163 TSR given must be accurate and actual, under traffic safety conditions. The Contractor must match special and actual kilometres. All data necessary for this matching shall be the responsibility of the Contractor. (LC)"
            },
            {
                "id": 203,
                "title": "",
                "description": "RBC 164 The RBC must be able to issue a TSR associated to a malfunctioning level crossing installation (LCI) (when it receives this information from the EI installation). See also the chapter “Signal set to STOP due to malfunctioning level crossing installation”. (LC)"
            },
            {
                "id": 204,
                "title": "",
                "description": "RBC 165 The RBC must be able to revoke the TSR LCI when receiving information regarding the normal operation of the previously malfunctioning LCI. (LC)"
            },
            {
                "id": 205,
                "title": "",
                "description": "RBC 166 The issuance (or revoking) of a TSR LCI must be followed by (LC): the issuance of a new MA (containing the new TSR), with the same EoA, OR the sending of only the TSR to the OBU to be integrated in the OBU MA for each OBU which already has an MA over the malfunctioning LCI in question. Simultaneously, a text message shall be sent indicating the reason for this TSR (“Malfunctioning level crossing, km xxx+yyy”)."
            },
            {
                "id": 206,
                "title": "",
                "description": "RBC 167 The RBC must not wait until the trains in question request a new MA – the new MA or just the TSR is issued as soon as the TSR LCI has been issued by the RBC. (LC)"
            },
            {
                "id": 207,
                "title": "",
                "description": "NOTE 30. The end of mission must be reported to the RBC through the “End of Mission” message."
            },
            {
                "id": 208,
                "title": "",
                "description": "RBC 168 The “End of mission” procedure must be executed in accordance with the “TSI CCS Annex A” document, plus the requirements in the hereby document. (LC)"
            },
            {
                "id": 209,
                "title": "",
                "description": "RBC 169 The train number and data must be removed from the controller’s display when deregistration is complete. (LC)"
            },
            {
                "id": 210,
                "title": "",
                "description": "RBC 170 Shunting movements are not executed under the control of the RBC. (LC) NOTE 31 In order to enter SH mode, the driver shall request RBC permission. (I)"
            },
            {
                "id": 211,
                "title": "",
                "description": "RBC 171 The RBC shall not prevent a train to leave its area while in SH mode. (LC)"
            },
            {
                "id": 212,
                "title": "",
                "description": "RBC 172 When receiving the request from an OBU, the RBC must transmit the permission to shunt to this OBU. (LC)"
            },
            {
                "id": 213,
                "title": "",
                "description": "RBC 173 No list of balises will be transmitted to the OBU. (LC)"
            },
            {
                "id": 214,
                "title": "",
                "description": "NOTE 32 After receiving the permission, the OBU will enter SH mode. (LC)"
            },
            {
                "id": 215,
                "title": "",
                "description": "RBC 174 No permanent shunting areas are used. (LC)"
            },
            {
                "id": 216,
                "title": "",
                "description": "NOTE 33 Shunting movements must not be allowed for an OBU, until it has received permission from the RBC / until it is in SH mode. (LC)"
            },
            {
                "id": 217,
                "title": "",
                "description": "RBC 175 Shunting routes must not be registered in the RBC. (LC)"
            },
            {
                "id": 218,
                "title": "",
                "description": "RBC 176 The OBU must allow entry in SH mode only when the OBU is not moving. (LC)"
            },
            {
                "id": 219,
                "title": "",
                "description": "NOTE 34 In order to exit SH mode, the driver must select “exit shunting”. This action must switch the OBU to Stand By mode. (I)"
            },
            {
                "id": 220,
                "title": "",
                "description": "RBC 177 The neutral sections must be indicated in the route configuration. (LC)"
            },
            {
                "id": 221,
                "title": "",
                "description": "RBC 178 The RBC must transmit to the OBU the indication of where the driver must turn the main power switch off/on."
            },
            {
                "id": 222,
                "title": "",
                "description": "RBC 179 The issued MAs must also take into account the following (LC): a) The RBC shall transmit the “track conditions” pack with information regarding the neutral section. b) The minimum distance between the location for transmitting the neutral section state and the beginning of the neutral section is calculated using the formula: D = Vline [m/s] / 11 [s] c) The pack shall comprise the mandatory disconnection order for the main power switch. d) The length indicated in the pack will be calculated separately for each case, with the formula: L =neutral section length + 40 [m]."
            },
            {
                "id": 223,
                "title": "",
                "description": "RBC 180 The RBC must be able to store text messages issued to the OBUs located in its area of responsibility. (LC)"
            },
            {
                "id": 224,
                "title": "",
                "description": "RBC 181. Only text messages from the moment of OBU registration in the corresponding RBC are taken into account. (LC)"
            },
            {
                "id": 225,
                "title": "",
                "description": "RBC 182 RBC must be able to work with fixed lengths of block/track sections for train separation. (LC)"
            },
            {
                "id": 226,
                "title": "",
                "description": "RBC 183 In order to indicate traffic on the left track of the double line provided with reversible ABS/IABS, the RBC shall transmit a text message with confirmation. The text is “Exit on the left”. If the driver does not confirm the message, the service brake shall be activated. (LC)"
            },
            {
                "id": 227,
                "title": "",
                "description": "RBC 184 The RBC shall transmit a text message without confirmation for the direction indicator. The test is “Direction” followed by the name of the locality. (LC)"
            },
            {
                "id": 228,
                "title": "",
                "description": "RBC 185 The RBC must be able to send an emergency stop message (conditional and unconditional) to the OBU, based on status of the routes/the EI installation information. (LC)"
            },
            {
                "id": 229,
                "title": "",
                "description": "RBC 186 The issuance of an emergency stop message must be possible at any time. (LC)"
            },
            {
                "id": 230,
                "title": "",
                "description": "RBC 187 The RBC must send an emergency stop message to an OBU until a confirmation is received from the OBU. The confirmation refers to the fact that the message has reached the OBU, not to the fact that the driver has confirmed the message. (LC)"
            },
            {
                "id": 231,
                "title": "",
                "description": "RBC 188 The emergency stop message must be revoked in order for the RBC to be able to issue a new MA to the OBU in question. (LC)"
            },
            {
                "id": 232,
                "title": "",
                "description": "RBC 189 The consequences (mode change, shortening of an MA) of each emergency stop message for each OBU must be indicated on the RBC-CMI. (LC)"
            },
            {
                "id": 233,
                "title": "",
                "description": "NOTE 35. These operations shall be performed in SH mode. They are outside the scope of the RBC. (I)"
            },
            {
                "id": 234,
                "title": "",
                "description": "RBC 190 The RBC must support the management of security keys. (LC)"
            },
            {
                "id": 235,
                "title": "",
                "description": "RBC 191 The RBC must ensure that the keys are stored in a secure and confidential manner. Retrieving the secret keys installed in the RBC must be impossible (to unauthorised personnel). (LC)"
            },
            {
                "id": 236,
                "title": "",
                "description": "RBC 192 The RBC must ensure the use of the transport keys for the protection of the authentication keys (KMAC). (LC)"
            },
            {
                "id": 237,
                "title": "",
                "description": "RBC 193 The RBC must be able to store up to 5000 KMAC keys. (LC)"
            },
            {
                "id": 238,
                "title": "",
                "description": "RBC 194 The RBC must ensure a secure procedure for the installation of transport keys. (LC)"
            },
            {
                "id": 239,
                "title": "",
                "description": "RBC 195 The RBC must ensure the installation and deletion of keys without an interruption of operation (i.e. without RBC restart or reboot). (LC)"
            },
            {
                "id": 240,
                "title": "",
                "description": "RBC 196 The keys stored in the RBC must not be lost in case of power outage. (LC)"
            },
            {
                "id": 241,
                "title": "",
                "description": "RBC 197 The RBC must allow different key management policies (e.g. all trains/one train – one key). (LC)"
            },
            {
                "id": 242,
                "title": "",
                "description": "RBC 198 The session keys generated by the RBC must be strong, from a cryptographic point of view, as specified in the UNISUG documents. (LC)"
            },
            {
                "id": 243,
                "title": "",
                "description": "NOTE 36 It shall be considered for the purposes of this project that the classic signals remain installed in the field. In this case, most EoAs are placed near a signal. (I)"
            },
            {
                "id": 244,
                "title": "",
                "description": "NOTE 37 There are two main types of traffic signals -“absolute stop” signals and “permissive stop” signals. (I)"
            },
            {
                "id": 245,
                "title": "",
                "description": "NOTE 38 When a train approaches the EoA, it requests, at a certain distance, an MA extension from the RBC. If the extension is not granted, the train stops."
            },
            {
                "id": 246,
                "title": "",
                "description": "(I)"
            },
            {
                "id": 247,
                "title": "",
                "description": "NOTE 39 A train may pass an EoA (LC): if it receives a new MA (EoA is “transferred”) OR by performing the EoA passing procedure."
            },
            {
                "id": 248,
                "title": "",
                "description": "NOTE 40 According to national rules, passing an EoA associated with an “absolute stop” signal is permitted: if the signal displays the “calling” indication OR with a written (traffic) order"
            },
            {
                "id": 249,
                "title": "",
                "description": "NOTE 41 There are two main types of calling indications –CH1 - “calling with locked route” (the route is set and locked behind the signal), CH2/CH3 “calling without locked route” (the route is not locked or set behind the signal). Only the CH1 calling shall be sent to RBC. (I/LC-EI)"
            },
            {
                "id": 250,
                "title": "",
                "description": "NOTE 42 The EI installation shall send to the RBC the commanded information, and not the indication displayed by the signal. Because of this, it is possible that the indication displayed by a signal does not correspond to the message received from the RBC. In this case, the RBC message has priority. This condition is valid for the signal indicating “permissive stop”. (I/LC-EI)"
            },
            {
                "id": 251,
                "title": "",
                "description": "NOTE 43 The EI installation must be able to identify the exact cause or combination of causes leading to the passing of a block signal set to “STOP” and to provide all the necessary data to the RBC. (I/LC-EI)"
            },
            {
                "id": 252,
                "title": "",
                "description": "NOTE 44. In order to comply with CFR rules, the driver must stop in front of the signal and/or a level crossing, and then continue running, even if the train has an MA. This matter will settled by national operational rules and it is not the object of the system to be implemented. (I)"
            },
            {
                "id": 253,
                "title": "",
                "description": "RBC 199 The RBC must issue a new MA FS, practically identical with the previous one, but additionally containing a text message indicating to the driver that they are allowed to pass the signal displaying the STOP indication due to burnt lamps at permissive signal lights. It is also allowed to send only one text message to the OBU (the previously described message), without issuing a new MA. The text message shall be displayed on the DMI, 600 m or closer to the signal and shall not require confirmation. The message shall read “Malfunctioning signal”. This message shall disappear when the train’s front end passes the signal. (LC)"
            },
            {
                "id": 254,
                "title": "",
                "description": "RBC 200 When it receives from the EI installation the information regarding the “malfunctioning LCI”, the RBC must immediately issue a special TSR-LCI over the level crossing area. See also the chapter “Temporary Speed Restriction associated to a level crossing installation”. (LC)"
            },
            {
                "id": 255,
                "title": "",
                "description": "RBC 201 After issuing the TSR-LCI, the RBC must (LC): • either issue a new MA for each train that already has an MA over the malfunctioning LCI (different from the usual TSRs, which do not require the issuance of a new MA) – see also “TSR status change” • or just send a new TSR to each OBU, with each OBU being able to integrate it in the current MA."
            },
            {
                "id": 256,
                "title": "",
                "description": "RBC 202 The RBC must also send an initial text message to the OBU, informing the driver about “Malfunctioning level crossing installation, km. xxx+yyy”. (LC)"
            },
            {
                "id": 257,
                "title": "",
                "description": "I. This message shall be sent to the OBU as follows:"
            },
            {
                "id": 258,
                "title": "",
                "description": "a) If the OBU has an MA over the level crossing, the RBC sends the message when the level crossing installation malfunctions."
            },
            {
                "id": 259,
                "title": "",
                "description": "b) If the OBU does not yet have an MA over the malfunctioning LCI, the text message must be sent along with the MA, at the same time with the issuance of the MA over the level crossing."
            },
            {
                "id": 260,
                "title": "",
                "description": "II. The display of the message on DMI shall be as follows:"
            },
            {
                "id": 261,
                "title": "",
                "description": "a) The text message shall be displayed on the DMI at 600 m or closer to the signal and shall be without confirmation. The message shall be “Malfunctioning level crossing, km xxx+yyy”. The message shall disappear from the DMI at the time when the OBU (with “front end”) passes the signal"
            },
            {
                "id": 262,
                "title": "",
                "description": "b) If OBU is after the block signal that covers the level crossing installation, the message shall be displayed instantly."
            },
            {
                "id": 263,
                "title": "",
                "description": "RBC 203 This initial text message shall be without confirmation (LC)"
            },
            {
                "id": 264,
                "title": "",
                "description": "RBC 204 The RBC must send a new text message, with identical syntax as the one of the initial signal (“Malfunctioning level crossing installation, km xxx+yyy”, 50 m before the level crossing, in order to warn the driver. This shall be a text message with confirmation. If the driver does not confirm the message, service braking shall be triggered (LC)"
            },
            {
                "id": 265,
                "title": "",
                "description": "RBC 205 If the LCI malfunction occurs when the OBU is at a distance shorter than 50 m from it, only the initial message shall be sent, without confirmation. (LC)"
            },
            {
                "id": 266,
                "title": "",
                "description": "RBC 206. The initial message and the 50 m message must be sent to the OBU regardless of the running mode (FS, OS, SR) (LC)."
            },
            {
                "id": 267,
                "title": "",
                "description": "RBC 207 The TSR length must be of 50 m plus the passage width. The beginning of the TSR must be 50 m before the passage, in the running direction. This means that the position of TSRs allocated to level crossings depends on the direction from which the OBU approaches the level crossing. (LC)"
            },
            {
                "id": 268,
                "title": "",
                "description": "NOTE 45 The issuance of a new MA or of the TSR-LCI may trigger emergency braking. (I)"
            },
            {
                "id": 269,
                "title": "",
                "description": "NOTE 46. The OBU must accept this MA / comply with the TSR LCI. Acceptance is mandatory, not conditional. (I)"
            },
            {
                "id": 270,
                "title": "",
                "description": "NOTE 208 The TCAF function in the EI installation shall be activated independently ON EACH TRACK. Therefore, it must be taken into account that it is possible, from the RBC point of view, for the same level crossing to be considered as malfunctioning on one track (the one with TCAF active) and completely functional on the other. (LC)"
            },
            {
                "id": 271,
                "title": "",
                "description": "RBC 209 In predefined locations (200m to the next signal), the RBC must send a TAF request to the OBU which is in OS or SR mode. (LC)"
            },
            {
                "id": 272,
                "title": "",
                "description": "RBC 210 If the TMCO has set the block signal to “STOP”, the RBC shall not issue an MA. The signal shall be passed using the OVERRIDE. (LC)"
            },
            {
                "id": 273,
                "title": "",
                "description": "RBC 211 If a block signal is set to “STOP” due to the reverse block orientation, the RBC shall not issue an MA (for this signal). The signal shall be passed using the OVERRIDE. (LC)"
            },
            {
                "id": 274,
                "title": "",
                "description": "RBC 212 If a block signal is set to “STOP” due to the failure of the interface between the 2 stations (the IABS case), the RBC shall not issue an MA (for this signal). The signal shall be passed using OVERRIDE. (LC)"
            },
            {
                "id": 275,
                "title": "",
                "description": "RBC 213 The RBC must issue a new MA FS, practically identical to the previous one, but which in addition contains a text message indicating to the driver the fact that they are permitted to pass the signal displaying the “STOP” indication due to the burnt lamps at the permissive lights. It is also possible to send only one text message to the OBU (message described previously), without the issuance of a new MA, The text message shall be displayed on the DMI at 600 m (if the lamps were burnt before) or closer (if the lamps are bunt when the train is at a distance of less than 600 m) from the signal and shall be without confirmation. The message shall be “Malfunctioning signal”. The message shall disappear from the DMI when the OBU’s front end passes the signal. (LC)"
            },
            {
                "id": 276,
                "title": "",
                "description": "RBC 214 If a block signal is set to “STOP” due to EI failure or EI – RBC communication failure, the RBC shall not issue an MA (for this signal). The signal shall be passed using OVERRIDE. (LC)"
            },
            {
                "id": 277,
                "title": "",
                "description": "RBC 215 In case of mixed situations, the RBC must take the most restrictive decision (most restrictive MA must be issued). (LC)"
            },
            {
                "id": 278,
                "title": "",
                "description": "RBC 216 In case of mixed situations, corresponding messages shall be sent for each individual situation."
            },
            {
                "id": 279,
                "title": "",
                "description": "RBC 217 The RBC must not issue an MA for (LC): a signal set to “STOP” displaying the “calling without locked route” a signal set to “STOP” that does not display the “calling” indication. This requirement shall be valid even when the signal is set to “STOP” because of burnt lamps."
            },
            {
                "id": 280,
                "title": "",
                "description": "RBC 218 The RBC must issue an MA OS for a signal set to “STOP” displaying a calling with locked route. (LC)"
            },
            {
                "id": 281,
                "title": "",
                "description": "RBC 219 If an LCI malfunctions after an MA was issued over it, the MA in question must be revoked / annulled. Unlocking the route must follow the requirements in this document. (LC)"
            },
            {
                "id": 282,
                "title": "",
                "description": "RBC 220 The principles and manner of decommissioning the automatic block (integrated or not), as specified in the CFR document 2/4/284/12.12.2012, must be complied with. (LC)"
            },
            {
                "id": 283,
                "title": "",
                "description": "RBC 221 After activating AFBL, the RBC will issue for all block signals MA OS corresponding to the static speed profile, but without exceeding 100 km/h. (LC)"
            },
            {
                "id": 284,
                "title": "",
                "description": "NOTE 47. A traffic order shall be issued which may contain, depending on the particular situations, speeds lower than SSP. Also, the traffic order shall specify the “PROCEED” light signals whose indications are not complied with, according to the current instructions in force. This is an operational procedure and does not have any impact on functionality. (I)"
            },
            {
                "id": 285,
                "title": "",
                "description": "RBC 222 The system must allow the registration of information regarding the malfunctioning / missing balise groups. (LC)"
            },
            {
                "id": 286,
                "title": "",
                "description": "NOTE 48.This information is transmitted by the OBU. (I)"
            },
            {
                "id": 287,
                "title": "",
                "description": "RBC 223 If a train sends the information regarding missing / malfunctioning balises, this information must be displayed on the CMI. (LC)"
            },
            {
                "id": 288,
                "title": "",
                "description": "RBC 224 The Contractor must present in its tender a quoted maintenance contract (per year). (M)"
            },
            {
                "id": 289,
                "title": "",
                "description": "RBC 225 The maintenance concept must include functions supporting the following (LC):"
            },
            {
                "id": 290,
                "title": "",
                "description": "Preventive maintenance"
            },
            {
                "id": 291,
                "title": "",
                "description": "Corrective maintenance"
            },
            {
                "id": 292,
                "title": "",
                "description": "System monitoring"
            },
            {
                "id": 293,
                "title": "",
                "description": "Maintenance data recording"
            },
            {
                "id": 294,
                "title": "",
                "description": "Legal data recording"
            },
            {
                "id": 295,
                "title": "",
                "description": "RBC 226 The Tenderer must include in the tender system operation and maintenance training courses for the CFR personnel. The training courses must be distinct for the operating personnel and the maintenance personnel. The courses must be subject to different quotations. (M)"
            },
            {
                "id": 296,
                "title": "",
                "description": "RBC 227 At least 2 instructors, 2 district managers, 1 head of section must be trained in the “Train the trainers” program. Also, 10 electro-mechanics must be trained. 10 persons from CFR Headquarters must be trained. (LC)"
            },
            {
                "id": 297,
                "title": "",
                "description": "NOTE 49. The personnel are the same personnel, trained for the interlocking installations. (LC)"
            },
            {
                "id": 298,
                "title": "",
                "description": "RBC 228 For this project, data preparation for the RBC route layout must be the responsibility of the Contractor. (LC)"
            },
            {
                "id": 299,
                "title": "",
                "description": "RBC 229 Data preparation (as a specific application) shall consist of at least the establishment of fixed data for the route configuration, including (LC): infrastructure data profiles route conditions and dependencies"
            },
            {
                "id": 300,
                "title": "",
                "description": "RBC 230 The RBC manufacturer must provide all necessary information regarding preventive maintenance measures for the RBC equipment, as well as inspection intervals, sustainability of hardware components, procurement of spare parts, etc. (LC)"
            },
            {
                "id": 301,
                "title": "",
                "description": "RBC 231The diagnosis function must assist the maintenance staff in identifying the malfunctioning units, when failure has occurred. (LC)"
            },
            {
                "id": 302,
                "title": "",
                "description": "RBC 232 The diagnosis function must assist the maintenance staff in filtering the diagnosis messages according to type and date. (LC)"
            },
            {
                "id": 303,
                "title": "",
                "description": "RBC 233 The diagnosis function must be able to export diagnosis data locally and to a remote server. (LC)"
            },
            {
                "id": 304,
                "title": "",
                "description": "RBC 234 The RBC must be provided with a set of self-testing functions. These functions must include a system test at start-up, as well as online tests during operation. (LC)"
            },
            {
                "id": 305,
                "title": "",
                "description": "RBC 235 The RBC must provide status and diagnosis messages to the RBC maintenance staff, with a view to the analysis of malfunctions of RBC components and interfaces. Every RBC hardware item relevant for repair or replacement must be taken into account. Temporary malfunctions and permanent failures must be highlighted in order to assist the maintenance personnel. (LC)"
            },
            {
                "id": 306,
                "title": "",
                "description": "RBC 236 After RBC start-up (e.g., after a repair is completed), a completely automatic self-test must ensure the safe RBC operation. (LC)"
            },
            {
                "id": 307,
                "title": "",
                "description": "RBC 237 The maintenance of the ETCS trackside equipment and the GSM-R equipment must be supported by the diagnosis of (LC): failures at balise groups (reading errors), reported by the OBU GSM-R failures, frequency and location of connection interruption"
            },
            {
                "id": 308,
                "title": "",
                "description": "RBC 238 All messages sent by the RBC must be documented in a maintenance manual, along with their detailed descriptions and required actions. (LC)"
            },
            {
                "id": 309,
                "title": "",
                "description": "RBC 239 Critical diagnosis messages must be displayed and accompanied by an acoustic alarm. (LC)"
            },
            {
                "id": 310,
                "title": "",
                "description": "RBC 240 The confirmation of an acoustic alarm must stop the acoustic alarm. (LC)"
            },
            {
                "id": 311,
                "title": "",
                "description": "RBC 241 When the conditions leading to the triggering of an alarm are no longer valid, the status of the alarm must change until the controller’s confirmation, when it is removed from the display. (LC)"
            },
            {
                "id": 312,
                "title": "",
                "description": "RBC 242 The maintenance function must include sub-functions for indicating detailed information regarding the system and real-time status. The Contractor must submit to CFR a proposal for a maintenance tool. (LC)"
            },
            {
                "id": 313,
                "title": "",
                "description": "RBC 243 The RBC must include a function for recording legal data and data needed for system diagnosis. (LC)"
            },
            {
                "id": 314,
                "title": "",
                "description": "RBC 244 The recording function must store at least the following data:"
            },
            {
                "id": 315,
                "title": "",
                "description": "Indications displayed on the operator interface"
            },
            {
                "id": 316,
                "title": "",
                "description": "Commands entered via the operator interface"
            },
            {
                "id": 317,
                "title": "",
                "description": "Telegrams exchanged between the trains and the RBC"
            },
            {
                "id": 318,
                "title": "",
                "description": "Data exchanged over other RBC interfaces (with the EI installations, etc.)"
            },
            {
                "id": 319,
                "title": "",
                "description": "Internal status and system variables"
            },
            {
                "id": 320,
                "title": "",
                "description": "Legal recorder users (internal subsystems and/or operator)"
            },
            {
                "id": 321,
                "title": "",
                "description": "RBC 245 All stored data must have a time and a date. (LC)"
            },
            {
                "id": 322,
                "title": "",
                "description": "RBC 246 The recorded data must be stored for at least six month. (LC)"
            },
            {
                "id": 323,
                "title": "",
                "description": "RBC 247 The RBC must store all legal data in a secure manner so that possible data handling and/or data errors may be detected. (LC)"
            },
            {
                "id": 324,
                "title": "",
                "description": "RBC 248 The “recording function” maintenance tool must include recorded data analysis functions, which allow the recorded data to be filtered for the purposes of an efficient data evaluation for diagnosis and legal purposes. (LC)"
            },
            {
                "id": 325,
                "title": "",
                "description": "RBC 249 The analysis tool must support at least the following (LC):"
            },
            {
                "id": 326,
                "title": "",
                "description": "Displaying specific data from the legal recorder"
            },
            {
                "id": 327,
                "title": "",
                "description": "Downloading data from the legal recorder"
            },
            {
                "id": 328,
                "title": "",
                "description": "RBC 250 The information must be easily understandable, adequate, and clear, so that the user may understand the tasks under his/her responsibility. (LC)"
            },
            {
                "id": 329,
                "title": "",
                "description": "RBC 251 The CMI must be (physically) different from the MMI for the EI or CTC installations. (LC)"
            },
            {
                "id": 330,
                "title": "",
                "description": "RBC 252 All text information displayed on the CMI must be in Romanian language. (LC)"
            },
            {
                "id": 331,
                "title": "",
                "description": "RBC 253 Every user data input must trigger an acoustic and/or visual reaction in order to confirm that the action has been correctly recognised. (LC)"
            },
            {
                "id": 332,
                "title": "",
                "description": "RBC 254 During the detailed design, it must be possible to select the types of sounds to be used, as well as when these are used. (LC)"
            },
            {
                "id": 333,
                "title": "",
                "description": "RBC 255 Information requiring the user’s attention must be presented in such a manner as to alert the user of the situation. (LC)"
            },
            {
                "id": 334,
                "title": "",
                "description": "RBC 256 Critical messages must have a visual and an acoustic component. (LC)"
            },
            {
                "id": 335,
                "title": "",
                "description": "RBC 257 The user must be able to recognise the system status and the supervision status at a glance. (LC)"
            },
            {
                "id": 336,
                "title": "",
                "description": "RBC 258 The user must easily identify if the display is “frozen”. The entire chain from the object to the route layout must be supervised. (LC)"
            },
            {
                "id": 337,
                "title": "",
                "description": "RBC 259 The RBC must indicate to the user that it is “busy” (working), if the result of the user’s action cannot be immediately displayed. (LC)"
            },
            {
                "id": 338,
                "title": "",
                "description": "RBC 260 A “ready” indication must be displayed on screen only when the action requested by the RBC from the user has been performed. (LC)"
            },
            {
                "id": 339,
                "title": "",
                "description": "RBC 261The confirmation request must be clearly indicated to the user. (LC)"
            },
            {
                "id": 340,
                "title": "",
                "description": "RBC 262 The CMI must provide ways for confirmation. (LC)"
            },
            {
                "id": 341,
                "title": "",
                "description": "RBC 263 The CMI must provide ways for consulting and entering data. These must be easily understandable for the user. (LC)"
            },
            {
                "id": 342,
                "title": "",
                "description": "RBC 264 The acoustic unit must be able to produce a variety of sounds. (LC)"
            },
            {
                "id": 343,
                "title": "",
                "description": "RBC 265 The user must be able to adjust the sound volume level. (LC)"
            },
            {
                "id": 344,
                "title": "",
                "description": "RBC 266 The different sounds must be easily distinguishable and recognised by the user. (LC)"
            },
            {
                "id": 345,
                "title": "",
                "description": "RBC 267 The CMI must display the operational area, which the controller has under its command. (LC)"
            },
            {
                "id": 346,
                "title": "",
                "description": "RBC 268 All trains under RBC supervision must be displayed on the line layout, as well as in a table with the identification of the train supervision status. (LC)"
            },
            {
                "id": 347,
                "title": "",
                "description": "RBC 269 The MA sent to the train must be displayed on the line layout. (LC)"
            },
            {
                "id": 348,
                "title": "",
                "description": "RBC 270 The MA must be permanently displayed in graphic form and in table form, at the controller’s demand."
            },
            {
                "id": 349,
                "title": "",
                "description": "RBC 271 The RBC-related status indications must cover at least the following statuses (LC): Operational – fully operational Partially operational (2oo2 operation, one of the components is malfunctioning or offers results different from the other two)"
            },
            {
                "id": 350,
                "title": "",
                "description": "RBC 272 It must be possible to define the number and details related to the information displayed on the CMI. (LC)"
            },
            {
                "id": 351,
                "title": "",
                "description": "RBC 273: The controller shall be able to enter and remove TSRs, stop a certain train and approve or disapprove the RBC."
            },
            {
                "id": 352,
                "title": "",
                "description": "RBC 274 The maintenance engineer has unrestricted access to the RBC. (LC)"
            },
            {
                "id": 353,
                "title": "",
                "description": "RBC 275 The access of the maintenance staff to the line must be restricted to maintenance functions and must occur under the controller’s authority. (LC)"
            },
            {
                "id": 354,
                "title": "",
                "description": "RBC 276 A workstation must be equipped with graphic displays, keyboard and other equipment necessary for supporting the controller’s activity. (LC)"
            },
            {
                "id": 355,
                "title": "",
                "description": "RBC 277 The RBC must be capable of displaying when a train has received an emergency stop message (when the OBU sends this acknowledgement to the RBC). (LC)"
            },
            {
                "id": 356,
                "title": "",
                "description": "RBC 278 It must be possible to integrate different types of information (diagrams and texts) on one physical screen, including (LC):"
            },
            {
                "id": 357,
                "title": "",
                "description": "Overviews"
            },
            {
                "id": 358,
                "title": "",
                "description": "List of alarms"
            },
            {
                "id": 359,
                "title": "",
                "description": "RBC 279 The basic colours for displaying the object state must comply with national standards. It is allowed to use the symbol sets / basic colours from the EI installations. (LC)"
            },
            {
                "id": 360,
                "title": "",
                "description": "RBC 280 During the detailed design, it must be possible to select a model for symbols, colours and screen background for the route configuration. It is allowed to use the symbol sets/basic colours from the EI installations. (LC)"
            },
            {
                "id": 361,
                "title": "",
                "description": "RBC 281 It must be possible to represent an object by means of text. (LC)"
            },
            {
                "id": 362,
                "title": "",
                "description": "RBC 282 It must be possible to place an object anywhere in the line layout. (LC)"
            },
            {
                "id": 363,
                "title": "",
                "description": "RBC 283 During detailed design, it must be possible to define the commands available when selecting a specific object. (LC)"
            },
            {
                "id": 364,
                "title": "",
                "description": "RBC 284 The tracks and objects in the ERTMS area must be displayed on the CMI. (LC)"
            },
            {
                "id": 365,
                "title": "",
                "description": "RBC 285 The error messages must be displayed irrespective of whether the malfunctioning object is displayed on the screen at that time or not. (LC)"
            },
            {
                "id": 366,
                "title": "",
                "description": "RBC 286 The controller must be able to add and remove the texts for a track section, e.g. for identifying any vehicle on the respective track section. (LC)"
            },
            {
                "id": 367,
                "title": "",
                "description": "RBC 287 It must be possible to predefine user groups. (LC)"
            },
            {
                "id": 368,
                "title": "",
                "description": "RBC 288 Each user must be able to belong to several user groups. (LC)"
            },
            {
                "id": 369,
                "title": "",
                "description": "RBC 289 Each user group must be able to contain several users. (LC)"
            },
            {
                "id": 370,
                "title": "",
                "description": "RBC 290 The authorisation check must be performed as a login procedure, based on access codes and password. (LC)"
            },
            {
                "id": 371,
                "title": "",
                "description": "RBC 291 For each user group, it must be possible to define functions and information accessible by the respective user group. (LC)"
            },
            {
                "id": 372,
                "title": "",
                "description": "RBC 292 For each workstation, it must be possible to define user groups with authorisation to operate the respective workstation. (LC)"
            },
            {
                "id": 373,
                "title": "",
                "description": "RBC 293 For safety reasons, the user must not be permitted to modify display settings. (LC)"
            },
            {
                "id": 374,
                "title": "",
                "description": "RBC 294 A specific alarm and its status must be displayed on the monitor in a suitable manner. (LC)"
            },
            {
                "id": 375,
                "title": "",
                "description": "RBC 295 If an alarm is not assigned a certain position on the monitor, it must be displayed as a text message. (LC)"
            },
            {
                "id": 376,
                "title": "",
                "description": "RBC 296 All active alarms must be registered in an alarm list, which must be displayable upon request. (LC)"
            },
            {
                "id": 377,
                "title": "",
                "description": "RBC 297 In this project, special functions (such as TSR activation / deactivation) shall not be provided for portable devices. (LC)"
            },
            {
                "id": 378,
                "title": "",
                "description": "RBC 298 A verification of the telegram content issued by the RBC and the balises shall be performed as part of the ETCS level 2 acceptance tests. (LC)"
            },
            {
                "id": 379,
                "title": "",
                "description": "NOTE 50 CFR accepts one of the following procedures (a, b) for the telegram content verification. (I)"
            },
            {
                "id": 380,
                "title": "",
                "description": "RBC 299 Declaration of conformity (procedure a). As part of the acceptance tests, the Contractor shall not offer the technical means of actually reading the content of the telegram issued by the RBC or the balise, for any possible situation in the project. In this case, the Contractor must present, before the testing begins, the written documentation with the intended content of the telegrams, the plans and documents underlying the telegrams. (LC)"
            },
            {
                "id": 381,
                "title": "",
                "description": "RBC 300 Also, in this case, the Contractor must present a statement of responsibility specifying the technical impossibility to read the telegrams and for assuming responsibility to present the previously described documents as well as the written responsibility detailed below. (M) – if procedure a is chosen."
            },
            {
                "id": 382,
                "title": "",
                "description": "RBC 301 With this statement, the Contractor is made responsible for the correctness of the telegrams issued by the RBC and the balises, for storing the software free of charge if it results from system operation that the telegrams were not correctly written (including values for lengths, curbs, gradients and maximum speeds allowed, etc.), as well as for paying the resulting costs for any dysfunction in traffic due to issuing telegrams which are not in accordance with the documentation. (I)"
            },
            {
                "id": 383,
                "title": "",
                "description": "RBC 302 Declaration of conformity (procedure b). As part of the acceptance tests, the Contractor offers the technical means of actually reading the content of the telegrams issued by the RBC or the balise, for any situation in the project. In this situation, CFR does not require a statement of responsibility from the Contractor, but only a declaration guaranteeing the capability of actually reading the telegrams during testing. (M) – if procedure b is chosen."
            },
            {
                "id": 384,
                "title": "",
                "description": "RBC 303 The Contractor must include in the tender one of the statement described above – “The statement of responsibility” (procedure a) OR “The declaration of conformity” (procedure b). (M)"
            },
            {
                "id": 385,
                "title": "",
                "description": "The same MA FS, but accompanied by a text message indicating to the driver that passing a signal set to “STOP” is allowed without restrictions, because the signal’s lamps are burnt."
            },
            {
                "id": 386,
                "title": "",
                "description": "A modified MA FS, including a TSR corresponding to the LCI position, or only a TSR, which will be integrated in the existing MA shall be issued. Associated text messages shall be issued in accordance with the provisions in the hereby document."
            },
            {
                "id": 387,
                "title": "",
                "description": "A new MA FS is issued; it is shortened up to the signal displaying the “STOP” indication, followed by an MA OS over the occupied section."
            },
            {
                "id": 388,
                "title": "",
                "description": "No MA shall be issued. The signal shall be passed using OVERRIDE."
            },
            {
                "id": 389,
                "title": "",
                "description": "No MA shall be issued. The signal shall be passed using OVERRIDE."
            },
            {
                "id": 390,
                "title": "",
                "description": "No MA shall be issued. The signal will be passed with OVERRIDE."
            },
            {
                "id": 391,
                "title": "",
                "description": "No MA shall be issued. The signal shall be passed using OVERRIDE."
            },
            {
                "id": 392,
                "title": "",
                "description": "In the absence of information on the status of the signal from the EI installation, the RBC shall not issue an MA. The signal shall be passed using OVERRIDE."
            },
            {
                "id": 393,
                "title": "",
                "description": "MA OS shall be issued in accordance with the set route."
            },
            {
                "id": 394,
                "title": "",
                "description": "No MA shall be issued. The signal shall be passed using OVERRIDE, in compliance with the operational rules in force (traffic order)."
            },
            {
                "id": 395,
                "title": "",
                "description": "No MA shall be issued. The signal shall be passed using OVERRIDE, in compliance with the operational rules in force (traffic order)."
            },
            {
                "id": 396,
                "title": "",
                "description": "NOTE 1 The notes and requirements of this document are rated as follows: (I)  M – “Mandatory”. The fulfilment of the conformity requirement must be proven in the tender  LC – mandatory conformity requirement. The requirement must be complied with until the commissioning of the systems. It is not required to prove such fulfilment in the tender.   I - Informative"
            },
            {
                "id": 397,
                "title": "",
                "description": "NOTE 2 The LED light unit shall be abbreviated in this document as ULED. The incandescent light unit lamp shall be abbreviated in this document as ULI (I)"
            },
            {
                "id": 398,
                "title": "",
                "description": "LED 1 This document lays down the general, technical and operational safety requirements for the critical railway product: Light units with light emitting diodes (LED) for traffic and shunting light signals (I)"
            },
            {
                "id": 399,
                "title": "",
                "description": "NOTE 3 The light units with light emitting diodes (LED) described in this document shall be used for the fitting of traffic and shunting light signals of the electronic interlocking installations (EI) and integrated automatic block system (IABS) installations included in the new project. LED light units must ensure proper visibility for train traffic speeds of at least 160 km/h. (I)."
            },
            {
                "id": 400,
                "title": "",
                "description": "LED 2 In accordance with the Ministry of Transport Order (OMT) No 290/2000, as amended by OMT 2068/2004, ULED for traffic and shunting light signals must fall into the 1A risk class. (LC)."
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
