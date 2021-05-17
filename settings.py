class SettingsClass:
    def __init__(self):
        self.mul_symbol = " \\cdot "
        self.big_frac = True
        self.big_brac = True

    def set_mul_symbol(self, symbol: str):
        self.mul_symbol = " " + symbol + " "

    def get_mul_symbol(self):
        return self.mul_symbol

    def set_big_frac(self):
        self.big_frac = True

    def set_small_frac(self):
        self.big_frac = False

    def get_frac(self):
        if self.big_frac:
            return " \\displaystyle\\frac "
        else:
            return " \\frac "

    def set_big_brac(self):
        self.big_brac = True

    def set_small_brac(self):
        self.big_brac = False

    def get_left_brac(self):
        if self.big_brac:
            return " \\left( "
        else:
            return " ( "

    def get_right_brac(self):
        if self.big_brac:
            return " \\right) "
        else:
            return " ) "


Settings = SettingsClass()
