# usage: pytest check_requirement_test.py -rP

import pytest

import spacy

from check_requirement import CheckRequirement


class Test_CheckRequirement:

    def test_name(self):
        checker = CheckRequirement(nlp = "nlp", name = "n", config = "c")

        ret = checker.getname()
        assert "n" == ret

    def test_config(self):
        checker = CheckRequirement(nlp = "nlp", name = "n", config = "c")

        ret = checker.getconfig()
        assert "c" == ret
    
    def test_CheckRequirement(self):
        nlp = spacy.load("en_core_web_sm")
        label_map = {"GPE": "LOC"}
        nlp.add_pipe(
                    "check_requirement",
                    last=True,
                    config={"config": label_map}
                    )
        doc = nlp("We went into Yellowstone Park in Wyoming.")

        print(doc.user_data)
        assert "c" == "c"

