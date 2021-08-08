
class PyObj:

    c = 10
    meet = 2

    def exe(self):
        self.c = 11
        self.meet = 1
        return self.c


    def exe2(self):
        c = 11
        return c