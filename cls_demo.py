
out = 'out'
other = 'other out'
class MyDemo:
    cls_arg = 1
    def __init__(self, name, age):
        self._name = name
        self._age = age
        out = 'in __int__'
        print(out, other)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


def main():
    print(MyDemo.cls_arg)
    MyDemo.cls_arg = 8
    mydemo1 = MyDemo("Lucy", 18)
    mydemo2 = MyDemo('John', 24)

    print(mydemo1.cls_arg, mydemo1.get_name())
    print(mydemo2.cls_arg, mydemo2.get_name())

    print(MyDemo.__dict__)
    print(mydemo1.__dict__)

if __name__ == "__main__":
    main()