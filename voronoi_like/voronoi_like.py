from PIL import Image
import random, math



w, h = 400, 400

img= Image.new('RGB', (w, h))
points = [(random.randint(0, w), random.randint(0, h),
           (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)))
          for _ in range(20)]
for y in range(h):
    for x in range(w):
        closest=min(points, key=lambda p: (p[0]-x)**2 + (p[1]-y)**2)
        img.putpixel((x, y),closest[2])


img.save('voronoi_like.png')

