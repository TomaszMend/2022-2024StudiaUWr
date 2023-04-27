import colorsys

(r, g, b) = (0.2, 0.4, 0.4)
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
print('HSV : ', h, s, v)