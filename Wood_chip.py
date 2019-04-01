#Modules
############################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#%matplotlib inline
############################################################


#Data inputs
#############################################################
A = input('Feed speed (m/min) :')
A = float(A)

N = input('Rotation speed (RPM) :')
N = float(N)

H = input('Cutting depth (mm) :')
H = float(H)

R = input('Radius of cutter (mm) :')
R = float(R)

Z = input('Number of knives on cutterhead :')
Z = float(Z)


r=input('Pitch radius of the pinion (mm) :') #ft
r = float(r)
#############################################################


#Data equations
#############################################################

#Wavelengths or feed per knife (mm)
o = (A *1000 / (Z * N))
o = float(o)

#Height of the machining wave (mm)
h = (o**2) / (8 * (R + (o*Z) / 3.1416))


#Average chip thickness (mm)
act = o * np.sqrt(H / (2*R))

#Angle made by the knife during chip machining
alpha = np.arccos((R-H)/R)
alpha_deg = math.degrees(alpha)
#Path of angle during chip machining between 0 to alpha
t = np.arange(0, alpha, 0.001)
t = -1*t

# Martellotti equation's for X and Y coordinates
X=(r * t)- (R * np.sin(t))
Y=R * (1-np.cos(t))
XO = X + o

debx = r * -alpha - R * np.sin(-alpha)
deby = R * (1 - np.cos(-alpha))

finx = (r * -alpha - R * np.sin(-alpha)) + o
finy = R * (1 - np.cos(-alpha))

a = [debx, finx]
b = [deby, finy]

#Plotting chip shape
#############################################################
plt.plot(X, Y, 'b') #same line width and color
plt.plot(XO, Y,  'b') #same line width and color
plt.plot(a,b, 'b')  # union of points

#plt.plot.spines['left'].set_position(('zero'))
#plt.plot.spines['bottom'].set_position(('zero'))

plt.xlabel('Path of the cutting tool in X coordinates (mm)') #show label in x position
plt.ylabel('Path of the cutting tool in Y coordinates (mm)') #show label in x position
plt.title('Theorical Chip shape during wood peripheral planning')#show title Forme théorique du copeau


print("Average chip thickness (mm): ",act)
print("Wavelengths or feed per knife (mm): ", o)
print("Height of the machining wave (mm): ", h)
print("Angle made by the knife during chip machining (degrees): ", alpha_deg)


plt.show()