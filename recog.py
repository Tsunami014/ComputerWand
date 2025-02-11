# import matplotlib.pyplot as plt
import dollarN as dN
from multiprocessing import Process
import time

r = dN.recognizer()
#By default, a recognizer gives a positive result when gestures have
#the same number of strokes only. This can be turned off:
#r.set_same_nb_strokes(False)

#Rotation invariance can also be turned off:
#r.set_rotation_invariance(False)

def register_gesture(name, paths, reverse=True):
    if reverse:
        paths = paths + [[[5-j[0], j[1]] for j in i] for i in paths]
    for p in paths:
        r.add_gesture(name, [p])

register_gesture('Swish+flick', [
    [[0.,2.], [1.,1.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.], [5.,2.5]],
    [[0.,2.], [1.,1.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.]],
    [[0.,5.], [1.,2.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.], [5.,2.5]],
    [[0.,5.], [1.,2.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.]],
    [[0.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.]],
    [[0.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.], [5.,2.5]]
])

register_gesture('Flick', [
    [[0.,4.], [0.,0.], [0., 0.5]],
    [[0.,5.], [0.,0.], [0., 0.4]],
    [[0.,5.], [0.,0.], [0., 0.3]],
    [[0.,5.], [0.,0.], [0., 0.1]]
], False)

register_gesture('Wave', [
    [[5.,5.], [0., 2.5], [5.,0.]],
    [[5.,5.], [1.,3.], [0., 2.5], [1., 2], [5.,0.]],
    [[5.,8.], [1.,6.], [0., 5.5], [1., 5], [4.,3.], [5.,2.5], [4.,2.], [0, 0]]
])

def _recog(coords):
    try:
        recoged = r.recognize(coords)
        if recoged['name'] == '':
            print('= Nothing detected.')
        else:
            print(f'> {recoged['name']}: {recoged['value']}, time: {recoged['time']}')
    except Exception as e:
        print(f'! An error has occured: {e}')

def recog(mouse_coords):
    if len(mouse_coords) <= 1:
        return
    pro = Process(target=_recog, args=([mouse_coords],), daemon=True)
    pro.start()
    now = time.time()
    while pro.is_alive():
        if time.time() > now+1:
            pro.kill()
            print('] Timeout!')
            break

    # xs, ys = zip(*mouse_coords)
    # plt.scatter(xs, ys)
    # lft, rt = plt.xlim()
    # plt.xlim(lft-100, rt+100)
    # bt, tp = plt.ylim()
    # plt.ylim(bt-100, tp+100)
    # plt.show()
