import sys

A, B = sys.stdin.readline().split() # 입력받은 문자열을 공백 기준으로 분리
A = int(A)  # 입력받은 값은 문자열 상태입으로 int를 사용해서 정수로 변환
B = int(B)  # 변수를 정수로 변환한 뒤 다시 저장
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)