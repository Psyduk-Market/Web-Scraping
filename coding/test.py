import collections

a = {"a":0, "b":1}

a["b"] += 1
a["c"] = 9
# a = sorted(a.items(), key=lambda kv: kv[1], reverse=True)

# a = collections.OrderedDict(a)
print(a)

# b = "Hello"
#
# b = b.replace("o","")
#
# print(b)
# print(len(b))

result = a.keys()
print(result)
print("b" in result)
