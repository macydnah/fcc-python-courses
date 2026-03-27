import copy
import random

class Hat:
    contents: list[str]

    def __init__(self, **balls_per_color: int) -> None:
        self.contents = Hat._dict_to_contents(balls_per_color)

    def draw(self, balls: int) -> list[str]:
        drawn: list[str] = []

        if balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
        else:
            for _ in range(balls):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn.append(ball)

        return drawn

    @staticmethod
    def _dict_to_contents(balls_per_color: dict[str, int]) -> list[str]:
        contents: list[str] = []
        for color, cuantas in balls_per_color.items():
            for _ in range(cuantas):
                contents.append(color)

        return contents

def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    exitos = 0
    for _ in range(num_experiments):
        matches = True
        _hat = copy.deepcopy(hat)
        drawn = _hat.draw(num_balls_drawn)

        for color, cuantas in expected_balls.items():
            if cuantas > drawn.count(color):
                matches = False
                break

        if matches:
            exitos += 1

    return exitos/num_experiments

def ejemplo():
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(
        hat=hat,
        expected_balls={'red':2,'green':1},
        num_balls_drawn=5,
        num_experiments=2000
    )
    print(f"{probability}")

if __name__ == '__main__':
    ejemplo()
