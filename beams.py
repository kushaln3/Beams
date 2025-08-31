import ops







class Beam:

    def __init__(self, isWeb = False):
        self.isWeb = isWeb
        if isWeb == False:    
            self.printex = ops.Printex()


    def simple(self, lengthb = None, pF = None, dF = None):
        if self.isWeb == True:
            gF = ops.getForces(lengthb, lengthb, 0, isWeb = self.isWeb) #initialize getForces object, in simple beam lengthb = length
            
            #takes point forces input from user # pF is a database of point forces
            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
            
            #takes ditributed forces input from user # pF is a database of distributed forces
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']
            

        else:
            length = int(input('Enter length of beam: '))
            gF = ops.getForces(length, length, 0, isWeb = self.isWeb) #initialize getForces object, in simple beam lengthb = length

            #takes point forces input from user # pF is a database of point forces
            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
        

            #takes ditributed forces input from user # pF is a database of distributed forces            
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']



        R1, R2, moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if moment>0:
            self.printex.unstable() # checks if system is statically stable ie. r2>=0 for simple beam
        
        print(R1,R2,'\n',dF,'\n',pF)

        fig1 = gF.sfd()
        fig2 = gF.bmd()
        return fig1, fig2


    def canti(self,lengtha = None, pF = None,dF = None ):
        length = int(input('Enter length of beam: '))
        if self.isWeb == False:
            gF = ops.getForces(length, None, 0, isWeb=False) #initialize getForces object, in cantiliver beam pass only length, others must be None

            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces() #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces() #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']

        else:
            gF = ops.getForces(length, None, 0, isWeb=True) #initialize getForces object, in cantiliver beam pass only length, others must be None
            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']


        R1,R2,moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if moment>0:
            self.printex.unstable() # checks if system is statically stable ie. moment<=0 
        
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

            gF = ops.getForces(length, lengthb, lengthc, isWeb=False) #initialize getForces object, pass all lengths for mixed beam

            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces() #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces() #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']
       
        else:


            length = lengtha + lengthb + lengthc

            gF = ops.getForces(length, lengthb, lengthc, isWeb=True) #initialize getForces object, pass all lengths for mixed beam

            #takes point forces input from user # pF is a database of point forces

            pF = gF.getPforces(pF) #['distance', 'force', 'moment']
            

            #takes ditributed forces input from user # pF is a database of distributed forces
            
            dF = gF.getDforces(dF) #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']



        R1, R2, moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if moment>0:
            self.printex.unstable() # checks if system is statically stable ie. moment<=0 
        
        print(R1,'\n',dF,'\n',pF)

        fig1 = gF.sfd()
        fig2 = gF.bmd()
        return fig1, fig2