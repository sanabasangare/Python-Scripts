import random
import platform

os=platform.dist()[0]
if os=='LinuxMint' or os=='Ubuntu':
    loc='/usr/share/dict/cracklib-small'
else:
    loc='/usr/share/dict/words'
with open(loc) as f:
    content=f.read().split('\n')
f.close()
