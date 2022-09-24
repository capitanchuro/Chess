import position

class Unit:
    
    def __init__(self, ID, name, points, POS = 0):
        self.setID(ID)
        self.setName(name)
        self.setPoints(points)
        self.setPOS(POS)
        
    #Setter Methods
    def setID(self, ID):
        self.ID = ID
        
    def setName(self, name):
        self.name = name
        
    def setPoints(self, points):
        self.points = points
        
    def setPOS(self, POS):
        self.POS = POS
        
    #Getter Methods
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name
    
    def getPoints(self):
        return self.points
    
    def getPOS(self):
        return self.POS
