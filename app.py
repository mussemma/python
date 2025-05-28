print("welcome to python program")
class ParentA:
    def feature(self):
        return "Feature from ParentA"

    def common_method(self):
        return "Common method from ParentA"


class ParentB:
    def feature(self):
        return "Feature from ParentB"

    def common_method(self):
        return "Common method from ParentB"


class Child(ParentA, ParentB):
    def call_features(self):
        return self.feature()

    def call_common(self):
        return self.common_method()


# Create an instance of Child
child = Child()

# Print the Method Resolution Order
print("MRO:", [cls.__name__ for cls in Child.__mro__])

# Test method calls
print(child.call_features())  # Calls feature() from ParentA
print(child.call_common())    # Calls common_method() from ParentA