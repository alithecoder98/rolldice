def dice():
    sides=6
    print("The purpose of this program is to process the outcome of 2 DICES")
    import random
    ran1:int=random.randint(1,sides)
    ran2:int=random.randint(1,sides)
    print(f"The outcome of first dice is {ran1} and outcome of second dice is {ran2} where the sum is {ran1+ran2}")
if __name__=="__main__":
    dice()

    