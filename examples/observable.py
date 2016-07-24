from kopy.observable import InputValue, ComputedValue


def print_value(o):
    print('{} value changed to {}'.format(o.name, o.value))


def print_values(*values):
    for v in values:
        print('{} = {}'.format(v.name, v.value))

if __name__ == '__main__':
    a = InputValue(5, 'a')

    b = ComputedValue(lambda: a.value * 2, 'b')
    c = ComputedValue(lambda: a.value + 3, 'c')
    d = ComputedValue(lambda: b.value + c.value, 'd')
    e = ComputedValue(lambda: a.value + d.value, 'e')

    a.on_change(print_value)
    b.on_change(print_value)
    c.on_change(print_value)
    d.on_change(print_value)
    e.on_change(print_value)

    print_values(a, b, c, d, e)

    a.value = 7

    print_values(a, b, c, d, e)

