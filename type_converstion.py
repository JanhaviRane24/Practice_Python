# Type Conversion (Explicit Conversion)

# int()
value = "100"
converted_int = int(value)
print("\nString to Integer:", converted_int)
print(type(converted_int))

# float()
value = "25.5"
converted_float = float(value)
print("\nString to Float:", converted_float)
print(type(converted_float))

# str()
number = 500
converted_string = str(number)
print("\nInteger to String:", converted_string)
print(type(converted_string))

# bool()
print("\nBoolean Conversion:")
print(bool(1))       # True
print(bool(0))       # False
print(bool("Hello")) # True
print(bool(""))      # False
print(bool([]))      # False


# Implicit Type Conversion

integer_value = 10
float_value = 2.5

result = integer_value + float_value

print("\nImplicit Conversion:")
print("Result:", result)
print("Type:", type(result))


# Explicit Conversion Example

num1 = "20"
num2 = "30"

sum_result = int(num1) + int(num2)

print("\nExplicit Conversion:")
print("Sum:", sum_result)
