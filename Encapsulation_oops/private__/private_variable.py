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