def getRangedInt(self, min, max):
    while True:
        try:
            myInt = int(input('please choose an option between %d and %d >>' %(min, max)))
            if myInt  < min or myInt > max:
                print('Invalid option')
            else:
                return myInt
        except ValueError:
            print('Invalid option')


print('myInt = %d' %getRangedInt(1, 4))
