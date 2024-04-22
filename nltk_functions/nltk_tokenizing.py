import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer, sent_tokenize, word_tokenize

nltk.download("punkt")
nltk.download("stopwords")


def tokenize_word(sentence):
    # 토큰화
    tokens = word_tokenize(sentence)

    # 불용어 제거(토큰 단위)
    stop_words = set(stopwords.words("english"))
    filterd_tokens = [
        token
        for token in tokens
        if (token.lower() not in stop_words)
        and (
            token.lower()
            not in ["‘", "’", "“", "”", ",", ".", "`", "'", "''", "``", "?", "!"]
        )
    ]

    filterd_tokens2 = []

    # 마지막글자가 특수문자(.)인 토큰에서 (.) 제거.
    for no_endpoint_token in filterd_tokens:
        if no_endpoint_token[-1] == ".":
            no_endpoint_token = no_endpoint_token[:-1]
        else:
            no_endpoint_token = no_endpoint_token

        filterd_tokens2.append(no_endpoint_token)

    return filterd_tokens2


def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    return sentences


def treebanktokenize_word(sentence):
    # 리서치 중....(미사용)
    # 하이푼으로 구성된 단어는 하나로 유지, 아포스트로피로 접어가 함께하는 단어는 분리.
    tokens = TreebankWordTokenizer(sentence)

    # 불용어 제거(토큰 단위)
    stop_words = set(stopwords.words("english"))
    filterd_tokens = [
        token
        for token in tokens
        if (token.lower() not in stop_words)
        and (
            token.lower()
            not in ["‘", "’", "“", "”", ",", ".", "`", "'", "''", "``", "?", "!"]
        )
    ]

    return filterd_tokens
