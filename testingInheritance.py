class Furniture:
    def __init__(self,name="22ss", type = ''):
        self.name = name
        self.type = type

class Table(Furniture):
    def __init__(self, name='X091', type='study'):
        self.name = name
        self.type = type
    def Tabledef(self, name, type, color):
        self.name = name
        self.type = type
        self.color = color
    def printAll(self):
        print("name %s , type %s, color %s " % (self.name, self.type, self.color))


tabObj = Table()
Table.__init__(tabObj)

print(tabObj.name)
print(hasattr(Table,'name'))
print(issubclass(Table,Furniture))
