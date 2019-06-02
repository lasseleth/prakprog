def half_int(n, x, z):
    # n is the dimension of x (list)
    # z is a point between the first and last element of x
    it = int(0); # iteration number
    L = int (0); 
    R = int(n-1)

    if (L > R):
        print("Error, list must be longer\n")
        return -1

    while (L <= R):
        # Search for the interval in which z belongs
        m = int((L+R)/2)

        if (x[m] <= z and x[m+1] > z):
            return m
        elif (x[m] < z):
            L = m + 1
        elif (x[m] > z):
            R = m - 1
        it = it + 1
        if (it > n):
            print("Search was not succesful.\n")
            return -1
            break