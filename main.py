from sqlalchemy import text

from databases.service import DatabaseService as ds
from nltk_functions.nltk_tokenizing import tokenize_word

# DatabaseService 인스턴스 생성
database_service = ds("/workspaces/making_sentence/content/mysql_talktree_dev.json")

# get_engine 메서드 호출
engine = database_service.get_engine()

# SQL 쿼리 작성
query = text(
    """
       SELECT sample_sentence
            , sample_sentence_10000_word_id 
         FROM sample_sentence_10000_words
    """
)

# 연결 생성
connection = engine.connect()

# 쿼리 실행
result = connection.execute(query)

# 결과를 반복하며 word_tokenize 함수 적용
for row in result:
    tokenized_sentence = tokenize_word(row[0])
    sentence_id = row[1]
    word_levels = []  # word_level 결과를 저장할 리스트
    for token in tokenized_sentence:
        query = text(
            """
               SELECT word_level 
                 FROM word_10000_scale_500_total 
                WHERE word = :token
            """
        )

        # 쿼리 실행
        word_level_result = connection.execute(query, {"token": token})

        # 결과를 리스트에 추가
        for word_level in word_level_result:
            word_levels.append(word_level[0])

    # word_levels 리스트에서 최대값 추출
    max_word_level = max(word_levels) if word_levels else None

    # max_word_level 값을 해당 sample_sentence의 corpus_level로 업데이트
    # update_query = text(
    #     """
    #        UPDATE sample_sentence_10000_words
    #           SET corpus_level = :max_word_level
    #         WHERE sample_sentence_10000_word_id = :sentence_id
    #     """
    # )
    update_query = text(
        """
        UPDATE sample_sentence_10000_words 
           SET corpus_level = :max_word_level
         WHERE sample_sentence_10000_word_id = :sentence_id
        """
    )
    select_query = text(
        """
        SELECT corpus_level
          FROM sample_sentence_10000_words
         WHERE sample_sentence_10000_word_id = :sentence_id
        """
    )

    update_result = connection.execute(
        update_query, {"max_word_level": max_word_level, "sentence_id": sentence_id}
    )
    select_result = connection.execute(select_query, {"sentence_id": sentence_id})

    print(f"Number of rows updated: {update_result.rowcount}")
    print(select_result.fetchone())

# 연결 종료
connection.close()
