from matplotlib import pyplot as plt


def plot_comparison(original, thresh, title, otsu=False):
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(original, 'gray')
    axes[0].set_title("Original")
    axes[0].axes.get_xaxis().set_visible(False)
    axes[0].axes.get_yaxis().set_visible(False)

    if otsu:
        axes[1].imshow(original > thresh, 'gray')
    else:
        axes[1].imshow(thresh, 'gray')

    axes[1].set_title(title)
    axes[1].axes.get_xaxis().set_visible(False)
    axes[1].axes.get_yaxis().set_visible(False)
    plt.show()
