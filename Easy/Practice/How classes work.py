class Example:
    def say_hello(self, name):
        print(f"Hello {name}, I am inside {self}")

obj = Example()
obj.say_hello("Rhea")


class Counter:
    
    def increment(c1):
        c1 += 1   # needs self to refer to THIS object's count

c1 = 0
c2 = 1

c1.increment(c1)
c1.increment(c1)
c2.increment(c2)

print(c1.count)  
print(c2.count)  

