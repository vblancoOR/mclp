
from math import pi
import random
from disc import *
import sys
sys.path.append('../geom')
from point import *
from cp import get_angle
import matplotlib.pylab as plt
from matplotlib import patches 
import numpy as np
from elzinga_hearn import *
import os
import imageio
from PIL import Image
#import pyglet
#from celluloid import Camera # getting the camera

#from IPython.display import HTML # to show the animation in Jupyter
import matplotlib.animation as animation


def PlotCircle(A, p, r, q):
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1, 1)
    ax.set_aspect('equal')   
    ax.axis('off')       
    
    
    ax.axis([-0.2, 1.2, -0.2,1.2])
    
    for i in range(len(A)):
        if np.sqrt((A[i].x - p.x)**2 + (A[i].y - p.y)**2) <= r+0.0001:
            ax.plot(A[i].x, A[i].y, 'o', color='k')
        else:
            ax.plot(A[i].x, A[i].y, 'o', color='g')
            
    for i in range(2):
        ax.plot(q[i].x, q[i].y, 'o', color='b')
    if q[2]!=None:
        ax.plot(q[2].x, q[2].y, 'o', color='b')
    circlek = plt.Circle((p.x, p.y), r, color='gray', alpha=0.3)
    ax.add_artist(circlek)
    ax.plot(p.x, p.y, '*', color='r')
    
    
    #plt.close()
    #plt.show()
    
    
def PlotCircleRed(A, p, r, q, R):
    
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(1,1, 1)
    ax.set_aspect('equal')   
    ax.axis('off')       
    
    
    ax.axis([-0.2, 1.2, -0.2,1.2])
    
    for i in range(len(A)):
        if np.sqrt((A[i].x - p.x)**2 + (A[i].y - p.y)**2) <= r+0.0001:
            ax.plot(A[i].x, A[i].y, 'o', color='k')
        else:
            ax.plot(A[i].x, A[i].y, 'o', color='g')
            
    for i in range(2):
        ax.plot(q[i].x, q[i].y, 'o', color='b')
    if q[2]!=None:
        ax.plot(q[2].x, q[2].y, 'o', color='b')
    if r<R:
        alpha0=0.15
        alpha1=0.1
    else:
        alpha0=0.1
        alpha1=0.15
    circlek = plt.Circle((p.x, p.y), r, color='gray', alpha=alpha1)
    ax.add_artist(circlek)
    circlek2 = plt.Circle((p.x, p.y), R, color='red', alpha=alpha0)
    ax.add_artist(circlek2)
    ax.plot(p.x, p.y, '*', color='r')
    
    
    #plt.close()
    #plt.show()
    
    
def OneCenterEH(P):
    
    
    p3 = [Point(-1, -1) for i in range(3)]
    p3[0] = P[0]
    p3[1] = P[1]
    d = disc(points=[p3[0], p3[1]])
    n = len(P)
    cnt = 0
    stop, p3[2] = cover_all(P, d, p3[:2])
    while not stop:
        ##€print(cnt, p3)
        if right_obtuse_triangle(p3): 
            #PlotCircle(P, d.center, d.radius, p3)# right/obtuse triangle
            d = disc(points=[p3[0], p3[1]])
            stop, p3[2] = cover_all(P, d, p3[:2])
        else:                         # strict acute triangle
            d = disc(points=[p3[0], p3[1], p3[2]])
            #PlotCircle(P, d.center, d.radius, p3)
            stop, pd = cover_all(P, d, p3)  # pd outside d
            if not stop:
                find_three(p3, pd, d)
        
        cnt += 1
    #print("Iterations: ", cnt)
    return d#, p3
        
  
def OneCenterEHPlot(P):
    
    p3 = [Point(-1, -1) for i in range(3)]
    p3[0] = P[0]
    p3[1] = P[1]
    d = disc(points=[p3[0], p3[1]])
    n = len(P)
    cnt = 0
    stop, p3[2] = cover_all(P, d, p3[:2])
    it=0
    #filenames = []
    #fig, ax = plt.subplots() # creating my fig

    while not stop:
        ##€print(cnt, p3)
        if right_obtuse_triangle(p3): 
            PlotCircle(P, d.center, d.radius, p3)# right/obtuse triangle
            d = disc(points=[p3[0], p3[1]])
            stop, p3[2] = cover_all(P, d, p3[:2])
        else:                         # strict acute triangle
            d = disc(points=[p3[0], p3[1], p3[2]])
            PlotCircle(P, d.center, d.radius, p3)
            stop, pd = cover_all(P, d, p3)  # pd outside d
            if not stop:
                find_three(p3, pd, d)
        if it <9:
            filename = "pics/pic0%d.png"%(it+1)
        else:
            filename = "pics/pic%d.png"%(it+1)
        it+=1
        #filenames.append(filename)
        #plt.savefig(filename)
        plt.close()
         # make it bigger


        
     # cnt += 1
    #print("Iterations: ", cnt)

    # build gif
#     with imageio.get_writer('1center.gif', mode='I', duration=2) as writer:
#         for filename in filenames:
#             image = imageio.imread(filename)
#             writer.append_data(image)
        
