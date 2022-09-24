import unit

class Position:
    
    def __init__(self, ID, row, col):
        self.setID(ID)
        self.setRow(row)
        self.setCol(col)
        
    #Setter Methods
    def setID(self, ID):
        self.ID = ID
        
    def setRow(self, row):
        self.row = row
    
    def setCol(self, col):
        self.col = col
     
    #Getter Methods
    def getID(self):
        return self.ID
    
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col