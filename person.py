
class Person(object):

    def __init__(self, name, password, address = [None, None, None, None]):
        self.name = name
        self.password = password
        self.address = address
        
    def get_address(self):
        return self.address

    def update_name(self, name):
        self.name = name

    def update_address(self, address): ### takes a list as a parameter.
        self.adress = address
        
        
    def get_name(self):
        return self.name

    def print_details(self):
        print("Name %s:" %self.name)
        print("Address: %s" %self.address[0])
        print("         %s" %self.address[1])
        print("         %s" %self.address[2])
        print("         %s" %self.address[3])
        print(" ")


    def check_password(self, password):
        if self.password == password:
            return True
        return False

    def profile_settings_menu(self):
        #print the options you have
         print (" ")
         print ("Your Profile Settings Options Are:")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Update name & address")
         print ("2) Update password")
         print ("3) Print details")
         print ("4) Back")
         print (" ")
         option = int(input ("Choose your option: "))
         return option
    
    def update_password(self):
        return self.password
    def get_password(self):
        return self.password
    
           
    def run_profile_options(self):
        loop = 1           
        while loop == 1:
            choice = self.profile_settings_menu()
            if choice == 1:
            ### this is  the method used so that you can change names.
                option=input("\nCurrent name is%s. Change (Y/N)? " %self.get_name())
                if option.upper() == 'Y':
                    name = input('Please enter new name')
                    self.update_name(name)
                tempAdd = []
                option = input("\nAddress line 1 is %s. Change (Y/N)?  " %(self.get_address())[0])
                if option.upper() == 'y':
                    temp = input('please enter a new line 1: ')
                    tempAdd.append(temp)
                else:
                    tempAdd.append(self.get_address()[0])
                option = input("\nAddress line 2 is %s.change (Y/N)?  " %(self.get_address())[1])
                if option.upper() == 'Y':
                    temp = input('Please enter new line 2:  ')
                    tempAdd.append(temp)
                else:
                    tempAdd.append(self.get_address()[1])
                option = input("\nAddress line 3 is %s. Change (Y/N)? " %(self.get_address())[2])
                if option.upper() == 'Y':
                    temp = input(' please enter new line 3:  ')
                    tempAdd.append(temp)
                else:
                    tempAdd.append(self.get_address()[2])
                option = input("\nAddress line 4 is %s. Change (Y/N)? " %(self.get_address())[3])
                if option.upper() =='Y':
                    temp = input ('Please enter new line 4: ')
                    tempAdd.append(temp)
                else:
                    tempAdd.append(self.get_address()[3])
                self.update_address(tempAdd)
     

            elif choice == 2:
                while True:
                    password = input("\nCurrent password is %s. Please enter a new password (between 6 & 10 alphanumreic characters) >> " %self.get_password())
                    if len(password) < 6 or len(password) > 10 :
                        print ('not the correct format. Try again......')
                    else:
                        self.password=password
                        print('Password Updated')
                        break
                        
                        




                    
            elif choice == 3:
                self.print_details()
            elif choice == 4:
                loop = 0                     
