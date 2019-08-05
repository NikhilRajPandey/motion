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
    @staticmethod
    def fromGiven(find,**given):
        '''
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

a = Motion.fromGiven('s',v=0,t=6,a=-6)
print(a)