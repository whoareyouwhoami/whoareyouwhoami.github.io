# Relational Database

우리가 흔히 사용하는 MySQL 은 관계형 데이터베이스이다 (Relational Database). 관계형 데이터베이스는 관계있는 데이터들을 행과 열을 사용해 테이블 형태로 표현한다. 각 행에는 고유식별자가 있으면서 하나의 개체/엔티티에 관련된 데이터들을 가지고있다. 그리고 테이블 열은 데이터의 속성값들을 가지고있다. 그 외에도 데이터베이스에는 스키마 (Schema)가 존재하며 이를 통해 데이터베이스의 구조와 제약 조건들을 정의한다. 더 나아가 테이블  사이의 관계를 이용해서 효율적으로 데이터 처리를 할 수 있게 설계할 수 있다.

**SQL 종류**

- **DML (Data Manipulation Language)** - 데이터 조작어
    - 테이블의 행 데이터들에 대해 조회/수정/삭제 등의 역할을함
        - SELECT
        - INSERT
        - UPDATE
        - DELETE

- **DDL (Data Definition Language)** - 데이터 정의어
    - 데이터베이스 또는 테이블에 대해 생성/수정/삭제 등의 역할을함
        - CREATE
        - DROP
        - ALTER
        - RENAME
        - TRUNCATE

- **DCL (Data Control Language)** - 데이터 제어 언어
    - 데이터베이스에 대한 권한을 주는 역할을함
        - GRANT
        - REVOKE

- **TCL (Transaction Control Language)** - 트랜잭션 제어 언어
    - 데이터 처리에 대한 역할을함
        - COMMIT
        - ROLLBACK


**트랜잭션 (Transaction)** 이란 데이터베이스 시스템에 대해서 하나의 작업 단위이다. 그리고 작업들을 원할하게 수행할 수 있게 4가지 조건 (ACID) 을 만족해야 한다. 

- **Atomicity (원자성)**
    - 트랜잭션이 수행하는 연산이 모두 정상적으로 처리되거나 아니면 모두 처리되지 않아야 한다.

- **Consistency (일관성)**
    - 트랜잭션이 성공적으로 처리된 후에도 데이터베이스의 데이터는 일관된 상태를 유지해야 된다.

- **Isolation (격리성)**
    - 트랜잭션이 수행중이면 다른 트랜잭션으로 방해되지 않게 독립적으로 처리해야 한다.

- **Durability (지속성)**
    - 트랜잭션이 성공적으로 완료되면 데이터베이스에 데이터들은 영구적으로 보존되어야 한다.