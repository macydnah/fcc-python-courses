import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, starting_speed, starting_height, starting_angle):
        self.__speed = starting_speed
        self.__height = starting_height
        self.__angle = math.radians(starting_angle)

    def __str__(self):
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {round(self.angle)}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __repr__(self):
        return f'{self.__class__.__name__}({self.speed}, {self.height}, {self.angle})'

    def __calculate_displacement(self):
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    def __calculate_y_coordinate(self, x):
        y = self.__height 
        y += x * math.tan(self.__angle)
        y -= (GRAVITATIONAL_ACCELERATION * x**2) / (2 * self.__speed**2 * math.cos(self.__angle)**2)

        return y

    def calculate_all_coordinates(self):
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @angle.setter
    def angle(self, new_angle):
        self.__angle = math.radians(new_angle)

class Graph:
    __slots__ = ('__coordinates')

    def __init__(self, coordinates):
        self.__coordinates = coordinates

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__coordinates})'

    def create_coordinates_table(self):
        table = f'\n{"x":>3} {"y":>6}\n'
        for x, y in self.__coordinates:
            table += f'{x:>3} {y:>6.2f}\n'
        return table

    def create_trajectory(self):
        rounded_coords = [(round(x, None), round(y, None)) for x, y in self.__coordinates]

        x_max = max(x for x, _ in rounded_coords)
        y_max = max(y for _, y in rounded_coords)

        matrix_list = [[' ' for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[y_max - y][x] = PROJECTILE
        for row in range(len(matrix_list)):
            matrix_list[row] = [y_axis_tick] + matrix_list[row]

        x_axis_list = [' '] + [x_axis_tick] * (x_max + 1)
        matrix_list.append(x_axis_list)

        matrix = ["".join(row) for row in matrix_list]

        final_output = f'\n'
        for item in matrix:
            final_output += f'{item}\n'

        matrix = final_output

        return matrix

def projectile_helper(starting_speed, starting_height, starting_angle):
    projectile = Projectile(starting_speed, starting_height, starting_angle)

    coordinates = projectile.calculate_all_coordinates()
    graph = Graph(coordinates)
    coordinates_table = graph.create_coordinates_table()

    trajectory = graph.create_trajectory()

    print(projectile)
    print(coordinates_table)
    print(trajectory)

if __name__ == '__main__':
    projectile_helper(10, 3, 45)
