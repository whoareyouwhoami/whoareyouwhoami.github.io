# RediSearch

[RediSearch](https://github.com/RediSearch/RediSearch)는 Redis 기반의 검색엔진이다. 기본적으로 Redis에서 제공하는 자료구에서는 인덱싱을 제공하지만 RediSearch는 보조 인덱스 (Secondary Index)를 사용한다. 그 결과 전문 검색 (Full Text Search) 외에도 다중 필드 쿼리 검색이 가능하다. Full text search란 말 그대로 전체를 검색하는 것이다. 즉, 검색하는 단어에 해당하는 전체 문서/내용을 찾는 것이다. RediSearch는 일반 Redis 인덱스를 사용하는 것보다 검색하는 단어에 대해 조금 더 유연하고 효율적으로 접근하는데 집중해 개발된 모듈이라고 생각한다.

인덱스는 테이블에 있는 레코드를 빨리 검색하려고 사용하는 하나의 테크닉이다. 보조 (Secondary) 인덱스는 기본 (Primary) 인덱스의 다음 인덱스라고 보면 쉽다. 예를 들어 설명하는게 이해하기 훨씬 쉬울것이다.

```
STUDENT
------------------------------------------
| ID |  Name  | Major | Year | Grad Date |
|----|--------|-------|------|-----------|
| 1  | Lauren | CS    | 2014 |   2021    |
| 2  | Peter  | MATH  | 2013 |   2022    |
| 3  | James  | SCI   | 2011 |   2020    |
| 4  | Lauren | STAT  | 2017 |   2025    |
| 5  | Marry  | ENG   | 2013 |   2024    |
------------------------------------------
```

위 테이블에서 학생번호 ID는 기본 키 (Primary Key)이다. 기본 인덱스는 기본 키들을 가리킨다. 즉, 중복이 있으면 안된다. 반대로 보조 인덱스는 중복을 허용한다. 예를 들면 학생번호로 레코드를 찾는다면 1개의 행이 반환될 것이다. 그러나 이름을 사용하면 1개 이상의 레코드를 찾아 반환할 수 있다. 만약 테이블이 너무 커지고 읽기 활동이 많아지면 보조키를 만들어 분산시키는게 좋다.


## 검색 엔진

```
Crawling -> Indexing -> Query
```

검색 엔진은 위와 같이 3단계를 거친다고 볼 수 있다. 먼저 1 단계에서는 자료들을 수집한다. 그리고 각 자료에 인덱싱을 거쳐 메타데이터를 생성한다. 마지막으로 메타데이터의 정보를 가지고 쿼리를 던져서 검색을 실행한다.

여기서 알아보고 싶은건 2번째 단계인 인덱싱이다.

### Inverted Index

역색인 (inverted index) 이란 전문 검색을 빨리 실행시킬 수 있게 도와주는 인덱싱 자료구조이다. 역색인 자료구조에는 2가지 종류가 있다. 각 단어에가 포함된 문서들을 담는 종류와 문서와 단어의 위치를 나타내는 종류가 있다.

```
Original Data
---------------------------------------------------------------------------------
|Document | Content                                                             |
|---------|---------------------------------------------------------------------|
|    1    | He saw a boy playing with his dog.                                  |
|    2    | When the boy whistled, the dog ran straight to him.                 |
|    3    | He tried to whistle, but he couldn’t.                               |
|    4    | Peter ran home to show his father and mother what he could do.      |
|    5    | He whistled all the way home.                                       |
---------------------------------------------------------------------------------

Inverted Index
------------------------------------
| Word     | (Document, Position)  |
|----------|-----------------------|
| saw      | (1, 2)                |
| boy      | (1, 4), (2, 3)        |
| play     | (1, 5)                |
| dog      | (1, 8), (2, 6)        |
| whistle  | (2, 4), (5, 2)        |
| straight | (2, 8)                |
| ...      | ...                   |
------------------------------------
```

역색인을 만들기 위해서 몇 단계 처리 과정이 있다. 

먼저 **stop words**를 제거한다. Stop words는 문서에서 빈번하게 발생하는 단어들, 주로 검색에 크게 도움되지 않는 단어들을 제거한다. 예를 드면, 'a', 'with', 'the' 같이 문장의 의미를 떠나 자주 발생하는 단어들을 먼저 제거해준다. RediSearch에는 기본으로 사용되는 stop words들은 다음과 같다.

```
 a,    is,    the,   an,   and,  are, as,  at,   be,   but,  by,   for,
 if,   in,    into,  it,   no,   not, of,  on,   or,   such, that, their,
 then, there, these, they, this, to,  was, will, with
```

그 외에도 RediSearch에서는 stop words들을 새로 만들 수 있고 또는 stop words 기능을 제거할 수 있다.

 다음으로 **stemming**과 **Lemmatization**을 통해 어근을 추출해 낸다 ('playing' -> 'play'). 그 외에도 URL이나 태그들을 제거하는 과정도 있다. 이러한 과정을 통해 마지막으로 해당 글자가 속한 서류 ID를 기록하고 단어의 위치 또는 빈도, 스코어 등 다양한 정보를 담아 역색인을 만들 수 있다.

- [RediSearch Inverted Index](https://github.com/RediSearch/RediSearch/blob/master/docs/DESIGN.md)

RediSearch에 대한 자세한 내용은 [공식 사이트](https://oss.redislabs.com/redisearch/)를 통해 알아볼 수 있다.