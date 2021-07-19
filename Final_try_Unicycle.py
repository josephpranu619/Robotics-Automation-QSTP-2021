import numpy as np
import matplotlib.pyplot as plt
import math

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt
        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):

        for i in range(0,n):
            self.x = self.x + v * np.cos(self.theta)*self.dt
            self.y = self.y + v * np.sin(self.theta)*self.dt
            self.theta = self.theta + w*self.dt
            self.x_points.append(self.x)
            self.y_points.append(self.y)
        return self.x, self.y, self.theta

    def plot(self, v: float, w: float,name:str):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        #plt.show()
        plt.savefig(name)
        # plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":
    print("Unicycle Model Assignment")
    path1 = Unicycle(0,0,0,0.1)
    v,w,theta = path1.step(1,0.5,25)
    path1.plot(v,w,"1.jpg")
    path2 = Unicycle(0, 0, 1.57,0.2)
    v,w,theta = path2.step(0.5,1,10)
    path2.plot(v,w,"2.jpg")
    path3 = Unicycle(0, 0, 0.77,0.05)
    v,w,theta = path3.step(5,4,50)
    path3.plot(v,w,"3.jpg")