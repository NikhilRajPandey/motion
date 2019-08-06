from math import sqrt

'''
We have given 3 equation of motion

(v: Final Velcoity, u: Initial Velocity,a:accelaration,t:time,s:Distance)

v = u + at (I equation)
s = ut + a*t*t*1/2 (II equation)
2as = (v*v) - (u*u) (III equation)

We have to find a certain using this equation
Example:
If Time was not given but we gave to find s then we have to use III equation

All the args of function that are given to you in  are SI UNIT
'''

class Motion:
    def __init__(self,a=None,u=None,v=None,s=None,t=None,avg=None):
        self.accelaration = a
        self.initVelocity = u
        self.finalVelociy = v
        self.distanceTraveled = s
        self.time = t
        self.avgVelocity = avg
    
    '''Basic Formulas'''
    # You need to first Make object of Motion for using this

    def accelfromTUV(self):
        if all(variables != None for variables in [self.finalVelociy,self.initVelocity,self.time]):
            self.accelaration = (self.finalVelociy - self.initVelocity) / self.time
            return self.accelaration
        else:
            print("Wrong Var")
    
    def avgVelocityWithoutDisplacement(self):
        self.avgVelocity = (self.initVelocity + self.finalVelociy) / 2
        return self.avgVelocity

    @staticmethod
    def fromGiven(find,**given):
        '''
        This Function is static Means:
        You can use it without Making Motion Object.

        Suppose You want to find acceleration then you can write like this: 

        Motion.fromGiven('a',u=5,t=2,v=10)
        It will result 2
        Similiary This program will help you so much in physics        
        '''
        # For I equation
        if find == 'a' and 'u' in given and 'v' in given and 't' in given:
            result = int((given['v']-given['u'])/given['t'])
            return result
        
        elif find == 'u' and 'a' in given and 'v' in given and 't' in given:
            result = int((given['a']*given['t'])-given['v'])
            return result

        elif find == 'v' and 'u' in given and 't' in given and 'a' in given:
            result = int(given['u']+(given['a']*given['t']))
            return result

        elif find == 't' and 'u' in given and 'v' in given and 'a' in given:
            result = int ((given['v']-given['u'])/given['a'])
            return result

        # For II Equation
        elif find == 's' and 't' in given and 'a' in given and 'u' in given:
            result = int((given['u'] * given['t']) + ( (given['a'] * given['t'] * given['t']) / 2))
            return result

        elif find == 't' and 'u' in given and 'a' in given and 's' in given and given['u'] == 0:
            result = int((2* given['s'])/given['a'])
            result = sqrt(result)
            return result
        elif find == 'a' and 'u' in given and 't' in given and 's' in given:
            result = int((2*(given['s'] - given['u']*given['t']))/ given['t']* given['t'])
            return result
        elif find == 'u' and 's' in given and 't' in given and 'a' in given:
            result = int((given['s']-given['a']*given['t']*given['t'])/given['t'])
            return result

        # For equation III
        elif find == 'u' and 'v' in given and 'a' in given and 's' in given:
            result = int((2*given['a']*given['s'])-(given['v']*given['v']))
            result = sqrt(result)
            return result
        
        elif find == 'v' and 'u' in given and 'a' in given and 's' in given:
            result = sqrt(int((2*given['a']*given['s'])+(given['u']*given['u'])))
            return result

        elif find == 'a' and 'u' in given and 'v' in given and 's' in given:
            result = (((given['v']*given['v']) - (given['u']*given['u']))/ (2 * given['s']))
            return result
        
        elif find == 's' and 'u' in given and 'v' in given and 'a' in given:
            result = (((given['v']*given['v']) - (given['u']*given['u']))/ (2 * given['a']))
            return result

a = Motion(a=None,u=23,v=5,t=5)
print(a.accelfromTUV())