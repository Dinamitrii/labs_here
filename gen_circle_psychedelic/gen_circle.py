import math

from PIL import Image

w, h = 400, 400

img = Image.new("RGB", (w, h))
cx, cy = w // 2, h // 2

for y in range(h):
    for x in range(w):
        dx, dy = x - cx, y - cy
        angle = math.atan2(dy, dx)
        dist = math.hypot(dx, dy)
        r = int((math.sin(dist / 10 + angle) * 127 + 128) % 256)
        g = int((math.cos(dist / 10 - angle) * 127 + 128) % 256)
        b = int((math.sin(dist / 15) * 127 + 128) % 256)

        img.putpixel((x, y), (r, g, b))

img.save("psycho_circle.png")
