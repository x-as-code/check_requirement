from spacy.language import Language
import spacy

@Language.factory("check_requirement")
class CheckRequirement:

    def __init__(self, nlp, name, config):
        self.nlp = nlp
        self.name = name
        self.config = config

    def __call__(self, doc):
        my_user_data = {}
        my_user_data ['active'] = True
        doc.user_data = my_user_data
        return doc

    def getconfig(self):
        return self.config

    def getname(self):
        return self.name
