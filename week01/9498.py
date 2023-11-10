import sys

score = int(sys.stdin.readline())    # 입력받은 값이 문자열이므로, 정수형으로 바꿔주기!

if score >= 90:
    print('A')
elif score >= 80:
        print('B')
elif score >= 70:
        print('C')
elif score >= 60:
        print('D')
else:
    print('F')