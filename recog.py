import matplotlib.pyplot as plt

def recog(mouse_coords):
    xs, ys = zip(*mouse_coords)
    plt.scatter(xs, ys)
    l, r = plt.xlim()
    plt.xlim(l-100, r+100)
    b, t = plt.ylim()
    plt.ylim(b-100, t+100)
    plt.show()
