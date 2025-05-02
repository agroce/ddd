def minandmax(values):
    if not values:
        return (None, None)
    min_v = values[0]
    max_v = values[0]
    for v in values:
        if v < min_v:
            min_v = v
        if v > max_v:
            max_v = v
    return (min_v, max_v)
