from math import ceil, sqrt

def get_participants(handshakes):
    return ceil((1 + sqrt(1+8*handshakes))/2) if handshakes > 0 else 0