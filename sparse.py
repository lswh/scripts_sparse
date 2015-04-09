import scipy, numpy, sklearn, spams, osgeo
from osgeo import gdal
from osgeo.gdalconst import *
from scipy import misc

#Formal input image is GeoTIFF. Extract DEM from both High Reso and Low Reso GeoTIFF files. 
# GDAL commandline used to translate GeoTIFF input to DEM (gdal_translate command)
# The specific command used for input data was: gdal_translate -of XYZ elevation.tif elevation.xyz

#Step 0.5 Get the values from XYZ files and Store the Essential Variables/Lists/Matrices Here. 
#gdal warp to make pixel number of LiDAR equal to pixel number of SAR. Used average command
# gdalwarp -tr 9 9 -r average CDO_LiDAR_500x500.tif DownsampledLiDAR.tif
# Should strictly be 9.08 but I did not try that yet. 

highxyz = "56by56LIDARSAMPLE.xyz"
lowxyz = "SARELEVATION.xyz"

highxyz = open(highxyz)
lowxyz = open(lowxyz)

xhighinitial = []
xlowinitial = []
yhighinitial = []
ylowinitial = []
zhighinitial = []
zlowinitial = []

for line in highxyz:
    x,y,z=line.split()
    xhighinitial.append(float(x))
    yhighinitial.append(float(y))
    zhighinitial.append(float(z))
highxyz.close()


for line in lowxyz:
    x,y,z=line.split()
    xlowinitial.append(float(x))
    ylowinitial.append(float(y))
    zlowinitial.append(float(z))

zlowinitial = numpy.asmatrix(zlowinitial)
print zlowinitial

#Step 1: Declare the necessary functions for both high reso and low reso
#PatchSelectFunction -- input ang Z values
def PathSelect():
    



"""
# Arbitrarily assign 3 at a time for the patch selection
# Note: This needs to be converted as a callable function for both high and low
for i in range(0, len(blockimghigh)):
    for j in range(0, len(blockimghigh)-2):
        h=blockimghigh[i,j]
        y.append(h)
        h=blockimghigh[i,j+1]
        y.append(h)
        h=blockimghigh[i,j+2]
        y.append(h)
        yp.append(h)
        j+=1
    i+=1

#PatchSimplification -- input ang matrix from PatchSelectFunction
y = numpy.asmatrix(y)
y = y.transpose()

#Step 2: Dictionary - Acquire sampled atoms from input DEM file using Yang et al's Method(2008)
#Note for DictionaryHigh -- downsampled using bicubic interpolation
Dhigh = array[[]] 
Dlow = array[[]]

#Step 3: Incorporate the Weights - this is still a little hazy
#Get residuals from slope and roughness and predicted values. Normalize from a scale of 1 to 100. 
wlow = array[[]]
whigh = array[[]]

#Step 5: Matrix Operations under Initial Conditions
# Dtilde = 1st row sqrt(wlow)*Dlow, 2nd row sqrt(whigh)*Dhigh, 3rd row sqrt(beta)*P*Dhigh
# tau equal to 7, but ideal between range of 7 to 15. 
# beta values 0.5 to 1.5

# Initialize alpha sparse vector 
alphanaught = [[]]
# ytilde = 1st row sqrt wlow*ylow, 2nd row sqrt whigh*yhigh, 3rd row sqrt(beta)*yp of overlap
# ytilde = initialized residual 

# Gamma = null array
# Set iteration counter k = 1 
#Step 5 ITERATE AFTER INITIALIZATION
# min |Dtilde*alpha-ytilde| + tau*|alpha|
#Iterate and look for alpha
# Correlation of Dictionary atom or column and residual
Dtildemaxcorr = array[[]]

for k=1:
	for i=1 in len(Dtilde):
        pass
		return Dtildemaxcorr'''
"""



