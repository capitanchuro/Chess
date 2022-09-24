class Position:
    
    def __init__(self, ID, unit, row, col):
        self.setID(ID)
        self.setUnit(unit)
        self.setRow(row)
        self.setCol(col)
        
    #Setter Methods
    def setID(self, ID):
        self.ID = ID
        
    def setUnit(self, unit):
        self.unit = unit
        
    def setRow(self, row):
        self.row = row
    
    def setCol(self, col):
        self.col = col
     
    #Getter Methods
    def getID(self):
        return self.ID
    
    def getUnit(self):
        return self.unit
    
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
