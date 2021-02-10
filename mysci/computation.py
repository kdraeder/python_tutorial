def compute_windchill(t, v):
    """
    Compute the wind chill factor, given the T and wind speed
    NOTE; valid for -45 F <T < +45 F
                    3mph  < wind < 60 mph
    Paramters: 
        t: Tempertatureunits of F (float)
        v: wind speed units mph (float)
    """
    # constants
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    # new variable
    v16 = v **0.16

    wci = a + (b*t) - (c * v16) + (d * t * v16)
    return wci


# Calc heat index
# Use verbs for function names.
def compute_heatindex(t, hum):
    """
    Compute the heat index, given T and humidity
    Parameters:
        t: Temp units F (float)
        hum: rel humidity units % (float)
    """
    # constants
    a = -42
    b = 2
    c = 10
    d = 0.22
    e = 0.0068
    f = 0.0048
    g = 0.0012
    h = 0.00085
    i = 0.000002

    # new variable
    rh = hum / 100
    hi = (a + (b * t) + (c * rh) + (d * t * rh) + (e * t ** 2) + 
          (f * rh ** 2) + (g * rh * t ** 2) + (h * t * rh ** 2) +
          (i * t ** 2 * rh ** 2))
    return hi

