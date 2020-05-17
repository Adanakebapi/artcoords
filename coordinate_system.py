from PIL import Image

# Write the rule into rule function.
def rule(x,y):
    return True

img = Image.new("RGB",(1021,1021))

data = []
for i in range(1021):
    for j in range(1021):
        y = 127-int(i/4)
        x = int(j/4)-127
        if (i % 4 == 0) or (j % 4 == 0):
            if (i == 512) or (j == 512) or (i == 508) or (j == 508):
                data += [(0,0,255)]
            else:
                data += [(255,0,0)]
        elif rule(x,y):
            data += [(255,255,255)]
        else:
            data += [(0,0,0)]

img.putdata(data)
img.save("graph.png")
