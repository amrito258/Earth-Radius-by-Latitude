import math


def calculate_radius(latitude_degree):

    r1 = 6378.137
    r2 = 6357.752
    B = math.radians(latitude_degree)

    a = (r1**2 * math.cos(B))**2
    b = (r2**2 * math.sin(B))**2
    x = math.sqrt(a + b)

    m = (r1 * math.cos(B))**2
    n = (r2 * math.sin(B))**2
    y = math.sqrt(m + n)

    R = x / y
    return R


latitude_degree = float(input('Enter the latitude (°): '))
radius = calculate_radius(latitude_degree)
print(f'The earth radius of your location is {radius}km')
