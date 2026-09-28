# # Question1: Enter a number and show the square value using a static variable.
class Number:
    n=0
    def square(self):
        print("square =", Number.n * Number.n)

Number.n=int(input("Enter a number: "))

object= Number()
object.square()



# # Question2: Show addition of two numbers using global and local variables.
a=10

class Addition:
    def show(self):
        b=20
        c=a+b
        print("Addition =", c)

obj=Addition()
obj.show()   



# # Question3: Show actual value, square value and cube value using the same function name.
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




# # Quetion4: enter any number from the user and show the square value, cube value and actual value 
# # of that number using different functions. The functions must be user-defined and have the same name.
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


# Question5: Show addition result of three numbers using only protected data members of a class.

class addition:
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
    def add(self):
        result =self._a+self._b+self._c
        print("Addition value= ", result)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

obj=addition(a,b,c)
obj.add()


# Question6: Show addition result of three numbers using only private data members of a class.

class addition :
    def __init__(self, a, b):
        self.__a=a
        self.__b=b

    def add(self):
        result=self.__a +self.__b
        print("Addition Value =", result)


a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

obj= addition(a,b)
obj.add()


# Question7: Enter a single input and check whether it is alphabet, digit or special symbol using a class method.

class checking:
    def show(self, ch):
        if ("A"<= ch <="Z") or ("a"<= ch <="z"):
          print("Alphabet")

        elif("0"<=ch<="9"):
           print("Digit")

        else:
           print("Special symbol")

ch=input("Enter any Charachter : ")

obj=checking()
obj.show(ch)


# Question8.enter any two numbers from the user and show the addition result and division result of that number using different class methods.

class Number:
    def addition(self,a,b):
    #   result=a+b
      print("Addition Value= ",a+b)

    def division(self,a,b):
       if b!=0:
        #   result=a/b
          print("Division Value= ",a/b)

       else:
          print("Division by 0 is not possible")

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))


obj=Number()

obj.addition(a,b)
obj.division(a,b)


# 9. Same as Question 8 but using different class methods with the same name.

class Addition:
   def show(self,a,b):
      print("Addition Value = ",a+b)
class Division:
   def show(self,a,b):
      if b!=0:
         print("Division Value = ",a/b)
      else:
         print("The division by 0 is not possible")

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))


obj1 = Addition()
obj2 = Division()

obj1.show(a,b)
obj2.show(a,b)


# Question10. show the addition result of three different numbers with a single-parameter class method.

class Addition:
   def __init__(self, a,b):
      self._a = a
      self._b = b

   def show(self, c):
      result=self._a + self._b + c
      print("Addition Value : ", result)

a=int(input("Enter 1st number= "))
b=int(input("Enter 2nd number= "))
c=int(input("Enter 3rd number= "))


obj=Addition(a,b)

obj.show(c)