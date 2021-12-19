import cv2
import matplotlib.pyplot as plt
import numpy as np
import wand.image as wi


def resize_img(img, height):
    scale = height / img.shape[0]
    weight = int(scale * img.shape[1])
    return cv2.resize(img, (weight, height), interpolation=cv2.INTER_AREA)


def draw_img_and_hist(img, title, ax1, ax2, lim):
    ax1.set_title(title)
    ax1.imshow(img)
    ax2.set_title(title + ' hist')
    ax2.hist(img.ravel(), 256, [0, 256])
    ax2.set_xlim([0, 256])
    ax2.set_ylim([0, lim])


def stretch_method(image_name, output):
    with wi.Image(filename=image_name) as i:
        i.contrast_stretch(0.15)
        i.save(filename=output)
    return resize_img(cv2.imread(output), 500)


def find_union(name):
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Lab 8 - origin')
    fig.tight_layout()

    # побудувати гістограму яскравості усього зображення
    img = resize_img(cv2.imread(name), 500)
    draw_img_and_hist(img, 'Original img', axs[0, 0], axs[0, 1], 50000)

    # побудувати гістограми яскравостей для сегменту – об’єктів ідентифікації
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[350:550, 325:700] = 255
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    draw_img_and_hist(masked_img, 'Segment of img', axs[1, 0], axs[1, 1], 5000)
    fig.show()

    # здійснити кольорову корекцію усього зображення з використанням метода розтягування гістограми яскравості
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Lab 8 - color correction')
    fig.tight_layout()

    img = stretch_method(name, name + 'stretched')
    draw_img_and_hist(img, 'Corrected img', axs[0, 0], axs[0, 1], 50000)

    # здійснити кольорову корекцію сегменту зображення з використанням метода розтягування гістограми яскравості
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    draw_img_and_hist(masked_img, 'Segment of corrected img', axs[1, 0], axs[1, 1], 5000)
    fig.show()


if __name__ == "__main__":
    find_union("unions.jpg")
