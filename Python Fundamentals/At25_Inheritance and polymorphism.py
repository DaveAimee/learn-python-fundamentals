class Animal(object):
    def run(self):
        print('Animal is running...')

# Dog 和 Cat继承了Animal
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

# 当子类和父类都存在相同的run()方法时，
# 我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。

