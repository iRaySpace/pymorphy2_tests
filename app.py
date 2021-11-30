import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def get_normal_forms(word):
    parsed_word = morph.parse(word)
    normal_forms = [x.normal_form for x in parsed_word]
    return list(set(normal_forms))


def get_normal_forms_from_sentence(sentence):
    words = sentence.split(' ')
    return {x: get_normal_forms(x) for x in words}
