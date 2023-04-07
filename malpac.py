# this tool is only for educational purposes only... please u>
import string
import pickle
import struct
import random
import os
import random, time

os.system('clear')

# function to create packet
print('[PROCESS] creating packet...')
time.sleep(2)
def create_packet():
    chars = string.ascii_letters + string.punctuation + string.digits
    dumb_chars = pickle.dumps(chars)
    unpack_dumb_chars = struct.unpack('! 12s 12s H', dumb_chars[:26])
    print('[MALPAC] packet generated successfully')
    print('[PACKET]\n')
    for i in range(100):
        rand_pkt = random.choice(unpack_dumb_chars)
        print(rand_pkt, end='')
create_packet()

