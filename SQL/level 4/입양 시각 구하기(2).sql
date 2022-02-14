SET @HOUR := -1 ;

SELECT (@HOUR := @HOUR + 1) AS HOUR,
        (SELECT COUNT(*)
        FROM ANIMAL_OUTS
        WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23 ;

# SET 옆에 변수명과 초기값을 설정할 수 있습니다.
# @가 붙은 변수는 프로시저가 종료되어도 유지된다고 생각하면 됩니다.
# 이를 통해 값을 누적하여 0부터 23까지 표현할 수 있습니다.
# @hour은 초기값을 -1로 설정합니다. PL/-SQL 문법에서 :=은 비교 연산자 =과 혼동을 피하기 위한의 대입 연산입니다.
# SELECT (@hour := @hour +1) 은 @hour의 값에 1씩 증가시키면서 SELECT 문 전체를 실행하게 됩니다.
# 이 때 처음에 @hour 값이 -1 인데, 이 식에 의해 +1 이 되어 0이 저장됩니다.
# HOUR 값이 0부터 시작할 수 있습니다.
# WHERE @hour < 23일 때까지, @hour 값이 계속 + 1씩 증가합니다.
