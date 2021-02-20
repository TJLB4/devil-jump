def spike(x, y, h=20, w=20):
    """ Draws 3 spikes starting at x,y with height 20 and wdith 20 """
    return ((x, y), (x+w, y-h), (x+2*w, y), (x+3*w, y-h), (x+4*w, y), (x+5*w, y-h), (x+6*w, y))