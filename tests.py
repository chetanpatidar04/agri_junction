class Index():
    # msg = False
    def __init__(self):
        self.msg = False

    def post1(self):
        self.msg = True
        print(self.msg)
        return self.msg    

    def get1(self):
        print(self.msg)
        return self.msg


s1 = Index()
s1.post1()
s1.get1()