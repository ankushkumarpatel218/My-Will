Data = {}

Keys = ["put keys"]
Values = ["put Values"]

if len(Keys) == len(Values):
    for i in range(len(Keys)):
        if Keys[i] not in Data:
            Data[Keys[i]] = 0

        Data[Keys[i]] += Values[i]

