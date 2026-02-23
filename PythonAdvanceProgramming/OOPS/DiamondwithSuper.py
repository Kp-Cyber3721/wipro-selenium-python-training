class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("class B")
class C(A):
    def show(self):
        super().show()
        print("class C")

class D(B, C):
    def show(self):
        super().show()
        print("Class D")

d=D()
d.show()
print(D.mro())



