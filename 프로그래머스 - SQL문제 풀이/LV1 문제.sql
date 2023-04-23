-- 동물의 아이디와 이름 -- (주어진 테이블에서 ID값을 기준으로 ID와 NAME를 오름차순으로 출력)
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC -- ASC는 내림차순(디폴트값이기에 없어도 된다.)


-- 이름이 있는 동물의 아이디 -- (주어진 테이블에서 이름이 있는 컬럼의 ID값을 오름차순으로 출력)
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL -- WHERE NAME != NULL 이 문법은 작동하지 않았다.
-- WHERE NAME IS NOT TRUE 이건 정상 작동한다.
ORDER BY ANIMAL_ID

-- 이름이 없는 동물의 아이디
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID


-- 어린 동물 찾기 -- (테이블에서 INTAKE_CONDITION값이 Aged가 아닌 컬럼들)
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged' -- 문자열 비교에서는 != 이 먹는다. NULL값에만 먹지 않는건가?


-- 상위 N개 레코드 -- (테이블에서 가장 날짜가 빠른 컬럼의 이름 출력)
SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS) -- 서브쿼리를 이용하여 테이블에서 가장빠른 날짜를 가져왔다.


-- 역순 정렬하기 -- (NAME과 DATETIME를 ID값을 기준으로 역순으로 출력)
SELECT NAME,DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC -- DESC는 내림차순 정렬이다.


-- 여러 기준으로 정렬하기 -- (ANIMAL_ID,NAME,DATETIME를 이름을 기준으로 오름차순 이름이 같다면 데이트타임을 내림차순으로 정렬)
SELECT ANIMAL_ID,NAME,DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC -- 정렬 기준을 여러개 줄수있다.


-- 아픈 동물 찾기 -- (동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회)
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID


-- 나이 정보가 없는 회원 수 구하기 -- (나이 정보가 없는 ID를 서브쿼리로 구하고 해당 쿼리에 ID가 있는 사람들의 수를 USERS로 출력)
--COUNT(*)는 NULL 값을 포함하고 COUNT(AGE)와 같이 특정 컬럼을 지정해줄 경우 NULL 값을 포함하지 않기 때문입니다
SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE USER_ID IN (SELECT USER_ID FROM USER_INFO WHERE AGE IS NULL)

SELECT COUNT(*) - COUNT(AGE) AS USERS -- COUNT 함수를 통해 알아서 NULL값을 제외하고 COUNT한다.
FROM USER_INFO


-- 강원도에 위치한 생산공장 목록 출력하기 -- (LIKE를 사용하여 풀이)
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE "%강원도%" -- ADDRESS에 강원도라는 글자가 있는 애들만 출력
ORDER BY FACTORY_ID


-- 경기도에 위치한 식품창고 목록 출력하기 -- (IFNULL를 이용하여 NULL값을 N으로 출럭)
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') -- IFNULL은 주어진 값이 NULL이면 지정한 문자를 출력한다.
-- CASE 
-- WHEN FREEZER_YN IS NULL
-- THEN 'N' ELSE FREEZER_YN 
-- END  / CASE-END를 이용하여 처리할수도 있다.
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "%경기도%"
ORDER BY WAREHOUSE_ID


-- 가장 비싼 상품 구하기 -- (MAX함수를 이용)
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT


-- 조건에 맞는 회원수 구하기 -- (BETWEEN과 YEAR함수를 이용하여 풀이)
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE BETWEEN 20 AND 29 AND YEAR(JOINED) = '2021'


-- 흉부외과 또는 일반외과 의사 목록 출력하기 -- (DATE_FORMAT를 이용하여 원하는 형식의 시간으로 출력)
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d")
FROM DOCTOR
WHERE MCDP_CD IN ("CS",'GS') -- ["CS","GS"]는 안된다 ()를 사용하자
ORDER BY HIRE_YMD DESC, DR_NAME ASC


-- 12세 이하인 여자 환자 목록 출력하기 --
SELECT PT_NAME,PT_NO,GEND_CD,AGE,IFNULL(TLNO,'NONE') -- IFNULL를 이용하여 NULL값은 NONE으로 출력
FROM PATIENT
WHERE GEND_CD = 'w' AND AGE <= 12 -- 각 조건에 해당하는 애들만 출력
ORDER BY AGE DESC, PT_NAME


-- 인기있는 아이스크림 --
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID


-- 모든 레코드 조회하기 --
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- 조건에 맞는 도서 리스트 출력하기 --
SELECT BOOK_ID,DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") -- DATE_FORMAT를 이용하여 주어진 시간형으로 출력
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = '2021' AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE


-- 평균 일일 대여 요금 구하기 --
-- ROUND(X,Y) : X값을 소숫점 Y에서 반올림한다. 디폴트는 0이다.
SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE -- ROUND함수와 AVG함수를 이용하여 평균을 반올림해서 가져온다.
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'


-- 최대값 구하기 --
SELECT MAX(DATETIME) -- 해당 테이블에서 해당 컬럼의 최대값을 가져온다.
FROM ANIMAL_INS


-- 특정 옵션이 포함된 자동차 리스트 구하기 --
SELECT CAR_ID,CAR_TYPE,DAILY_FEE,OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE "%네비게이션%" -- LIKE를 이용하여 옵션 컬럼에 네비게이션이 있는지 확인
ORDER BY CAR_ID DESC


-- 자동차 대여 기록에서 장기/단기 대여 구분하기 --
SELECT HISTORY_ID,CAR_ID,
DATE_FORMAT(START_DATE, "%Y-%m-%d") AS START_DATE, -- LEFT(START_DATE, 10)
DATE_FORMAT(END_DATE, "%Y-%m-%d") AS END_DATE,
-- IF(DATEDIFF(END_DATE, START_DATE) >= 29, "장기 대여", "단기 대여") -- 이렇게 작성할수도 있다.
CASE
WHEN DATEDIFF(END_DATE, START_DATE) >= 29 -- DATEDIFF를 사용하여 두 날짜의 차이를 구한다.
THEN '장기 대여' ELSE '단기 대여'
END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- WHERE LEFT(START_DATE) = "2022-9" 이렇게 작성할수도 있다.
WHERE YEAR(START_DATE) = "2022" AND MONTH(START_DATE) = '9'
ORDER BY HISTORY_ID DESC


-- 조건에 부합하는 중고거래 댓글 조회하기 --
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, LEFT(R.CREATED_DATE,10)
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_REPLY R --JOIN를 이용하여 두개의 테이블을 검색한다.
ON B.BOARD_ID = R.BOARD_ID AND LEFT(B.CREATED_DATE,7) = "2022-10" -- 해당 조건에 만족하는 애들만 가져온다.
ORDER BY R.CREATED_DATE, B.TITLE