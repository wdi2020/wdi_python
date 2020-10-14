from PIL import Image


def load_image(filename):
    image = Image.open(filename)
    width, height = image.size
    pixels = list(image.getdata())
    image = [pixels[i:i + width] for i in range(0, len(pixels), width)]
    return image


def save_image(filename, image):
    flat_image = [item for sublist in image for item in sublist]
    height, width = len(image), len(image[0])
    image_out = Image.new("L", (width, height))
    image_out.putdata(flat_image)
    image_out.save(filename)


def color_to_grey(image, average=True):
    if average:
        for row in image:
            for item in row:
                r, g, b = item
                item = [0.3 * r, 0.59 * g, 0.11 * b]
    else:
        for row in image:
            for item in row:
                r, g, b = item
                sr = (r+g+b)/3
                item = [sr, sr, sr]
    return 9


if __name__ == "__main__":
    in_file = "photo.jpg"
    out_file = "decision_tree_grey.jpg"
    image = load_image(in_file)
    image = color_to_grey(image)
    save_image(out_file, image)
