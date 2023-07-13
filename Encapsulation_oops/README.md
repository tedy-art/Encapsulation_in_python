**Encapsulation** :- </br>
-> Wrapping of data and methods together in oe entity(class) is called encapsulaton.</br>
</br>
    Encapsulation ----> information hiding
</br>

-> You can hide internal state of object from outside. This is known as information hiding.

**Access modifiers in Python :-**</br>
-> Access modifirers linit access to the variable and methods of a class</br>
-> Python provides **three types of access modifiers** </br>
        1) Public Member-</br>
            -> Accessible anywhere from the outside class.</br>
        2) Private Member-</br>
            -> Accessible in within the class.</br>
        3) Protected Member-</br>
            -> Accessible within the class and it's sub-class.</br>

**1) Public Member:-**
e.g.

    class Counter:
        def __init__(self):
            self.count = 0

        def inc_count(self):
            self.count += 1

        def dec_count(self):
            self.count -= 1

        def display_count(self):
            print(self.count)

    c1 = Counter()
    c1.display_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.display_count()
    c1.dec_count()
    c1.dec_count()
    c1.dec_count()
    c1.display_count()
    c1.count = 777
    c1.inc_count()
    c1.display_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.display_count()

O/p-

    0
    7  
    4  
    778
    781


**Private Member :-**</br >
    Private Variable:-</br>
        -> A varible which is accessed inside class only.</br>
        -> We can access private variable from outside by using object referance.</br>

    sty:- </br>

        __count = 0

    e.g.

    class Counter:
        def __init__(self):
            self.__count = 0

        def inc_count(self):
            self.__count += 1

        def dec_count(self):
            self.__count -= 1

        def display_count(self):
            print(self.__count)

    c1 = Counter()
    c1.display_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.display_count()
    c1.dec_count()
    c1.dec_count()
    c1.dec_count()
    c1.display_count()
    c1.__count = 777 # Error
    c1.inc_count()
    c1.display_count()
    c1.inc_count()
    c1.inc_count()
    c1.inc_count()
    c1.display_count()

o/p

    0
    7
    4
    5
    8

</br>
Private members are accessible only within the class, and we can’t access them directly from the class objects.</br>

Example:</br>

    class Employee:
        # constructor
        def __init__(self, name, salary):
            # public data member
            self.name = name
            # private member
            self.__salary = salary

    # creating object of a class
    emp = Employee('Jessa', 10000)

    # accessing private data members
    print('Salary:', emp.__salary)

o/p

    AttributeError: 'Employee' object has no attribute '__salary'

We can access private members from outside of a class using the following two approaches </br>

1) Create public method to access private members</br>
2) Use name mangling </br>

**Public method to access private members**</br>
Example: Access Private member outside of a class using an instance method</br>

    class Employee:
        # constructor
        def __init__(self, name, salary):
            # public data member
            self.name = name
            # private member
            self.__salary = salary

        # public instance methods
        def show(self):
            # private members are accessible from a class
            print("Name: ", self.name, 'Salary:', self.__salary)

    # creating object of a class
    emp = Employee('Jessa', 10000)

    # calling public method of the class
    emp.show()

o/p:-

    Name: Jessa Salary: 10000

**Name Mangling to access private members**</br>
Example: Access private member</br>

    class Employee:
        # constructor
        def __init__(self, name, salary):
            # public data member
            self.name = name
            # private member
            self.__salary = salary

    # creating object of a class
    emp = Employee('Jessa', 10000)

    print('Name:', emp.name)
    # direct access to private member using name mangling
    print('Salary:', emp._Employee__salary)

o/p:

    Name: Jessa
    Salary: 10000

