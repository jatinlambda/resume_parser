import spacy
import pickle
from spacy import displacy

with open ('outfile', 'rb') as fp:
    itemlist = pickle.load(fp)
    # print(itemlist)
    line=" ".join(itemlist)
    # print(line)

    nlp = spacy.load("en_core_web_sm")
    # doc = nlp(line)
    # for sent in doc.sents:
    #     print(sent.text)
    # print("-------------")
    # for ent in doc.ents:
    #     print(ent.text, ent.start_char, ent.end_char, ent.label_)
    #     print()

    # displacy.serve(doc, style="ent")
    # displacy.serve(doc, style="dep")

    for item in itemlist:
        doc = nlp(item)
        print("------------------")
        for ent in doc.ents:
            print(ent.text, ent.label_)
            print()
