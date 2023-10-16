# usage: pytest check_requirement_test.py -rP

import pytest

import spacy

class Test_CheckRequirement:

    def test_CheckActive(self):
        nlp = spacy.load("en_core_web_lg")
        label_map = {"GPE": "LOC"}
        nlp.add_pipe(
                    "check_requirement",
                    last=True,
                    config={"config": label_map}
                    )
        doc = nlp("We went into Yellowstone Park in Wyoming.")

        print(doc.user_data)
        assert doc.user_data['Active'] == True and doc.user_data['Passive'] == False

    def test_CheckPassive(self):
        nlp = spacy.load("en_core_web_lg")
        label_map = {"GPE": "LOC"}
        nlp.add_pipe(
                    "check_requirement",
                    last=True,
                    config={"config": label_map}
                    )
        doc = nlp("She was sent a cheque for a thousand euros.")

        print(doc.user_data)
        assert doc.user_data['Active'] == False and doc.user_data['Passive'] == True

    def test_CheckRequirement(self):
        nlp = spacy.load("en_core_web_lg")
        label_map = {"GPE": "LOC"}
        nlp.add_pipe(
                    "check_requirement",
                    last=True,
                    config={"config": label_map}
                    )
        doc = nlp("She was sent a cheque for a thousand euros.")

        print(doc.user_data)
        assert doc.user_data['Indefinite_Article'] == True

    def test_CheckSlashUnit(self):
        nlp = spacy.load("en_core_web_lg")
        label_map = {"GPE": "LOC"}
        nlp.add_pipe(
                    "check_requirement",
                    last=True,
                    config={"config": label_map}
                    )
        doc = nlp("She drove per 20 km/h.")

        print(doc.user_data)
        assert doc.user_data['Slash'] == False

    def test_CheckSlash(self):
        nlp = spacy.load("en_core_web_lg")
        label_map = {"GPE": "LOC"}
        nlp.add_pipe(
                    "check_requirement",
                    last=True,
                    config={"config": label_map}
                    )
        doc = nlp("We want to do this and/or that.")

        print(doc.user_data)
        assert doc.user_data['Slash'] == True
