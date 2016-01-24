from __future__ import print_function

from knockoutpy.property import HasProperties, InputProperty, ComputedProperty
from knockoutpy.property import computed_property, on_change


class Test(HasProperties):
    a = InputProperty(5)

    @computed_property
    def b(self):
        return self.a * 2

    @computed_property
    def c(self):
        return self.a + 3

    @computed_property
    def d(self):
        return self.b + self.c

    @on_change(d)
    def print_value(self, observable):
        print('Test.print_value: {} value changed to {}'
              .format(observable.name, observable.value))


def print_value(o):
    print('print_value: {} value changed to {}'.format(o.name, o.value))


def print_values(obj, *names):
    for n in names:
        print('{} = {}'.format(n, getattr(obj, n)))


if __name__ == '__main__':
    t = Test()

    t.observe.a.on_change(print_value)
    t.observe.b.on_change(print_value)
    t.observe.c.on_change(print_value)
    t.observe.d.on_change(print_value)

    print_values(t, 'a', 'b', 'c', 'd')

    t.a = 7

    print_values(t, 'a', 'b', 'c', 'd')
