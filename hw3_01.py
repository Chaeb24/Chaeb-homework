discount_rate = 0

def set_rate(rate):
    global discount_rate
    discount_rate = rate

def get_rate():
    return discount_rate

def to_Athing(Awon):
    return Awon * (100 / (100 - discount_rate))

def to_Bthing(Bwon):
    return Bwon * (100 / (100 - discount_rate))