# # Remove files
#     for filename in set(filenames):
#         os.remove(filename)
        
        
        
        
    # # pick an animated gif file you have in the working directory
    # ag_file = "1center.gif"
    # animation = pyglet.resource.animation(ag_file)
    # sprite = pyglet.sprite.Sprite(animation)
    
    # # create a window and set it to the image size
    # win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    
    # # set window background color = r, g, b, alpha
    # # each value goes from 0.0 to 1.0
    # green = 0, 1, 0, 1
    # pyglet.gl.glClearColor(*green)
    
    # @win.event
    # def on_draw():
    #     win.clear()
    #     sprite.draw()
    
    # pyglet.app.run()    
        
        
    return d#, p3



def OneCenterAnimated(P):
    
    
         
    fig = plt.figure(figsize=(15, 10))

    i1, i2= ClosestPoints(P)
    p3 = [Point(-1, -1) for i in range(3)]
    p3[0] = P[i1]
    p3[1] = P[i2]
    d = disc(points=[p3[0], p3[1]])
    n = len(P)
    cnt = 0
    stop, p3[2] = cover_all(P, d, p3[:2])
    it=0
    filenames = []
    #fig, ax = plt.subplots() # creating my fig

    while not stop:
        ##€print(cnt, p3)
        if right_obtuse_triangle(p3): 
            PlotCircle(P, d.center, d.radius, p3)# right/obtuse triangle
            d = disc(points=[p3[0], p3[1]])
            stop, p3[2] = cover_all(P, d, p3[:2])
        else:                         # strict acute triangle
            d = disc(points=[p3[0], p3[1], p3[2]])
            PlotCircle(P, d.center, d.radius, p3)
            stop, pd = cover_all(P, d, p3)  # pd outside d
            if not stop:
                find_three(p3, pd, d)
        if it <9:
            filename = "pics/pic0%d.png"%(it+1)
        else:
            filename = "pics/pic%d.png"%(it+1)
        it+=1
        filenames.append(filename)
        plt.savefig(filename, transparent=True)
        plt.close()


    

    return filenames

def OneCenterAnimated2(P, r):
    
    
         
    fig = plt.figure(figsize=(15, 10))

    i1, i2= ClosestPoints(P)
    p3 = [Point(-1, -1) for i in range(3)]
    p3[0] = P[i1]
    p3[1] = P[i2]
    d = disc(points=[p3[0], p3[1]])
    n = len(P)
    cnt = 0
    stop, p3[2] = cover_all(P, d, p3[:2])
    it=0
    filenames = []
    #fig, ax = plt.subplots() # creating my fig

    while not stop:
        ##€print(cnt, p3)
        if right_obtuse_triangle(p3): 
            PlotCircleRed(P, d.center, d.radius, p3, r)# right/obtuse triangle
            d = disc(points=[p3[0], p3[1]])
            stop, p3[2] = cover_all(P, d, p3[:2])
        else:                         # strict acute triangle
            d = disc(points=[p3[0], p3[1], p3[2]])
            PlotCircleRed(P, d.center, d.radius, p3, r)
            stop, pd = cover_all(P, d, p3)  # pd outside d
            if not stop:
                find_three(p3, pd, d)
        if it <9:
            filename = "pics2/pic0%d.png"%(it+1)
        else:
            filename = "pics2/pic%d.png"%(it+1)
        it+=1
        filenames.append(filename)
        plt.savefig(filename, transparent=True)
        plt.close()


    

    return filenames
def Transparent(filenames):
    
    for f in filenames:
        img = Image.open(f)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                if item[0] > 150:
                    newData.append((0, 0, 0, 255))
                else:
                    newData.append(item)
                    #print(item)
    
    
        img.putdata(newData)
        img.save(f, "PNG")

def AnimationEH(A):
    
    filenames= OneCenterAnimated(A)
    #Transparent(filenames)
# Build GIF
    with imageio.get_writer('1center.gif', mode='I', duration=1.5) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    for f in filenames:
        os.remove(f)
    #im = Image.open('1center.gif')
    #transparency = im.info['transparency'] 
    #im.save('1center_.gif', transparency=255)


def AnimationEH2(A,r):
    
    filenames= OneCenterAnimated2(A,r)
    #Transparent(filenames)
# Build GIF
    with imageio.get_writer('1center_2.gif', mode='I', duration=1.5) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    for f in filenames:
        os.remove(f)
    #im = Image.open('1center_2.gif')
    #transparency = im.info['transparency'] 
    #im.save('1center2_.gif', transparency=255)

npts = 100
AA0 = []
for i in range(npts):
    a = Point(random.random(), random.random())
    AA0.append(a)

def ClosestPoints(A0):
    
    mind=100
    ii1=0
    ii2=0
    for i1 in range(len(A0)):
        for i2 in range(i1):
            dd=np.sqrt((A0[i1].x - A0[i2].x)**2 + (A0[i1].y - A0[i2].y)**2)
            if dd<mind and dd>0.001:
                mind=dd
                ii1=i1
                ii2=i2
                
        
    return ii1, ii2        
            



AnimationEH(AA0)
AnimationEH2(AA0, 0.4)


        


#OneCenterEHAnimated(A)


# # p=dd[0]
# # r=dd[1]





# r=dd.radius
# PlotCircle(A, dd.center, r,qq)