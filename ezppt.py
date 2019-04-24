#!/usr/bin/env python

from keyboard import *
import yaml

idx = 0
leng = 0
data = []
hotkeys = ["a", "s", "d", "f", "g", "h"]
labels = ["Verse1", "Verse2", "Chorus", "Bridge", "Outro", "Other"]

def priv_s(_):
    print(_)
    global idx
    idx -= 1
    idx %= leng
    print('song {}'.format(idx))

def next_s(_):
    print(_)
    global idx
    idx += 1
    idx %= leng
    print('song {}'.format(idx))

def transkey(x):
    l = labels[hotkeys.index(x)]
    num = data[idx][l]
    if num is None:
        return x
    else:
        num = str(num)
        keynum = [num[i] for i in range(len(num))]
        k = ','.join(keynum) + ',enter'
        return k

def setup_key():
    on_press_key('a', lambda _: send(transkey('a')))
    on_press_key('s', lambda _: send(transkey('s')))
    on_press_key('d', lambda _: send(transkey('d')))
    on_press_key('f', lambda _: send(transkey('f')))
    on_press_key('g', lambda _: send(transkey('g')))
    on_press_key('h', lambda _: send(transkey('h')))

    on_press_key('z', priv_s)
    on_press_key('x', next_s)

    # Blocks until you press esc.
    wait('esc')

def load_conf():
    global data
    with open("./config.yml") as fd:
        data = yaml.load(fd, Loader = yaml.SafeLoader)["Songs"]
    global leng
    leng = len(data)
    print(data)

if __name__ == "__main__":
    load_conf()
    setup_key()
