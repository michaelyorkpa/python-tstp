def bottles_of_beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. 
        No more bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. 
    {} bottles of beer. 
    Take one down, pass it around, 
    {} bottles of beer on the wall.""".format(tmp,tmp,tmp))
    bottles_of_beer(bob)

bottles_of_beer(99)