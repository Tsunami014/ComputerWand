import matplotlib.pyplot as plt
import dollarN as dN

r = dN.recognizer()
#By default, a recognizer gives a positive result when gestures have
#the same number of strokes only. This can be turned off:
#r.set_same_nb_strokes(False)

#Rotation invariance can also be turned off:
#r.set_rotation_invariance(False)

r.add_gesture('U', [ [[0.,5.], [0.,0.], [5.,0.], [5.,5.]] ])

def recog(mouse_coords):
    if not mouse_coords:
        return
    print(r.recognize([mouse_coords]))
    xs, ys = zip(*mouse_coords)
    plt.scatter(xs, ys)
    lft, rt = plt.xlim()
    plt.xlim(lft-100, rt+100)
    bt, tp = plt.ylim()
    plt.ylim(bt-100, tp+100)
    plt.show()
