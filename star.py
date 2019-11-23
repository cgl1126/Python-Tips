"""Star use, * and **
"""

def math_use(a, b):
    """
    res_product1 is a times b.
    res_product2 is a squared times b.
    """
    res_product1 = a * b
    print("{} * {} = {}".format(a, b, res_product1))
    if isinstance(a, int):
        res_product2 = a ** b
        print("{0} ** {1} = {2}".format(a, b, res_product2))


def arg_use():
    """
    args is non-key argument.
    kwargs is keyword argument.
    """
    def args_use(*args):
        # The different of  args and *args.
        print("*args value is {}".format(*args)) 
        print("args value is {}".format(args))
        for arg in args:
            print(arg)
    def kwargs_use(*args, **kwargs):
        # *kwargs get kwargs key(s)
        print("*kwargs value is %s", *kwargs)
        print("kwargs value is %s, type is %s" %(kwargs, type(kwargs)))
        for kwarg in kwargs:
            print(kwarg)
    arg_str = "abc"
    arg_list = [1, 2, 3]
    arg_dict = {'name': "Cai", 'age': 24}
    args_use(arg_str, arg_list)
    kwargs_use(arg_str, arg_dict, user='CAI', id=23)
    kwargs_use(arg_str, **{'name': "Cai", 'age': 24}, user='CAI', id=23)

def other_use():
    arg_str = "aBcDe"
    arg_list = [1, 2, 3, 4]
    arg_dict = {'No': 123, 'price': 10, 'name': 'apple'}
    def args_use(*args):
        print(args)
        for arg in args:
            print(arg, end='=|')
        print()
    def kwargs_use(**kwargs):
        print(kwargs)
        for key, value in kwargs.items():
            print("{} : {}".format(key, value))
    # new = (*arg_list) wrong use

    args_use(*arg_list)
    args_use(*arg_str)
    args_use(*arg_dict) # only can get key but value
    kwargs_use(**arg_dict) # key point

def mix_use(a, b=0, *c, x, **y):
    print('{}, {}，{}, {}, {}'.format(a, b, c, x, y))


def main():
    math_use(2, 5)
    math_use("+hello+", 5)
    arg_use()
    other_use()
    mix_use('A', 8, 'cm', ('a', 'p', 'p'), [1, 3, 1, 4], {'id': 1, 'price': 2}, name='CAI', x='xXx', y=1, z="endZ")
    a, *_, b = 1, 2, 3, 4, 5
    print(a, b)

if __name__ == "__main__":
    main()