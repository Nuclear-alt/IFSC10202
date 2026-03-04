def ParseDegreeString(ddmmss):
    degree_symbol = chr(176)

    degree_pos = ddmmss.find(degree_symbol)
    minute_pos = ddmmss.find("'")
    second_pos = ddmmss.find('"')

    degrees = ddmmss[:degree_pos]
    minutes = ddmmss[degree_pos + 1:minute_pos]
    seconds = ddmmss[minute_pos + 1:second_pos]

    degrees = float(degrees)
    minutes = float(minutes)
    seconds = float(seconds)

    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minytes, seconds):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

