from knockoutpy.property import HasProperties, InputProperty, ComputedProperty


class Test(HasProperties):
    a = InputProperty(5, 'a')

    b = ComputedProperty(lambda self: self.a * 2, 'b')
    c = ComputedProperty(lambda self: self.a + 3, 'c')


if __name__ == '__main__':
    t = Test()

    def print_value(o):
        print('{} value changed to {}'.format(o.name, o.value))

    t.observe.a.on_change(print_value)
    t.observe.b.on_change(print_value)
    t.observe.c.on_change(print_value)

    print('a = {}'.format(t.a))
    print('b = {}'.format(t.b))
    print('c = {}'.format(t.c))

    t.a = 7

    print('a = {}'.format(t.a))
    print('b = {}'.format(t.b))
    print('c = {}'.format(t.c))

