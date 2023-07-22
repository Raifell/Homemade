def convertor(val, count):
    value_1 = 0
    value_2 = 0
    if val == 1:
        value_1 = count * 1.8 + 32
        value_2 = count + 273.15
    elif val == 2:
        value_1 = (count - 32) / 1.8
        value_2 = (count + 459.67) / 1.8
    elif val == 3:
        value_1 = count - 273.15
        value_2 = count * 1.8 - 459.67

    return value_1, value_2
