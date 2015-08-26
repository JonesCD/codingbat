def front_times(str, n):
    if len(str) > 2:
        return n * str[:3]
    else:
        return n * str