-- 오랜 기간 보호한 동물(1) --
SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS) -- 나간 애들을 서브쿼리로 구하고 거기에 포함되지 않는 애들만 가져온다.
ORDER BY DATETIME
LIMIT 3 -- 3개만 가져와야하니깐 LIMIT을 3으로 준다.


-- 오랜 기간 보호한 동물(2) --
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID -- 두테이블에서 ID가 같은것에서만 탐색
-- GROUP BY DATEDIFF(O.DATETIME, I.DATETIME) -- 두 시간차이를 그룹화하고 // 생각해 보니 그룹화는 안해도 될듯?
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC -- 해당 그룹을 시간차이로 내림차순 정렬
LIMIT 2 -- 거기서 2개만 출력


-- 있었는데요 없었습니다 --
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I -- 두 테이블에서 ID가 같은 애들끼리 JOIN시키고 
JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME -- 두테이블의 정보를 토대로 판단후 참인 애들만 출력
ORDER BY I.DATETIME


-- 카테고리 별 도서 판매량 집계하기 --
SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES -- 카테고리별로 그룹화한곳에서 SALE의 총합을 구한다.
FROM BOOK B
JOIN 
(SELECT BOOK_ID, SUM(SALES) AS SALES -- BOOK_SALES테이블에서 ID별로 판매량을 그룹화로 얻어온다.
FROM BOOK_SALES
WHERE LEFT(SALES_DATE,7) = '2022-01'
GROUP BY BOOK_ID) S
ON B.BOOK_ID = S.BOOK_ID -- 누적 판매량 테이블과 ID가 같은것끼리 JOIN해준다.
GROUP BY CATEGORY -- JOIN한 테이블에서 카테고리로 그룹화
ORDER BY CATEGORY

-- SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES -- 한꺼번에 처리할수도 있다. JOIN이후에 한번의 그룹화를 통해
-- FROM BOOK B
-- JOIN BOOK_SALES S
-- ON B.BOOK_ID = S.BOOK_ID
-- WHERE LEFT(S.SALES_DATE,7) = '2022-01'
-- GROUP BY CATEGORY
-- ORDER BY CATEGORY


-- 조건별 분류하여 주문상태 출력하기 --
SELECT ORDER_ID, PRODUCT_ID,
LEFT(OUT_DATE,10) AS OUT_DATE,
CASE
WHEN OUT_DATE IS NULL THEN '출고미정'
WHEN OUT_DATE > "2022-05-01" THEN '출고대기' -- 2022-05-01 보다 작은애들은 출고대기
ELSE '출고완료'
END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID


-- 조건에 맞는 사용자와 총 거래금액 조회하기 --
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES -- ID와 닉네임, ID에 해당하는 사람의 판매된 상품의 합계가격
FROM USED_GOODS_BOARD  B
JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID -- 두테이블에서 각 ID가 같은것을 JOIN시킨 테이블에서
WHERE B.STATUS = 'DONE' -- 현재 판매가 끝난 상품만
GROUP BY B.WRITER_ID -- ID값을 그룹화하여
HAVING TOTAL_SALES >= 700000 -- 합계가격이 700000만원 이상인것만
ORDER BY TOTAL_SALES


-- 없어진 기록 찾기 --
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID NOT IN
(SELECT ANIMAL_ID FROM ANIMAL_INS) -- 입양간 애들중에 입양 기록이 없는 애들만 출력
ORDER BY ANIMAL_ID


-- 즐겨찾기가 가장 많은 식당 정보 출력하기 --
SELECT I.FOOD_TYPE, I.REST_ID, I.REST_NAME, I.FAVORITES
FROM REST_INFO I
JOIN
(SELECT FOOD_TYPE, MAX(FAVORITES) AS MAX_F
FROM REST_INFO
GROUP BY FOOD_TYPE) F -- 테이블에서 타입 별로 가장 큰 좋아요 수를 가진 테이블을 만들고 같은 타입별로 JOIN 한다.
ON I.FOOD_TYPE = F.FOOD_TYPE 
WHERE I.FAVORITES = F.MAX_F -- 좋아요 수가 가장큰좋아요 수와 같을경우만 출력
ORDER BY I.FOOD_TYPE DESC


