from mote import Mote

class MoteController:
    def __init__(self):
        self.mote = Mote()

        gammaCorrection = False
        self.mote.configure_channel(1, 16, gammaCorrection)
        self.mote.configure_channel(2, 16, gammaCorrection)
        self.mote.configure_channel(3, 16, gammaCorrection)
        self.mote.configure_channel(4, 16, gammaCorrection)

    def run(self, programs):
        while True:
            for program in programs:
                program.run(self.mote)
