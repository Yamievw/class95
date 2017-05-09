class test():
    def __init__(self, value):
        self.value = value

        
    def set_value(self, new_value):
        self.value = new_value
    def get_value(self):
        return self.value



a = test(3)
b = a
print a.get_value(), b.get_value()
a.set_value(5)

print a.get_value(), b.get_value()
