# 6. Can you change the self-parameter inside a class to something else (say “harry”)? Try
# changing self to “slf” or “harry” and see the effects

class Demo:
    name="harry"
    def __init__(slf):
        pass

d=Demo()
print(d.name)
d.name="harit"
print(d.name)

#Yes. In Python, self is just a convention, not a reserved keyword. 
# You can replace it with any valid parameter name such as slf, harry, or obj. 
# # The code will still work as long as you use the same name consistently inside the method.
# ✅ Python does not require the first parameter to be named self.
# ⭐ However, self is the standard Python convention, 
# so it is recommended to use it to make your code easier for others to read and maintain.