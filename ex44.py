class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD before PARENT altered()"
        super(Child, self).altered()
        print "CHILD after PARENT altered()"

dad = Parent()
son = Child()

dad.override()
son.override()

dad.implicit()
son.implicit()

dad.altered()
son.altered()
