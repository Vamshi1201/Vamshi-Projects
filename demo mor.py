'method overriding'
class parent:
    def bike(self):
        print("i have passion pro bike")

class child(parent):
    def bike(self):
        print("i have a pulsar 220cc bike")

obj = child()
obj.bike()
