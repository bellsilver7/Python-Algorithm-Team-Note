import math

def isPrimeNumber(num):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(num)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if num % i == 0:
            return False
    return True
