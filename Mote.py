from MoteController import MoteController
from Twinkle import Twinkle

if __name__ == '__main__':
    controller = MoteController()
    controller.run([Twinkle()])
