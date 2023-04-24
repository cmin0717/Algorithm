-- 최소값 구하기 -- (MIN함수 사용)
SELECT MIN(DATETIME) AS '시간' 
FROM ANIMAL_INS


-- 동물 수 구하기 -- (COUNT 함수 사용)
SELECT COUNT(*)
FROM ANIMAL_INS


-- 중복 제거하기 -- 
SELECT COUNT(A.NAME) -- 해당 테이블 네임을 그룹으로 설정하면 중복값이 사라진다. 그 그룹에서의 NAME의 개수를 출력
FROM (SELECT NAME
FROM ANIMAL_INS
GROUP BY NAME) A

SELECT COUNT(DISTINCT(NAME)) -- DISTINCT함수를 사용하여 중복을 제거한 NAME의 개수를 출력
FROM ANIMAL_INS


-- 동명 동물 수 찾기 --
SELECT NAME, COUNT(NAME) AS COUNT -- NAME과 NAME의 카운트수를 출력
FROM ANIMAL_INS
WHERE NAME IS NOT NULL -- NULL값은 그룹화 하기전에 미리 처리
GROUP BY NAME -- NAME으로 그룹화 하고
HAVING COUNT(NAME) >= 2 -- 해당 네임의 카운트수가 2이상만
ORDER BY NAME -- 네임을 기준으로 오름차순으로


-- 이름에 EL이 들어가는 동물 찾기 --
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = 'DOG' --이름에 EL이 들어가면서 강아지인 것만 출력
ORDER BY NAME


-- NULL 처리하기 --
SELECT ANIMAL_TYPE, IFNULL(NAME,'No name'), SEX_UPON_INTAKE -- IFNULL를 사용하여 NULL값을 원하는값으로 출력
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- DATETIME에서 DATE로 형 변환 --
SELECT ANIMAL_ID,NAME, LEFT(DATETIME,10) --LEFT를 사용하여 필요한값만 출력 (DATE_FORMAT를 사용하여 해결할수도있다.)
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- 가격이 제일 비싼 식품의 정보 출력하기 --
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT) --서브쿼리를 사용하여 MAX값을 가져온후 해당 값과 같은것만 출력

SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC -- 가격 내림차순 
LIMIT 1 -- 가격을 내림차순으로 정렬후 1개만 출력하는 방법도 있다.


-- 고양이와 개는 몇 마리 있을까 --
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) --해당 타입과 그 타입이 그룹안에 몇개있는지 출력
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE -- 타입으로 그룹을 형성
HAVING ANIMAL_TYPE IN ('Cat','Dog') -- 타입이 개와 고양이만
ORDER BY ANIMAL_TYPE --타입의 이름순으로 정렬


-- 중성화 여부 파악하기 --
SELECT ANIMAL_ID, NAME,
CASE
WHEN SEX_UPON_INTAKE LIKE "%Intact%" -- CASE,END와 LIKE함수를 이용하여 해결
THEN 'X' ELSE 'O'
END
AS "중성화"
-- IF (SEX_UPON_INTAKE LIKE "%Intact%", 'X', 'O') AS '중성화'  // 이렇게 작성할수 있다. IF (조건문, 참일때, 거짓일때)
FROM ANIMAL_INS
ORDER BY ANIMAL_ID


-- 입양 시각 구하기(1) --
SELECT HOUR(DATETIME), COUNT(*) --해당 시간과 그 시간에 해당하는 수를 출력
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20 --그룹하기 전에 범위안에 시간만 그룹화 한다.
GROUP BY HOUR(DATETIME) -- 시간을 HOUR로 변환한 값을 그룹화 한다.
ORDER BY HOUR(DATETIME)


-- 카테고리 별 상품 개수 구하기 --
SELECT LEFT(PRODUCT_CODE,2) AS CATEGORY, COUNT(*) -- PRODUCT_CODE에서 2자리만 출력하고 개수 출력
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE,2) -- PRODUCT_CODE의 왼쪽에서 2번쨰 까지만 자른걸 그룹화한다.
--GROUP BY CATEGORY // 이렇게도 표현할수 있다. 근데 이해가 가지 않는다 SELECT보다 GROUP BY가 먼저 실행인데 SELECT의 값을 참조할수있나??
ORDER BY PRODUCT_CODE


-- 진료과별 총 예약 횟수 출력하기 --
SELECT MCDP_CD AS "진료과코드", COUNT(MCDP_CD) AS '5월예약건수' -- 각 진료과코드와 건수를 출력
FROM APPOINTMENT
WHERE LEFT(APNT_YMD,7) = '2022-05' -- 해당 월에 속하는 진료만 그룹화한다.
GROUP BY MCDP_CD -- 진료과코드를 그룹화
ORDER BY 5월예약건수, 진료과코드 -- AS로 부여한 이름으로 정렬시킬수있다. "5월예약건수" 형태가 아닌 5월예약건수 형태로 사용해야한다.


