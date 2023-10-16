from spacy.language import Language
import spacy

from spacy.matcher import Matcher

from . import spaCy_rules


@Language.factory("check_requirement")
class CheckRequirement:

    def __init__(self, nlp, name, config):
        self.nlp = nlp
        self.name = name
        self.config = config

    def __call__(self, doc):
        matcher = Matcher(self.nlp.vocab)  # Init. the matcher with a vocab (note matcher vocab must share same vocab with docs)
        matcher.add('Passive', spaCy_rules.passive_voice_rules) 
        matcher.add('Active', spaCy_rules.active_voice_rules)
        matcher.add('Indefinite_Article', spaCy_rules.indefinite_article_rules)
        matcher.add('Slash', spaCy_rules.slash_rules)
        matches = matcher(doc)

        my_user_data = {}
        my_user_data ['Passive'] = False
        my_user_data ['Active'] = False
        my_user_data ['Indefinite_Article'] = False
        my_user_data ['Slash'] = False

        if len(matches) > 0:
            for match_id, start, end in matches:
                string_id = self.nlp.vocab.strings[match_id]
                #span = doc[start:end] # the matched span
                #print("\t{}: {}".format(string_id, span.text))
                my_user_data [string_id] = True

        doc.user_data = my_user_data
        return doc

    def getconfig(self):
        return self.config

    def getname(self):
        return self.name
