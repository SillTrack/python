class Road:
    def __init__(self, Road_length, Road_width):
        self.__length = Road_length
        self.__width = Road_width
        print('Длина', self.__length, 'и ширина дороги:', self.__width)
    def weigth_calculation(self, asphalt_mass, layer_width):
        return asphalt_mass*layer_width*self.__length*self.__width


road = Road(20, 5000)
print('Масса асфальта, при заданных условиях', road.weigth_calculation(25, 5))