-- 상품 별 오프라인 매출 구하기 --
SELECT P.PRODUCT_CODE, SUM(P.PRICE*O.SALES_AMOUNT) AS SALES -- 제품 코드와 SUM함수를 이용하여 총 가격을 출력
FROM PRODUCT P
JOIN OFFLINE_SALE O
ON P.PRODUCT_ID = O.PRODUCT_ID -- 두 테이블에서 ID가 같은것만 가져온다.
GROUP BY P.PRODUCT_CODE -- 제품 코드를 기준으로 그룹화한다.
ORDER BY SALES DESC, P.PRODUCT_CODE


-- 루시와 엘라 찾기 --
SELECT ANIMAL_ID,NAME,SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty") --IN 메소드를 사용하여 조건에 맞게 출력


-- 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기 --
SELECT CAR_TYPE, COUNT(CAR_TYPE) AS 'CARS' --그룹화해서 나온 애들의 타입과 해당 타입의 전체 수를 출력
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE "%통풍시트%" OR OPTIONS LIKE "%열선시트%" OR OPTIONS LIKE "%가죽시트%" -- LIKE를 사용하여 하나라도 참인 애들만 가져온다.
GROUP BY CAR_TYPE -- TYPE으로 그룹화
ORDER BY CAR_TYPE


-- 조건에 맞는 도서와 저자 리스트 출력하기 --
SELECT B.BOOK_ID, A.AUTHOR_NAME, LEFT(B.PUBLISHED_DATE,10)
FROM BOOK B
JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID -- 두 테이블의 작가 ID가 같은것들에서만 탐색한다. 
WHERE B.CATEGORY = '경제' -- JOIN은 FROM과 같은 라인이다. 그렇기에 WHERE은 JOIN 다음에 사용해야한다.
ORDER BY B.PUBLISHED_DATE


-- 성분으로 구분한 아이스크림 총 주문량 --
SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER -- 그룹화에서 타입과 해당 타입의 총 주문량을SUM함수로 출력
FROM FIRST_HALF F
JOIN ICECREAM_INFO I
ON F.FLAVOR = I.FLAVOR -- 두 테이블에서 맛이 같은것에서만 탐색
GROUP BY I.INGREDIENT_TYPE -- 타입으로 그룹화
ORDER BY TOTAL_ORDER


-- 3월에 태어난 여성 회원 목록 출력하기 --
SELECT MEMBER_ID, MEMBER_NAME, GENDER, LEFT(DATE_OF_BIRTH,10)
FROM MEMBER_PROFILE
WHERE GENDER = 'W' AND MONTH(DATE_OF_BIRTH) = 3 AND TLNO IS NOT NULL


-- 가격대 별 상품 개수 구하기 --
SELECT TRUNCATE(PRICE / 10000,0) *10000 AS PRICE_GROUP, COUNT(*) --TRUNCATE함수를 사용하여 소수점 0번쨰 까지만 출력한다.
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP


-- 재구매가 일어난 상품과 회원 리스트 구하기 --
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY PRODUCT_ID, USER_ID -- 유저와 상품을 같이 그룹화한다.
HAVING COUNT(*) > 1 --그룹화 중에서 개수가 1개 이상이라면 재구매다.
ORDER BY USER_ID, PRODUCT_ID DESC

SELECT DISTINCT A.USER_ID, A.PRODUCT_ID -- SELF JOIN를 사용하여 해결하는 방법도 있다. 하지만 이렇게 하면 중복결과가 나오기에
FROM ONLINE_SALE A                      -- DISTINCT로 중복을 제거해야한다.
JOIN ONLINE_SALE B
ON A.USER_ID = B.USER_ID AND 
A.PRODUCT_ID = B.PRODUCT_ID
WHERE A.SALES_DATE != B.SALES_DATE
ORDER BY A.USER_ID, A.PRODUCT_ID DESC


-- 조건에 부합하는 중고거래 상태 조회하기 -- 
SELECT BOARD_ID,WRITER_ID,TITLE,PRICE,
CASE
WHEN STATUS = 'SALE' THEN '판매중'     -- CASE END 구문을 사용하여 값에 해당하는 문구 출력
WHEN STATUS = 'RESERVED' THEN '예약중'
ELSE '거래완료'
END AS STATUS
FROM USED_GOODS_BOARD
WHERE LEFT(CREATED_DATE,10) = '2022-10-05'
ORDER BY BOARD_ID DESC


-- 자동차 평균 대여 기간 구하기 --
SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7 --그룹에서 평균이 7이 이상인 애들만 출력
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC
-- DATEDIFF(END_DATE, START_DATE)+1에서 +1를 해주는 이유는 시작날짜도 더해주어야 하기에 +1해주었다.
-- 10-05 부터 10-10일까지 빌렸다고 치면 총 6일을 빌린건데 DATEDIFF값은 5가 나오기 때문이다.