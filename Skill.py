class Skill:
    def __init__(self, name ,effect):
        self.name = name 
        self.effect = effect
        
    def getEffect(self):
        return self.effect