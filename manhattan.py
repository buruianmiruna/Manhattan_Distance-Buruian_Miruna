#import functia cityblock din biblio scipy
from scipy.spatial.distance import cityblock

def manhattan_manual(x, y):
    #fct care calc distanta manhattan manual intre doi vect x, y
    #initializ var dist cu 0, aici vom aduna diferentele absolute
    dist = 0
    #parcurg fiecare poz din vector
    for i in range(len(x)):#nr de elem din vect(len(x))
        dist += abs(x[i] - y[i])#calc dif dintre elem coresp si fol abs() ca sa obtinem val abs
    return dist


def manhattan_scipy(x, y):
    #fct care calc dist manhattan fol cityblock din scipy
    #apelam fct din biblioteca si returnam rezultatul
    return cityblock(x, y)