import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import io
import base64
plt.style.use("seaborn-v0_8")

x = sp.symbols('x')



class Printex:
    def Wellcome(self):
        print(
'''
   _____ ______ _____                      _    ____  __  __ _____          _       _   _            
  / ____|  ____|  __ \                    | |  |  _ \|  \/  |  __ \        | |     | | | |           
 | (___ | |__  | |  | |     __ _ _ __   __| |  | |_) | \  / | |  | |  _ __ | | ___ | |_| |_ ___ _ __ 
  \___ \|  __| | |  | |    / _` | '_ \ / _` |  |  _ <| |\/| | |  | | | '_ \| |/ _ \| __| __/ _ \ '__|
  ____) | |    | |__| |   | (_| | | | | (_| |  | |_) | |  | | |__| | | |_) | | (_) | |_| ||  __/ |   
 |_____/|_|    |_____/     \__,_|_| |_|\__,_|  |____/|_|  |_|_____/  | .__/|_|\___/ \__|\__\___|_|   
                                                                     | |                             
                                                                     |_|                             

                                                                                                    By KUSHAL N






''')
    def unstable(self):
        print("The given system is not static and is unstable, Please enter proper values!!!")
        



def plot_to_img(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode("utf-8")



class getForces:
    def __init__(self, length, lengthb, lengthc, isWeb):
        self.length = length
        self.lengtha = length-lengthb-lengthc
        self.lengthb = lengthb
        self.lengthc = lengthc
        self.isWeb = isWeb
        

    def getPforces(self, inppF=None):    #Takes input of all the point forces and their respective positions sequentially and returns a dataframe of: distance, force, moment 
        i=1
        pF = pd.DataFrame(columns=['distance', 'force', 'moment'])

        
        while True:
                
            if self.isWeb == False:
                print(pF)
                print(f'point Force_{i}', )
                pF.sort_values(by='distance', inplace=True)
                    
                try:    
                    dist = float(inp := input(f'Enter the distance of point of application of Force_{i} from origin: '))
                    mag = float(inp := input(f'Enter the Force_{i} with direction: '))


                except ValueError:
                    if inp.lower() == "q":
                        print("Quitting force input sequence...")
                        break
                    elif(dist <=0 or dist > self.length):
                        print('enter valid distance!!!')
                        continue
                    else:
                        print("Invalid input! Please enter a number or 'q'.")
                        continue
                pF.loc[len(pF)] = [dist, mag, (dist-self.lengtha)*mag]
                    
                
                print(f'Finished taking {i} forces')

            else:

                print(len(inppF))
                print((inppF))

                if i<=len(inppF):
                    dist = float(inppF.loc[i-1,'distance'])
                    mag = float(inppF.loc[i-1,'force'])

                    pF.loc[len(pF)] = [dist, mag, (dist-self.lengtha)*mag]
                else:break




            i+=1

        print(pF)
            
        self.pF = pF
        return pF


# Takes input of all the distributed forces and their respective positions sequentially and returns a 
# dataframe of: initial distance, final distance, force equation,equivalent force, equivalent distance, moment
  
    def getDforces(self, inpdF = None):

        i=1
        dF = pd.DataFrame(columns=['idistance', 'fdistance', 'localeqn',  'eqforce', 'eqdistance', 'moment'])
        
        while True:
            if self.isWeb == False:
                try:
                    print(f'Distributed Force_{i}', )
                    idist = float(inp:=input(f'Enter the STARTING point of application of Force_{i} from origin: '))
                    fdist = float(inp:=input(f'Enter the ENDING point of application of Force_{i} from origin: '))
                    localeqn = input(f'Enter the Force_{i} eqn wrt STARTING point: ')
                except ValueError:
                    if inp.lower() == "q":
                        print("Quitting force input sequence...")
                        break
                    elif(idist <=0 or idist > self.length or fdist <=0 or fdist > self.length):
                        print('enter valid distance!!!')
                    else:
                        print("Invalid input! Please enter a number or 'q'.")

            else:
                if i<=len(inpdF):
                    idist = float(inpdF.loc[i-1,'idistance'])
                    fdist = float(inpdF.loc[i-1,'fdistance'])
                    localeqn = inpdF.loc[i-1,'localeqn']
                else:break
            # input data from df into idist, fdist and loc eqn




            print(f'Finished taking {i} forces')

            
            eqforce = sp.integrate(sp.sympify(localeqn), (x, 0, fdist-idist)) #equivalent force
            eqdistance = idist+(sp.integrate(f'x*({sp.sympify(localeqn)})',(x, 0, fdist-idist)))/eqforce #equivalent distance of force from point A
            eqn  = sp.sympify(localeqn)
            eqn = eqn.subs(x, x-idist)
            moment = sp.integrate(f'(x - {self.lengtha}) * ({eqn})',(x, idist, fdist)) #moment of force about point A


            dF.loc[len(dF)] = [idist, fdist, localeqn ,eqforce,eqdistance, moment]
            print(dF)
            
            
            i+=1
        self.dF = dF
        return dF

    def Reactions(self): #takes force dataframe as argument and returns reactions r1 and r2 at the joints 

        if self.lengthb == None:
            self.lengthb = self.length

            R1 = -(self.dF['eqforce'].sum() + self.pF['force'].sum())
            self.R1 = R1
            self.R2 = 0
            self.pF.loc[len(self.pF)] = [0, R1, 0]
            self.pF.loc[len(self.pF)] = [self.lengthb, self.R2, 0]



        elif self.lengthb == self.length:
            R2 = -(self.dF['moment'].sum() + self.pF['moment'].sum())/self.lengthb
            R1 = -(self.dF['eqforce'].sum() + self.pF['force'].sum()) - R2

            
            self.pF.loc[len(self.pF)] = [0, R1, 0]
            self.pF.loc[len(self.pF)] = [self.length, R2, self.length*R2]

            self.R1 = R1
            self.R2 = R2

        
        else:
            R2 = -(self.dF['moment'].sum() + self.pF['moment'].sum())/self.lengthb
            R1 = -(self.dF['eqforce'].sum() + self.pF['force'].sum()) - R2

            
            self.pF.loc[len(self.pF)] = [self.lengtha, R1, self.lengtha*R1]
            self.pF.loc[len(self.pF)] = [(self.lengtha+self.lengthb), R2, R2*(self.lengtha+self.lengthb)]

            self.R1 = R1
            self.R2 = R2



        moment = self.pF['moment'].sum() +self.dF['moment'].sum()
        return R1,R2, moment

        

    def make_vectorizable(expr, var):
        expr = sp.sympify(expr)
        if var not in expr.free_symbols:
            expr = sp.Lambda(var, expr)(var)  # force it to depend on var
        return expr




    def sfd(self, res=200):
        plt.figure(1)
        fig, ax1 = plt.subplots()
        plt.axhline(y=0, lw=1, color='k')
        plt.axvline(x=0, lw=1, color='k')

        x = sp.symbols('x')
        x0 = 0
        breakpoints = pd.concat([self.pF['distance'], self.dF['idistance'],self.dF['fdistance']], ignore_index=True )

   

        if breakpoints.shape == (1,):
            return
        
        breakpoints.sort_values(inplace=True)
        print('breakpoints : \n', breakpoints)

        print('\n\nSFD VALUES')
        for i in breakpoints:

            x1 = i
            x_vals = np.linspace(x0, x1, res)




            #point forces
            # V = sp.sympify(  f"  {  sp.Lambda(x, (self.pF.loc[self.pF['distance']<x1, 'force'].sum()))(x)  }"  )
            V = sp.sympify(  f"  {   (self.pF.loc[self.pF['distance']<x1, 'force'].sum())  } "  )


            # distributed forces partially inside the breakpoint (requires integration)
            eqnseries = self.dF.loc[ (self.dF['idistance']<x1), 'localeqn']
            for eqn in eqnseries:
                eqn = sp.integrate(eqn, x)
                eqn = eqn.subs('x', f'x-{x0}')
                V = sp.Add(V, eqn)
            
            V=V+0*x
            V = getForces.make_vectorizable(V,x)
            
            




            f = sp.lambdify(x, V, "numpy")

            y_vals = f(x_vals)

            if (type(y_vals) == int) or (type(y_vals) == float):
                y_vals = np.full_like(x_vals, y_vals)
            
            print(V, f'plotting in x_range: ({x0} , {x1})',)
            plt.plot(x_vals, y_vals)

            x0 = x1


        plt.xlabel("x")
        plt.ylabel("SFD")
        plt.title(f"SFD Diagram")
        plt.grid(True)
        plt.savefig('SFD_PLT.jpg')
        # plt.show()
        return plot_to_img(fig)







    def bmd(self, res=200):
        plt.figure(2)
        fig, ax1 = plt.subplots()
        plt.axhline(y=0, lw=1, color='k')
        plt.axvline(x=0, lw=1, color='k')
        x = sp.symbols('x')
        x0 = 0
        Bx0 = 0
        
        
        breakpoints = pd.concat([self.pF['distance'], self.dF['idistance'],self.dF['fdistance']], ignore_index=True )
        if breakpoints.shape == (1,):
            return
        breakpoints.sort_values(inplace=True)
        print('\n\nPlotting BMD VALUES...')
        for i in breakpoints:
            x1 = i
            x_vals = np.linspace(x0, x1, res)




            #point forces
            
            V = sp.sympify(  f"  {   (self.pF.loc[self.pF['distance']<x1, 'force'].sum())  }"  )



            # distributed forces partially inside the breakpoint (requires integration)
            eqnseries = self.dF.loc[ (self.dF['idistance']<x1), 'localeqn']
            for eqn in eqnseries:
                eqn = sp.integrate(eqn, x)
                eqn = eqn.subs('x', f'x-{x0}')
                V = sp.Add(V, eqn)
            
            V=V+0*x
            

            B = sp.integrate(V, x)+ Bx0
            B = B.subs('x', f'x-{x0}')

            f = sp.lambdify(x, B, "numpy")

            print(B, f'plotting in x_range: ({x0} , {x1})',)
            y_vals = f(x_vals)
            if (type(y_vals) == int) or (type(y_vals) == float):
                y_vals = np.full_like(x_vals, y_vals)
            plt.plot(x_vals, y_vals)
            Bx0 = B.subs('x',x1)
            x0 = x1

        plt.xlabel("x")
        plt.ylabel("BMD")
        plt.title(f"BMD Diagram")
        plt.grid(True)

        plt.savefig('BMD_PLT.jpg')
        return plot_to_img(fig)
        # return plt.gcf()
        # plt.show()


