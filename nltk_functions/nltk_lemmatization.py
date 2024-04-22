import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

nltk.download("wordnet")
nltk.download("tagsets")
nltk.download("averaged_perceptron_tagger")

lemm = WordNetLemmatizer()


# 단어의 기본형 변환
def lemmatize_word(words, pos):

    if pos in ("v", "n", "a", "r"):
        lem_word = lemm.lemmatize(words, pos=pos)

        return lem_word
    else:
        return words


# 품사 부착 + 원형 복원
def get_wordnet_pos(pos_tag):
    """
    [매개변수] pos_tag: pos_tag()가 반환하는 품사
    [반환값] 문자열:동사-"v" , 명사-"n" , 형용사-"a" , 부사-"r", 그외-None
    """
    if pos_tag.startswith("V"):
        return "v"
    elif pos_tag.startswith("N"):
        return "n"
    elif pos_tag.startswith("J"):
        return "a"
    elif pos_tag.startswith("R"):
        return "r"
    else:
        return None
