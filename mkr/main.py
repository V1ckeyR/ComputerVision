from PIL import Image, ImageDraw
import cv2


def image_serpia_mode(name, output, depth=20):
    with Image.open(name) as image:
        draw = ImageDraw.Draw(image)
        pixels = image.load()
        for w in range(image.size[0]):
            for h in range(image.size[1]):
                average = sum(pixels[w, h]) // 3
                a = average + depth * 2 if (average + depth * 2) <= 255 else 255
                b = average + depth if (average + depth) <= 255 else 255
                c = average if average <= 255 else 255
                draw.point((w, h), (a, b, c))
        image.save(output, "JPEG")
    return output


def image_filter(name, output):
    cv2.imwrite(output, cv2.cvtColor(cv2.imread(name), cv2.COLOR_RGB2GRAY))


if __name__ == "__main__":
    image_filter(image_serpia_mode("img.jpg", "serpia.jpg"), "filtered.jpg")
