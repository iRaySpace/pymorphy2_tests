import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def get_normal_forms(word):
    parsed_word = morph.parse(word)
    normal_forms = [x.normal_form for x in parsed_word]
    return list(set(normal_forms))
