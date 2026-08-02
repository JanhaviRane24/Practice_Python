# def call_by_val(x):
#     x = x * 2
#     return x

# def call_by_ref(b):
#     b.append("D")
#     return b

# a = ["E"]
# num = 6

# updated_num = call_by_val(num)
# updated_list = call_by_ref(a)
# print("Updated value after call_by_val:", updated_num)
# print("Updated list after call_by_ref:", updated_list)

def call_by_value(c):
    c=c*3
    return c

def call_by_reference(d):
    d.append("E")
    return d

print("call by value",call_by_value([4]))
print("call by reference",call_by_reference([4]))