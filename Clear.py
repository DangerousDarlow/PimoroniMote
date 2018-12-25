from mote import Mote

if __name__ == "__main__":
    mote = Mote()
    gammaCorrection = False
    mote.configure_channel(1, 16, gammaCorrection)
    mote.configure_channel(2, 16, gammaCorrection)
    mote.configure_channel(3, 16, gammaCorrection)
    mote.configure_channel(4, 16, gammaCorrection)
    mote.clear()
    mote.show()