

string = "thisisazigzag"

k = 4

n = 2 * k - 1

result = ""

result += string[0]
result += string[n - 1]
result += string[n*2 - 2]

result += string[1]
result += string[n - 2]
result += string[n + 1]
result += string[n * 2 + 2]

print(result)
