# decorators - wraper function around the functions are called as decorators
# decorator method

def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return  inner

@make_pretty
def vanilacake():
    print("I am the vanilla cake")

@make_pretty
def straberrycake():
    print("I am the strawberry cake")

vanilacake()
straberrycake()





