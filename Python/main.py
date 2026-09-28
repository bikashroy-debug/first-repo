# Question1: Enter a number and show the square value using a static variable.
class Number:
    n=0
    def square(self):
        print("square =", Number.n * Number.n)

Number.n=int(input("Enter a number: "))

object= Number()
object.square()



# Question2: Show addition of two numbers using global and local variables.
a=10

class Addition:
    def show(self):
        b=20
        c=a+b
        print("Addition =", c)

obj=Addition()
obj.show()   



# Question3: Show actual value, square value and cube value using the same function name.
class Number:
    def show(self, n, choice):
        if choice==1:
            print("Actual Value = ", n)

        elif choice==2:
            print("Square Value = ", n*n)

        elif choice==3:
            print("Cube Value = ", n*n*n)

obj=Number()

n=int(input("Enter a number:"))

obj.show(n,1)
obj.show(n,2)
obj.show(n,3)




# Quetion4: enter any number from the user and show the square value, cube value and actual value 
# of that number using different functions. The functions must be user-defined and have the same name.
class Actual:
    def show(self,n):
        print("Actual Value =",n)

class Square:
    def show(self,n):
        print("Square Value =",n*n)

class Cube:
    def show(self,n):
        print("Cube Value =",n*n*n)


n=int(input("Enter a number: "))

obj1 = Actual()
obj2 = Square()
obj3 = Cube()

obj1.show(n)
obj2.show(n)
obj3.show(n)



