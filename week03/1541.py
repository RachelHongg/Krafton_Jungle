import sys

expression = sys.stdin.readline().strip()
elements = expression.split('-')
result = 0
sub_total = 0

for i in range(len(elements)):
    sub_elements = elements[i].split('+')
    sub_total = 0
    for sub_element in sub_elements:
            sub_total += int(sub_element)
            elements[i] = sub_total


for i in range(len(elements)):
    if i == 0:
        result = elements[0]
    else:
        result -= elements[i]
        
print(result)           