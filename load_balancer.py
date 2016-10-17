# --
#Author: Sayali Upasani
#Date: March 2014
# --

import numpy as np
import collections
time_stamp = []
source_host = []
destination_host= []
source_port = []
destination_port = []
bytes = []
result = []

def calculation( index , h, s, d ):
    #"This block is to calculate the average bit rate of packets for the duration of 5 minutes"
    #print (index)
    #print (s)
    #print (c)
    #print (index)
    #z=0
    #h=0
    #while z<=index:

    a1= float (h) * 8
    f1= np.divide(a1,s)
    f2= f1/1000
    #z= z+1
    #print 'Total bits in duration of 5 minutes =',a1
    #print 'Total bytes in duration of 5 minutes=',h
    #print 'Duration =',s
    #print 'Average bitrate for 5 minutes =', f1
    print 'Average bitrate for 5 minutes window for ' +d+ ' in Kbps =',f2

def Average(a, length, d, c):
        s=0
        x=1
        m = 299
        h = 0
        z = 0
        while x < length:
            if a[x-1] < m:
                #print (x)
                sub = np.subtract(a[x],a[x-1])
                #sub1 = np.subtract(a[x-1],o)
                s = np.sum([s,sub])
                h = np.sum([h,c[z]])
                #print (s)
                #if s <= 299:
                x = x + 1
                z = z + 1
            else:
                #result.append(s)
                index = x
                #print (index)
                calculation( index, h, s, d )
                s = 0
                m = m + 299
                #x -= 1
                #print "else loop"
                #print (x)
    #print (result)


with open ("packets.txt") as f:
        for line in f:
            x=line.split()
            time_stamp.append([float(x[0])])
            source_host.append([int(x[1])])
            destination_host.append([int(x[2])])
            source_port.append([int(x[3])])
            destination_port.append([int(x[4])])
            bytes.append([int(x[5])])

k = np.array(time_stamp).flatten().tolist()
b = np.array(bytes).flatten().tolist()
#d = np.array(destination_host).flatten().tolist()
l = len(bytes)

pb1 = []
pb2 = []
pb3 = []
pb4 = []
ts1 = []
ts2 = []
ts3 = []
ts4 = []

i = 0
m = 299

while i < l:
        pb1.append(b[i])
        ts1.append(k[i])
        i=i+4
#print(pb1)
length = len(pb1)
a = list(ts1)
c = pb1
d = 'pb1'
Average( a , length, d, c )

i = 1
while i < l:
        pb2.append(b[i])
        ts2.append(k[i])
        i=i+4
#print(pb2)
length = len(pb2)
a = list(ts2)
c = pb2
d = 'pb2'
Average( a, length, d, c )

i = 2
while i < l:
    pb3.append(b[i])
    ts3.append(k[i])
    i=i+4
length = len(pb3)
a = list(ts3)
c = pb3
d = 'pb3'
Average( a, length, d, c )

i = 3
while i < l:
    pb4.append(b[i])
    ts4.append(k[i])
    i=i+4
length = len(pb4)
a = list(ts4)
c = pb4
d = 'pb4'
Average( a, length, d, c)
                
