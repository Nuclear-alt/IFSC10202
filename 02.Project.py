from math import pi, sin, cos, acos
EnterRadiusofSphere = 6371

S1 = Latitude = 52
S2 = Latitude = 41
E1 = Longitude = 21
E2 = Longitude = 12

S1 = S1 * pi / 180
S2 = S2 * pi / 180
E1 = E1 * pi / 180
E2 = E2 * pi / 180

d = EnterRadiusofSphere * acos(
    sin(E1) * sin(E2) +
    cos(E1) * cos(E2) * cos(S1 - S2))
d = round(d, 2)
print("The Great Circle Distance is:", d)