import search #importing my own py-script

def linterp(n, x, y, z):
    i = search.half_int(n, x, z) #z is a point in the list x
    p = (y[i+1] - y[i]) / (x[i+1] - x[i])
    dx = z-x[i]
    res = y[i] + p*dx
    return res

def integ_linterp(n, x, y, z):
    integ = 0
    end_integ = search.half_int(n, x, z)

    for i in range(end_integ):
        dx = x[i+1] - x[i]
        p = (y[i+1]-y[i]) /dx
        integ = integ + y[i]*dx + 0.5*p*dx**2
    
    dx = z - x[end_integ]
    p = (y[end_integ+1] - y[end_integ]) / (x[end_integ+1] - x[end_integ])
    integ = integ + y[end_integ]*dx + 0.5*p*dx**2

    return integ