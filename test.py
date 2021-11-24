from itertools import count
from sim import SimpleSimulator

def main():
    sim = SimpleSimulator()

    for i in range(2):
        sim.reset()
        for t in count(start=1):
            action = True if (t % 20) == 0 else False
            print(t, action)
            if action:
                sim.apply_spacebar_action()
            sim.render()

            if t == 200:
                break
        
    sim.close()

if __name__ == "__main__":
    main()
