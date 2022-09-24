import position

class Unit:
    
    def __init__(self, ID, type, points, POS):
        self.setID(ID)
        self.setType(type)
        self.setPoints(points)
        self.setPOS(POS)
        
    #Setter Methods
    def setID(self, ID):
        self.ID = ID
        
    def setType(self, type):
        self.type = type
        
    def setPoints(self, points):
        self.points = points
        
    def setPOS(self, POS):
        self.POS = POS
        
    #Getter Methods
    def getID(self):
        return self.ID
    
    def getType(self):
        return self.type
    
    def getPoints(self):
        return self.points
    
    def getPOS(self):
        return self.POS