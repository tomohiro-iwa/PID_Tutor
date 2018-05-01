import pdb
import Truck
import matplotlib.pyplot as plt

class Pctrl:
    def __init__(self,Kp):
        self.Kp = Kp

    def act(self,diff):
        return self.Kp * diff


class Ictrl:
    def __init__(self,Ki,t_step):
        self.Ki = Ki
        self.integral = 0
        self.befor_diff = 0
        self.t_step = t_step

    def act(self,diff):
        trape = (self.befor_diff+diff)/2 * self.t_step
        #pdb.set_trace()
        self.integral += trape
        self.befor_diff = diff
        return self.Ki * self.integral


class Dctrl:
    def __init__(self,Kd):
        self.Kd = Kd

    def act(self,speed):
        return self.Kd * speed

def make_data(data_id):
    truck = Truck.Truck()
    pctrl = Pctrl(0.001)
    ictrl = Ictrl(0.001, 0.01)
    dctrl = Dctrl(0.01)

    goal = 30
    data = []
    for _ in range(10000):
        diff = goal - truck.pos
        energy = pctrl.act(diff)
        if data_id == 1:
            energy += ictrl.act(diff)
        energy -= dctrl.act(truck.speed)

        truck.accel(energy)

        pos = truck.step()
        print(pos)
        data.append(truck.pos)
    
    return data


if __name__ == "__main__":
    data = []
    data.append(make_data(0))
    data.append(make_data(1))

    plt.plot(data[0],label="0")
    plt.plot(data[1],label="1")
    plt.legend()

    plt.ylabel("pos")
    plt.show()

    #acc(t) - ref(t) = 
