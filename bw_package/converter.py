from PIL import Image

# image = Image.open('deadspace.png')
# image = image.rotate(90)
# image.show()

pixel = [0, 0, 0]

pixel[0]  #r
pixel[1]  #g
pixel[2]  #b

width = 800
height = 600

def convert(pixels, width, height):

    line = [(0, 0, 0)]*width
    new_image = [line]*height

    for i in range(height):
        for j in range(width):
            pixel = pixels[i][j]
            color =  (pixel[0] + pixel[1] + pixel[2])/3

            new_pixel = (color,color,color)

            new_image[i][j] = new_pixel

def convert_bw(image):
    new_image = Image.new('RGB', (image.width,image.height))

    for j in range(image.height):
        for i in range(image.width):
            pixel = image.getpixel((i,j))
            color =  int(0.3*pixel[0] + 0.6*pixel[1] + 0.1*pixel[2])

            new_pixel = (color,color,color)

            new_image.putpixel((i,j), new_pixel)

    return new_image



# novo_arquivo = Image.open('deadspace.png')
# novo_arquivo = convert_bw(novo_arquivo)
# novo_arquivo.save('bw.png')
