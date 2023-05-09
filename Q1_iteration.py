def cmplx_iter(x, y):
    z_0 = 0
    c = complex(x, y)
    i = 1
    while i < 100:
        if abs(z_0.real) < 1e154 and abs(z_0.imag) < 1e154:
            z_1 = z_0**2 + c
            if z_1 == z_0:
                break
            z_0 = z_1
            i += 1

        else:
            break

    return (z_0, i)