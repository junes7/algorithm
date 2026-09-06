WITH RECURSIVE CTE AS (
    #재귀 초기값(1세대=PARENT_ID = NULL인 ROW부터 시작)
    SELECT ID
            ,PARENT_ID
            ,1 AS LEVEL 
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    #재귀
    SELECT E.ID
            ,E.PARENT_ID
            ,1+C.LEVEL
    FROM ECOLI_DATA E INNER JOIN CTE C
        ON E.PARENT_ID = C.ID
)

SELECT COUNT(*) AS 'COUNT'
        ,LEVEL AS GENERATION
FROM CTE C LEFT OUTER JOIN (
                                SELECT PARENT_ID
                                        ,COUNT(PARENT_ID) CNT
                                FROM CTE
                                GROUP BY LEVEL, PARENT_ID
                            ) T
ON C.ID = T.PARENT_ID
WHERE T.PARENT_ID IS NULL
GROUP BY LEVEL
ORDER BY GENERATION;