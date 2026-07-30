# # Interview Cheat Sheet

# | Topic                | Keyword               | First Parameter | Purpose                           |
# | -------------------- | --------------------- | --------------- | --------------------------------- |
# | Instance Method      | Normal method         | `self`          | Work with object data             |
# | Class Method         | `@classmethod`        | `cls`           | Work with class data              |
# | Static Method        | `@staticmethod`       | None            | Utility/helper methods            |
# | `__init__`           | Constructor           | `self`          | Initialize object                 |
# | `__str__`            | String representation | `self`          | Customize `print(object)`         |
# | `__len__`            | Length                | `self`          | Customize `len(object)`           |
# | `__eq__`             | Equality              | `self, other`   | Customize `==`                    |
# | Operator Overloading | `__add__`, etc.       | `self, other`   | Define operator behavior          |
# | `@property`          | Getter property       | `self`          | Access a method like an attribute |
# | `@property.setter`   | Setter                | `self, value`   | Validate or control assignment    |