-- 대여 기록이 존재하는 자동차 리스트 구하기 --
SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
ON C.CAR_ID = H.CAR_ID -- ID가 같은 애들끼리 JOIN한 테이블에서 탐색한다.
WHERE MONTH(H.START_DATE) = 10 AND C.CAR_TYPE = '세단' -- 10월달에 대여시작했고 차종이 세단인 차만
ORDER BY CAR_ID DESC


-- 조건에 맞는 사용자 정보 조회하기 --
SELECT U.USER_ID, U.NICKNAME,
CONCAT(U.CITY,' ',U.STREET_ADDRESS1,' ',STREET_ADDRESS2) AS '전체주소', -- CONCAT함수를 이용하여 문자열을 조건에 맞게 출력한다.
CONCAT(LEFT(U.TLNO,3),'-',SUBSTR(U.TLNO,4,4) ,'-',RIGHT(U.TLNO,4)) AS '전화번호' --CONCAT함수와 SUBSTR를 이용하여 조건에 맞게 출력
FROM USED_GOODS_BOARD B                                                        -- SUBSTR(X,I,J) : X문자열에서 I번부터 J개를 출력한다.
JOIN USED_GOODS_USER U
ON B.WRITER_ID = U.USER_ID
GROUP BY B.WRITER_ID -- 두 테이블을 JOIN한곳에서 ID로 그룹화한다.
HAVING COUNT(B.WRITER_ID) >= 3 -- 그룹화한곳에서 같은 ID가 3개 이상인것만 출력
ORDER BY U.USER_ID DESC


-- 헤비 유저가 소유한 장소 --
SELECT P.ID, P.NAME, P.HOST_ID
FROM PLACES P
JOIN
(SELECT HOST_ID, COUNT(HOST_ID) AS CNT -- 테이블에서 HOST_ID로 그룹화 하여 해당 ID가 몇개씩 있는지 아는 테이블를 PALCES테이블과 JOIN
FROM PLACES
GROUP BY HOST_ID) C
ON P.HOST_ID = C.HOST_ID -- 같은 HOST_ID와 JOIN한다.
WHERE C.CNT >= 2 -- 가져온 헤비 유저 조건에 만족하는 애들만 출력
ORDER BY P.ID


-- 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기 --
SELECT DISTINCT CAR_ID,  -- DISTINCT로 중복 제거
IF (CAR_ID IN (           -- 만약 ID가 서브쿼리로 구한 대여중인 애들 안에 있다면 대여중 없다면 대여 가능 출력
SELECT DISTINCT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE), '대여중','대여 가능') AS AVAILABILITY 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC


-- 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기 --
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(CAR_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN -- CAR_ID가 '2022-08' AND '2022-10'안에 있고 '2022-08' AND '2022-10'동안 5건 이상 대여한 ID중 하나일경우에만 출력
(SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE LEFT(START_DATE,7) BETWEEN '2022-08' AND '2022-10'
GROUP BY CAR_ID
HAVING COUNT(CAR_ID) >= 5) AND
LEFT(START_DATE,7) BETWEEN '2022-08' AND '2022-10'
GROUP BY MONTH(START_DATE), CAR_ID -- 달과 ID를 그룹화하여 해당하는 애들의 전체 개수를 구한다.
ORDER BY MONTH, CAR_ID DESC


-- 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기 --
SELECT CONCAT("/home/grep/src/",BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID =  -- ID가 조회수가 가장 많은 게시판의 ID와 같은 것만 출력
(SELECT BOARD_ID
FROM USED_GOODS_BOARD
ORDER BY VIEWS DESC
LIMIT 1) -- LIMIT을 사용하면 IN 연산자를 사용할수없다.
ORDER BY FILE_ID DESC