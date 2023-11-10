import re
import sys

expression = sys.stdin.readline().strip()
operators = ['+', '-']
parts = re.split(r'(' + '|'.join(re.escape(op) for op in operators) + ')', expression)

# 결과 출력
print(parts)

for i in len(parts):
    if i == '-':
        i = '- ('
        for 
        
