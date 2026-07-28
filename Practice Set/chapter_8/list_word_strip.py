# 7. Write a python function to remove a given word from a list and strip it at the same time.

def remove_and_strip(lst, word):
    new_list = []
    for item in lst:
        if item.strip() != word:
            new_list.append(item.strip())
    return new_list


li = [" Good ", " Beautiful ", " Preety ", " Cute "]

print(remove_and_strip(li, "Preety"))
