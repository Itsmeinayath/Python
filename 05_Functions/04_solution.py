import math

def circle_stats(radius):
   area =math.pi * radius ** 2
   circumfarence = 2 * math.pi *radius
   return area,circumfarence
a,c = circle_stats(3)

print(f"Area: {a:.3f}, Circumference: {c:.3f}")
