class A:
    def p(self):
        print('A.p')


class B(A):
    def p(self):
        print('B.p')
        super().p(self)
        super(B, self).p(self)


a = A
a.p(a)

b = B
b.p(b)
