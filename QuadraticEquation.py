class Vector:
    def __init__(self,a,b,c):
        self.X=a
        self.Y=b
        self.Z=c
    # def __str__(self):
    #     # return f"({self.X}i+{self.Y}j+{self.Z}k)"
    def __repr__(self):
        return f"vector({self.X}i{self.Y}j{self.Z}k)"
    def __len__(self):
        return int((self.X**2+self.Y**2+self.Z**2)**(0.5))
    def __add__(self,v):
        return Vector(self.X+v.X,self.Y+v.Y,self.Z+v.Z)
vector1=Vector(3,6,2)
vector2=Vector(2,5,1)
print(f"Representation of vector is:{repr(vector1)}")
print(f"lenght of vector is:{len(vector1)}")
print(f"Addition of Two vector is:{vector1+vector2}")
