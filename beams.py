import ops







class Beam:

    def __init__(self, isWeb = False):
        self.isWeb = isWeb
        if isWeb == False:    
            self.printex = ops.Printex()


    def simple(self, lengthb = None, pF = None, dF = None):
        if self.isWeb == True:
            gF = ops.getForces(0, lengthb, 0, isWeb = self.isWeb, btype=1) #initialize getForces object, in simple beam lengthb = length
            
            #takes point forces input from user # pF is a database of point forces
            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
            
            #takes ditributed forces input from user # pF is a database of distributed forces
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']
            

        else:
            length = int(input('Enter length of beam: '))
            gF = ops.getForces(0, length, 0, isWeb = self.isWeb, btype=1) #initialize getForces object, in simple beam lengthb = length

            #takes point forces input from user # pF is a database of point forces
            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
        

            #takes ditributed forces input from user # pF is a database of distributed forces            
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']



        R1, R2, moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if R2<0:
            print("The given system is not static and is unstable, Please enter proper values!!!") # checks if system is statically stable ie. r2>=0 for simple beam
            return False, False
        else:
            fig1 = gF.sfd()
            fig2 = gF.bmd()
            return fig1, fig2


    def canti(self,lengthb = None, pF = None,dF = None ):
        if self.isWeb == False:
            length = int(input('Enter length of beam: '))
            gF = ops.getForces(0, length, 0, isWeb=False, btype = 2) #initialize getForces object, in cantiliver beam pass only length, others must be None

            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces() #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces() #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']

        else:
            gF = ops.getForces(0, lengthb, 0, isWeb=True,btype=2) #initialize getForces object, in cantiliver beam pass only length, others must be None
            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']


        R1,R2,moment = gF.Reactions()
        print("1111111111111111111111got111111111111111111    ", R1,R2)
        
         # calculates reaction forces at r1 and r2
        # if moment>0:
        #     self.printex.unstable() # checks if system is statically stable ie. moment<=0 
        
        print(R1,'\n',dF,'\n',pF)

        fig1 = gF.sfd()
        fig2 = gF.bmd()
        return fig1, fig2


    def mixed(self,lengtha = None, lengthb = None, lengthc = None, pF = None,dF = None):
        
        if self.isWeb == False:
            lengtha = float(input('Enter length of beam part a: '))
            lengthb = float(input('Enter length of beam part b: '))
            lengthc = float(input('Enter length of beam part c: '))
            length = lengtha + lengthb + lengthc

            gF = ops.getForces(length, lengthb, lengthc, isWeb=False, btype=3) #initialize getForces object, pass all lengths for mixed beam

            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces() #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces() #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']
       
        else:


            length = lengtha + lengthb + lengthc

            gF = ops.getForces(length, lengthb, lengthc, isWeb=True, btype=3) #initialize getForces object, pass all lengths for mixed beam

            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']



        R1, R2, moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if R2<0:
            print("The given system is not static and is unstable, Please enter proper values!!!")
            return False,False # checks if system is statically stable ie. moment<=0
        
        else:
            fig1 = gF.sfd()
            fig2 = gF.bmd()
            return fig1, fig2