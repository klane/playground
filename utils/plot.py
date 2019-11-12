import os

import imageio
import matplotlib.pyplot as plt
import PIL


# Display a single image using the epoch number
def display_image(epoch, image_dir='.'):
    return PIL.Image.open(os.path.join(image_dir, f'digits_{epoch:04d}.png'))


# plot images at the current epoch
def plot_images(images, rows, cols):
    plt.figure(figsize=(15, 15))

    for i in range(rows * cols):
        plt.subplot(rows, cols, i+1)
        plt.imshow(images[i, :, :, 0], cmap='gray_r')
        plt.axis('off')


def save_animation(anim_file, filenames, file_dir='.'):
    with imageio.get_writer(os.path.join(file_dir, anim_file), mode='I') as writer:
        filenames = sorted(filenames)
        last = -1

        for i, filename in enumerate(filenames):
            frame = 2*(i**0.5)
            if round(frame) > round(last):
                last = frame
            else:
                continue

            image = imageio.imread(filename)
            writer.append_data(image)

        image = imageio.imread(filename)
        writer.append_data(image)


# save images at the current epoch
def save_images(images, epoch, image_dir, rows, cols):
    plot_images(images, rows, cols)
    plt.savefig(os.path.join(image_dir, f'digits_{epoch:04d}.png'))
    plt.close()
