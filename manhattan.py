from scipy.spatial.distance import cityblock

def manhattan_manual(x, y):
    """
    Calculează distanța Manhattan manual.
    """
    dist = 0
    for i in range(len(x)):
        dist += abs(x[i] - y[i])
    return dist


def manhattan_scipy(x, y):
    """
    Calculează distanța Manhattan folosind scipy.
    """
    return cityblock(x, y)