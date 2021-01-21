string = input()
result = ''

result += 'E' if string[0] == 'I' else 'I'
result += 'S' if string[1] == 'N' else 'N'
result += 'T' if string[2] == 'F' else 'F'
result += 'J' if string[3] == 'P' else 'P'
print(result)