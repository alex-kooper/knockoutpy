from .observable import InputValue, ComputedValue


class Observables(object):

    def __init__(self, parent):
        self.parent = parent

    def __getattr__(self, name):
        descriptor = getattr(type(self.parent), name)
        o = descriptor.new_observable(self.parent)
        setattr(self, name, o)
        return o


class HasProperties(object):

    @property
    def observe(self):
        try:
            return self._observe
        except AttributeError:
            self._observe = Observables(self)
            self._fix_property_names()
            return self._observe

    @classmethod
    def _fix_property_names(cls):
        for name in dir(cls):
            p = getattr(cls, name)

            if isinstance(p, PropertyDescriptor) and not p.name:
                p.name = name


class PropertyDescriptor(object):

    def __init__(self, name=None):
        self.name = name
        self._subscribers = set()

    def __get__(self, obj, type_=None):
        if not obj:
            return self

        return getattr(obj.observe, self.name).value

    def __set__(self, obj, value):
            getattr(obj.observe, self.name).value = value

    def subscribe(self, *functions):
        self._subscribers |= set(functions)

    on_change = subscribe

    def new_observable(self, obj):
        o = self._create_observable(obj)

        for f in self._subscribers:
            o.on_change(f.__get__(obj))

        return o

    def _create_observable(self, obj):
        raise NotImplementedError()


class InputProperty(PropertyDescriptor):

    def __init__(self, value=None, name=None):
        super(InputProperty, self).__init__(name)
        self.value = value

    def _create_observable(self, obj):
        return InputValue(self.value, self.name)


class ComputedProperty(PropertyDescriptor):

    def __init__(self, f, name=None):
        super(ComputedProperty, self).__init__(name)
        self.f = f

    def _create_observable(self, obj):
        return ComputedValue(self.f.__get__(obj), self.name)


computed_property = ComputedProperty
