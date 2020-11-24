# class for Clicks objects used in clickTrackGUI.py

class Clicks:
    def __init__(self, leftClicks=0, rightClicks=0, totalClicks=0):
        self.public_leftClicks = leftClicks
        self.public_rightClicks = rightClicks
        self.public_totalClicks = totalClicks

    def get_left(self):
        return self.public_leftClicks

    def set_left(self, lc):
        self.public_leftClicks = lc

    def get_right(self):
        return self.public_rightClicks

    def set_right(self, rc):
        self.public_rightClicks = rc

    def get_total(self):
        return self.public_totalClicks

    def set_total(self, tc):
        self.public_totalClicks = tc

    def increment_left(self):
        self.public_leftClicks += 1

    def increment_right(self):
        self.public_rightClicks += 1

    def increment_total(self):
        self.public_totalClicks += 1
