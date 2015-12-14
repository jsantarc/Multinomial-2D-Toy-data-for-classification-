import numpy as np

def MakeToyData(a,NumberSamples):
    """    
    This function generates some nonlinearly separable toy data   
    Input
    a:column vector repenting decision boundary  in the form:
    f(x)=a[0]+a[1]x1+a[2]x2+a[3]x1x2+a[4]x1^2+a[5]x2^3    
    NumberSamples: number of samples
    Output  
    Out[1]:y lables such that f(xi)<=0 yi=1 and f(xi)>0 yi=2 
    Out[0]:X 2d feature vectors with rows corresponding to x     
    Needs:numpy ,  matplotlib.pyplot  
    """
    #Generate some feature vectors
    X=np.matrix(np.random.rand(NumberSamples,2))
    #Quadratic decision boundary
    f=a[0]+(X)*a[1:3]+np.multiply(X[:,0], X[:,1])*a[4]+np.multiply(X, X)*a[5:7]

    f1=np.array(f)
    f2=f1.flatten()
    y=np.array([1]*(NumberSamples));
    #Label data in on each side 
    y[np.where( f2> 0)]=2

      #output vrables 
    Out=[X,y]    
    
    return(Out) 