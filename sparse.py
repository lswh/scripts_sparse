import spams
import scipy, numpy, sklearn
from scipy import misc
# It can make the computation much faster if instead of * we can predetermine the specific numpy
# packages required by the script.

#PAGE 1 of REFERENCE DOCUMENT
# Step 1 Preprocess the Input Image
# Numpy Version reference: http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
# datahighnumpyarray =  numpy.loadtxt(inputfilehigh.txt, delimiter=None)
#The variables datahigh and datalow will have an appearance similar to this: [[1,2,3,4,5],[4,5,6,
#7, 8],[7,8,9,10,11], [1,2,3,4,5], [5,6,7,8,9]] for a 5 X 5 matrix

#Temporary use Lena standard testing image just to have 2D arrays that are equal in size
#256 elements here  
img=scipy.misc.lena()
blockimglow=img[0:16,0:16]
blockimghigh=img[17:33,17:33]
blockimghigh=numpy.asmatrix(blockimghigh)
blockimglow=numpy.asmatrix(blockimglow)

#Step 3: Patch Selection writen into a Column Matrix
#Initialize y with tilde here as a blank 2Dimensional list
y = []
#Y Patch of Overlap
yp = []


# Checker for final values. Just to see if end of list has same values produced.
'''h=blockimghigh[15,12]
y.append(h)
h=blockimghigh[15,13]
y.append(h)
h=blockimghigh[15,14]
y.append(h)
print y
print 'set'
h=blockimghigh[15,13]
y.append(h)
h=blockimghigh[15,14]
y.append(h)
h=blockimghigh[15,15]
y.append(h)
print y
print 'set' '''


#Concatenate first
# PATCH
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


# OUTPUT HERE: yhigh and ylow na columnar 
y = numpy.asmatrix(y)
y = y.transpose()


# Co-registration 
'''##STAGE 2: SPARSE

#Dictionary is here. Initialized via random sampling. Question: How do I randomize this??? 
Dhigh = array[[]] 
Dlow = array[[]]
# P is the operator getting the overlap.
# Dtilde = 1st row sqrt(wlow)*Dlow, 2nd row sqrt(whigh)*Dhigh, 3rd row sqrt(beta)*P*Dhigh
Dtilde = array[[]]
#values of this will depend on Debbie's recent output if any n by k matrix
tau = 7 
#ideal values for tau as per lit is between 7 to 15, tau being number of nonzero terms, so you can
# change this
#Get residuals from slope and roughness and predicted values. Normalize from a scale of 1 to 100. 
#This will be used as the content of the wlow and whigh.
wlow = array[[]]
whigh = array[[]]

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




