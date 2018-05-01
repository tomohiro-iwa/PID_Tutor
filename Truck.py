
class Truck:
    def __init__(self):
        self.pos = 0
        self.mass = 1 #Kg
        self.friction_c = 0.1
        self.gravity_a = 9.80665
        self.speed = 0
        self.t_step = 0.01

    def slow_down(self):
        speed = abs(self.speed)

        sign = 1
        if self.speed < 0:
            sign = -1

        vertical_f = self.mass * self.gravity_a
        friction_f = self.friction_c * vertical_f
        new_abs_speed = speed - (friction_f * self.t_step)

        if new_abs_speed > 0:
            self.speed = sign * new_abs_speed
        else:
            self.speed = 0

    def move_foward(self):
        self.pos += self.speed * self.t_step

    def step(self):
        self.move_foward()
        self.slow_down()
        return self.pos

    def accel(self,energy):
        self.speed += energy


