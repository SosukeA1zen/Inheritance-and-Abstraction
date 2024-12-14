from abc import ABC, abstractmethod


class Animal(ABC):

    def move(self):
            pass
    

class Human(Animal):
      
      def move(self):
              print("I can walk and run")

class snake(Animal):
        
        def move(self):
               print("I can crawl")

R=Human()
R.move()

K=snake()
K.move()


