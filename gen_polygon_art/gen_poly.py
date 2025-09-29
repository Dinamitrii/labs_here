from PIL import Image, ImageDraw
import random


w,h = 400,400
img = Image.new("RGB", (w,h), "black")
draw = ImageDraw.Draw(img)

for _ in range(200):
    point = [(random.randint(0,w),
        random.randint(0,h)) for _ in range(6)]
    color = (random.randint(0,255),
        random.randint(0,255),
             random.randint(0,255))
    draw.polygon(point, color)

img.save("out.jpg")

