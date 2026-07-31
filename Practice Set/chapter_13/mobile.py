class Mobile:
    def __init__(self):
        self.apps=("what's app","instagram","youtube")
        self._contacts={"janu":"84507739920","kashi":"5674313242","satur":"9421142768"}
        self.__messages={"janu":"good morning","kashi":"how are you?"}

    def see_apps(self):
        return self.apps

    def see_contact(self):
        return self._contacts

    def see_messages(self):
        return self.__messages

m=Mobile()
# print(m.see_apps())
# print(m.see_contact())
# print(m.see_messages())
print(m.apps)
print(m._contacts)
print(m._Mobile__messages)