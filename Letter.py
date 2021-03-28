class Letter:
    def __init__(self, key, points, amount, left = None, right = None):
        self.key = key
        self.points = int(points)
        self.amount = int(amount)
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.key
        