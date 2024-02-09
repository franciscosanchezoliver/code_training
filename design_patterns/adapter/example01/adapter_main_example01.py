from abc import ABCMeta, abstractmethod


class IA(metaclass=ABCMeta):
    """
    This class represent the interface of the class A
    """

    @abstractmethod
    def method_a(self):
        """
        Method that should be implemented in class A
        """


class A(IA):
    """
    Class that implements the interface IA
    """

    def method_a(self):
        print("method_a in class A")


class IB(metaclass=ABCMeta):
    """
    This class represents the interface of the class B
    """

    @abstractmethod
    def method_b(self):
        """
        Method that should be implemented in class B
        """


class B(IB):
    """
    Class that implements the interface IB
    """

    def method_b(self):
        print("method_a in class B")


# At first, if we create 2 objects from the classes A and B, the method
# are not the same.

a = A()
b = B()

a.method_a()
b.method_b()


# So both classes are incompatible, to make them compatible we need an
# intermediate class "Adapter"


class BAdapter(IA):
    """
    This class makes the class B compatible with the class A
    """

    def __init__(self) -> None:
        self.b = B()

    def method_a(self):
        """
        This method has the same signature as the IA, so its compatible with
        class A.

        However we are calling method_b from class B. So we are making both
        interfaces compatible with this intermediate class
        """
        print("Invoked method_b by calling method_a from the adapter class")
        self.b.method_b()


a = A()
b = B()
b_adapted = BAdapter()

a.method_a()
b.method_b()

b_adapted.method_a()
