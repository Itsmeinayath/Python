file = open('youtube.txt', 'w')

try:
    file.write("Hello Inayath")
finally:
    file.close()

with open('yotube.txt','w') as file:
    file.write("Hello Inayath here")