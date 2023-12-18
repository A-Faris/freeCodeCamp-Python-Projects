import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = list()
        for ball,num in balls.items():
            for i in range(num):
                self.contents.append(ball)

    def draw(self, num):
        if num < len(self.contents):
            self.balls_drawn = list()
            for i in range(num):
                self.contents.remove(random.choice(self.contents))
                self.balls_drawn.append(random.choice(self.contents))
            return sorted(self.balls_drawn)
        else:
            return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        picked = copy.deepcopy(hat)
        picked.draw(num_balls_drawn)
        n = copy.copy(expected_balls)
        for i in picked.balls_drawn:
            if n.get(i) != None and n.get(i) != 0:
                n[i] -= 1
        if sum(n.values()) == 0:
            M += 1
    return M/num_experiments

hat = Hat(blue=3,red=2,green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue":2,
                    "green":1},
    num_balls_drawn=4,
    num_experiments=1000)
print("Probability:", probability)