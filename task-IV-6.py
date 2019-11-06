class Furniture:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        self.string = string = ''.join(str(list(self.kwargs)).strip('[').strip(']'))

    def getFurniture(self):
        print(f'Общая площядь {self.getSizeHouse()}, Остальная площять {self.getHouseArea()}, вся мебель: {self.string}')

    def getSizeHouse(self):
        return self.kwargs['sizeHouse']

    def getHouseArea(self):
        otherHouseSize = self.kwargs['whichBed'] - self.kwargs['metersWardrobe'] - self.kwargs['metersTable']
        return float(otherHouseSize)

f1 = Furniture(sizeHouse = 10, whichBed = 4, metersWardrobe = 2, metersTable = 1.5)
f1.getFurniture()
