def entropy_formula(pk):
    import math
    return -sum([p*math.log(p,2) for p in pk])