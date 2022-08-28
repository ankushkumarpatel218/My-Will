def vol(r):

    p1 = r**3
    p2 = 22/7
    p3 = 4/3
    vol= p3*p2*p1
    return vol
r1=float(input("enter :"))
print("volume of sphere of radius",r1 ,"=",vol(r1))