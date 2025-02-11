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

r.add_gesture('Swish+flick', [ [[0.,2.], [1.,1.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.], [5.,2.5]] ])
r.add_gesture('Swish+flick', [ [[0.,2.], [1.,1.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.]] ])
r.add_gesture('Swish+flick', [ [[0.,5.], [1.,2.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.], [5.,2.5]] ])
r.add_gesture('Swish+flick', [ [[0.,5.], [1.,2.], [2.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.]] ])
r.add_gesture('Swish+flick', [ [[0.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.]] ])
r.add_gesture('Swish+flick', [ [[0.,0.], [4.,1.], [5.,0.], [5.,5.], [5.,0.], [5.,2.5]] ])

r.add_gesture('Flick', [ [[0.,5.], [0.,0.], [0., 0.4]] ])
r.add_gesture('Flick', [ [[0.,5.], [0.,0.], [0., 0.1]] ])

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
