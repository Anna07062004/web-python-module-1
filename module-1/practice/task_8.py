# d = {
#     "a": 1,
#     "b": [1,2,3],
#     "bool": True,
#     "nested": {
#         "a": 1
#     }
# }
# d_1 = dict(a=1)
# print(d, d_1)

############################################################################
#ключи из.

# keys = ["a", "b", "c"]
# d = dict.fromkeys(keys, 1)
#способ 1

# print(d ["d"])

# cпособ 2

# print(d.get("a"), d.get("d"))

#способ 3

# value = d.setdefault("e", 0)
# print(value)

############################################################################
#задачка 1. находит одинаковые слова.

# fr = ["apple", "banana", "apple"]
# d = {}

# for word in fr:
#     d.setdefault(word, 0)
#     d[word] += 1

# print(d)

##########################################################################

#способ 1
# d.pop("d")

# print(d)

# #способ 2

# del d["c"]

# print(d)

# #способ 3
# key, value = d.popitem()

# d.clear()

# print(d)

#############################################################################

# d_1 = {"a": 1}

# d_1.update({"a": 2, "b": 3})
# d_1.update(c=4,d=5)

# print(d_1)

# if "e" not in d_1:
#     print("ok")

# print(d_1.keys(), d_1.values())

# print(d_1.items())

# for key, value in d_1.items():
#     print(f"{key}={value}")