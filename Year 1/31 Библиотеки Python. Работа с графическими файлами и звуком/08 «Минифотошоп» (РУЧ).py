def image_filter(pixels, i, j):
    """Делает сепию"""
    k = 20
    r = pixels[i, j][0]
    g = pixels[i, j][1]
    b = pixels[i, j][2]
    sr = (r + g + b) // 3
    r = sr + k * 2
    g = sr + k
    b = sr
    r = 255 if r > 255 else r
    g = 255 if g > 255 else g
    b = 255 if b > 255 else b
    return r, g, b