class India():
    def capital(self):
        print("Capital of india is New Delhi")

    def Lang(self):
        print("Language spoken in india =Hindi")

    def type(self):
        print("india is a developing country")


class America():
    def capital(self):
        print("Capital of America is USA")

    def Lang(self):
        print("Language spoken in America =English")

    def type(self):
        print("USA is a developed country")

def func(obj):
    obj.capital()
    obj.Lang()
    obj.type()

a=India()
b=America()

func(a)
func(b)