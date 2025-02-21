for a in range(1,31):
    for b in range(a,31):
        c = math.sqrt(a**2 + b**2)
        if c.isinteger() and c<=30:
            print(f"({a}, {b}, {int(c)})")
