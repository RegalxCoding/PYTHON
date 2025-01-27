
def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thank you for using this function")
    mfx()

@greet
def hello():
    print("this is hello fun")