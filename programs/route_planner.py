def convert(string):
    li = list(string.split(" "))
    return li


def route(peaks):
    peaks = convert(peaks)
    current_peak = peaks[0]
    nexter_peak = peaks[2]
    next_peak = peaks[1]
    path = []
    # for i in range(1, len(peaks)-1):


route('0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15')
