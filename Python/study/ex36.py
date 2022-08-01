# 내장 함수(builtins)
# help(). int(), float(), str(), list(), dict(), set(), tuple(), type(), id(), ...
lst = [40, 90, 85, 60, 70, 30, 65]
print("lst의 요소 수 : ", len(lst))
print("lst의 요소의 합 : ", sum(lst))
print("lst의 요소중 최대값 : ", max(lst))
print("lst의 요소중 최소값 : ", min(lst))

import statistics                               # statistics 모듈 로딩
from statistics import variance, stdev, geometric_mean, harmonic_mean, median        # statistics 모듈 안의 함수를 로딩
print("lst의 표준편차 : ", stdev(lst))
print("lst의 분산 : ", variance(lst))
# 평균 : 산술 평균, 기하 평균, 조화 평균, 평방 평균(quadratic mean)
print("lst의 산술 평균 : ", mean(lst))                # 산술 평균
print("lst의 기하 평균 : ", geometric_mean(lst))      # 기하 평균
print("lst의 조화 평균 : ", harmonic_mean(lst))       # 조화 평균
print("lst의 중간값 : ", median(lst))