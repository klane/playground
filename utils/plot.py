import matplotlib.pyplot as plt


# plot images at the current epoch
def plot_images(images, rows, cols):
    plt.figure(figsize=(15, 15))

    for i in range(rows * cols):
        plt.subplot(rows, cols, i+1)
        plt.imshow(images[i, :, :, 0], cmap='gray_r')
        plt.axis('off')


# save images at the current epoch
def save_images(images, epoch, image_dir, rows, cols):
    plot_images(images, rows, cols)
    plt.savefig(f'{image_dir}/digits_{epoch:04d}.png')
    plt.close()
