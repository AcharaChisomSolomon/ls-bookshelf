# 1
# print(range(0, 25, 3)[6])


# 2
# string = "Launch School"
# id = string.find("c")
# print(string[id:id + 6])


# 3
# orig_tuple = (1, 2, 3, 4, 5)
# list_from_tuple = list(orig_tuple)
# list_from_tuple.reverse()
# list_from_tuple.pop()
# list_from_tuple.pop(0)
# new_tuple = tuple(list_from_tuple)
# print(new_tuple)


# 4
# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }
# print(pets['Dog'])
# print(pets.get("Lizard"))
# print(pets.get("Lizard", "<silence>"))


# 7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = "+".join(info.split(":"))
print(new_info)