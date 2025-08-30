import ops







class Beam:

    def __init__(self):
        self.printex = ops.Printex()


    def simple(self):
        length = int(input('Enter length of beam: '))

        gF = ops.getForces(length, length, 0) #initialize getForces object, in simple beam lengthb = length

        #takes point forces input from user # pF is a database of point forces

        pF = gF.getPforces() #['distance', 'force', 'moment']
        

        #takes ditributed forces input from user # pF is a database of distributed forces
        
        dF = gF.getDforces() #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']



        R1, R2, moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if moment>0:
            self.printex.unstable() # checks if system is statically stable ie. r2>=0 for simple beam
        
        print(R1,R2,'\n',dF,'\n',pF)

        gF.sfd()
        gF.bmd()


    def canti(self):
        length = int(input('Enter length of beam: '))

        gF = ops.getForces(length, None, 0) #initialize getForces object, in cantiliver beam pass only length, others must be None

        #takes point forces input from user # pF is a database of point forces

        pF = gF.getPforces() #['distance', 'force', 'moment']
        

        #takes ditributed forces input from user # pF is a database of distributed forces
        
        dF = gF.getDforces() #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']



        R1,R2,moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if moment>0:
            self.printex.unstable() # checks if system is statically stable ie. moment<=0 
        
        print(R1,'\n',dF,'\n',pF)

        gF.sfd()
        gF.bmd()

    def mixed(self):
        lengtha = float(input('Enter length of beam part a: '))
        lengthb = float(input('Enter length of beam part b: '))
        lengthc = float(input('Enter length of beam part c: '))
        length = lengtha + lengthb + lengthc

        gF = ops.getForces(length, lengthb, lengthc) #initialize getForces object, pass all lengths for mixed beam

        #takes point forces input from user # pF is a database of point forces

        pF = gF.getPforces() #['distance', 'force', 'moment']
        

        #takes ditributed forces input from user # pF is a database of distributed forces
        
        dF = gF.getDforces() #['idistance', 'fdistance', 'eqn', 'eqforce', 'eqdistance', 'moment']



        R1, R2, moment = gF.Reactions() # calculates reaction forces at r1 and r2
        if moment>0:
            self.printex.unstable() # checks if system is statically stable ie. moment<=0 
        
        print(R1,'\n',dF,'\n',pF)

        gF.sfd()
        gF.bmd()

        
        
        


