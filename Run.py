#--- Imports from other programs
from LogicProgram import VapeList
from CigeretteProgram import CigaretteList
from CigarProgram import CigarsList
from CannabisProgram import CannabisList
from ZynProgram import ZynList
from TobaccoProgram import TobaccoList


Vape_List = VapeList()
Cigarette_List = CigaretteList()
Cigars_List = CigarsList()
Cannabis_List = CannabisList()
Zyn_List = ZynList()
Tobacco_List = TobaccoList()


#--- Main Function ---#
try:
    def main():
        is_running = True
        while is_running:  # loop to run program
            print("~~~~~Substance Counting Program~~~~~")
            print("1. Add Vape")
            print("2. Add Cigarettes")
            print("3. Add Cigars")
            print("4. Add Cannabis Flower")
            print("5. Add Zyns")
            print("6 Add Tobacco")
            print("7. Print to file")
            print("8. Exit")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            choice = int(input("Enter a choice: "))

            if choice == 1:
                is_sub_running = True # a sub running variable to run program
                while is_sub_running: # loop to run program
                    print("~~~~~Substance Counting Program~~~~~")
                    print("1. Add new vape")
                    print("2. Print out list of vapes")
                    print("3. Delete Vape from list")
                    print("4. Print Brands of Vapes")
                    print("5. Add stock to Existing Vape")
                    print("6. Exit")
                    choice = int(input("Enter a choice: "))

                    if choice == 1: # Statement that adds vape to list
                        brand = input("What is the brand of the vape?: ")
                        name = input("What is the name of the vape?: ")
                        stock = int(input("How much?: "))
                        Vape_List.add(brand,name,stock)
                        print(brand,"|",name,"|",stock,"|","has been added to the list")
                    elif choice == 2: #statement that prints out the list of vapes
                        Vape_List.printItems()
                    elif choice == 3: # Statement that deletes certain item in list of vapes
                        brand_choice = input("Please enter the brand of Vape: ")
                        name_choice = input("Please enter the name: ")
                        Vape_List.delItem(brand_choice,name_choice)
                    elif choice == 4: # Statement that checks for the brand so that he shows all items of that brand
                        choice = input("What brand list would you like to see?: ")
                        Vape_List.ItemBrand(brand,choice)
                    elif choice == 5:
                        brand = input("Please enter brand of Vape: ")
                        name = input("Please enter name of Vape: ")
                        stock = int(input("How much stock would you like to add?: "))
                        Vape_List.addToItem(brand,name,stock)
                    elif choice == 6: # Statement ends program
                        is_sub_running = False
                        print("You exit the vape section")
            elif choice == 2:
                is_sub_running = True  # a sub running variable to run program
                while is_sub_running:  # loop to run program
                    print("~~~~~Substance Counting Program~~~~~")
                    print("1. Add new Cigarette")
                    print("2. Print out list of Cigarettes")
                    print("3. Delete Cigarette from list")
                    print("4. Print Brands of Cigarettes")
                    print("5. Add stock to Existing Cigarette")
                    print("6. Exit")
                    choice = int(input("Enter a choice: "))

                    if choice == 1:  # Statement that adds items to list
                        brand = input("What is the brand of the Cigarette?: ")
                        name = input("What is the name of the Cigarette?: ")
                        stock = int(input("How much?: "))
                        Cigarette_List.add(brand, name, stock)
                        print(brand, "|", name, "|", stock, "|", "has been added to the list")
                    elif choice == 2:  # statement that prints out the list of items
                        Cigarette_List.printItems()
                    elif choice == 3:  # Statement that deletes certain item in list of items
                        brand_choice = input("Please enter the brand of Cigarette: ")
                        name_choice = input("Please enter the name: ")
                        Cigarette_List.delItem(brand_choice, name_choice)
                    elif choice == 4:  # Statement that checks for the brand so that he shows all items of that brand
                        choice = input("What brand list would you like to see?: ")
                        Cigarette_List.ItemBrand(brand, choice)
                    elif choice == 5:
                        brand = input("Please enter brand of Cigarette: ")
                        name = input("Please enter name of Cigarette: ")
                        stock = int(input("How much stock would you like to add?: "))
                        Cigarette_List.addToItem(brand, name, stock)
                    elif choice == 6:  # Statement ends program
                        is_sub_running = False
                        print("You exit the Cigarette section")
            elif choice == 3:
                is_sub_running = True  # a sub running variable to run program
                while is_sub_running:  # loop to run program
                    print("~~~~~Substance Counting Program~~~~~")
                    print("1. Add new Cigar")
                    print("2. Print out list of Cigars")
                    print("3. Delete Cigar from list")
                    print("4. Print Brands of Cigar")
                    print("5. Add stock to Existing Cigar")
                    print("6. Exit")
                    choice = int(input("Enter a choice: "))

                    if choice == 1:  # Statement that adds item to list
                        brand = input("What is the brand of the Cigar?: ")
                        name = input("What is the name of the Cigar?: ")
                        stock = int(input("How much?: "))
                        Cigars_List.add(brand, name, stock)
                        print(brand, "|", name, "|", stock, "|", "has been added to the list")
                    elif choice == 2:  # statement that prints out the list of items
                        Cigars_List.printItems()
                    elif choice == 3:  # Statement that deletes certain item in list of items
                        brand_choice = input("Please enter the brand of Cigarette: ")
                        name_choice = input("Please enter the name: ")
                        Cigars_List.delItem(brand_choice, name_choice)
                    elif choice == 4:  # Statement that checks for the brand so that he shows all items of that brand
                        choice = input("What brand list would you like to see?: ")
                        Cigars_List.ItemBrand(brand, choice)
                    elif choice == 5:
                        brand = input("Please enter brand of Cigar: ")
                        name = input("Please enter name of Cigar: ")
                        stock = int(input("How much stock would you like to add?: "))
                        Cigars_List.addToItem(brand, name, stock)
                    elif choice == 6:  # Statement ends program
                        is_sub_running = False
                        print("You exit the Cigar section")
            elif choice == 4:
                is_sub_running = True  # a sub running variable to run program
                while is_sub_running:  # loop to run program
                    print("~~~~~Substance Counting Program~~~~~")
                    print("1. Add new Cannabis")
                    print("2. Print out list of Cannabis")
                    print("3. Delete Cannabis from list")
                    print("4. Print Brands of Cannabis")
                    print("5. Add stock to Existing Cannabis")
                    print("6. Exit")
                    choice = int(input("Enter a choice: "))

                    if choice == 1:  # Statement that adds item to list
                        brand = input("What is the brand of the Cannabis?: ")
                        name = input("What is the name of the Cannabis?: ")
                        stock = int(input("How much?: "))
                        Cannabis_List.add(brand, name, stock)
                        print(brand, "|", name, "|", stock, "|", "has been added to the list")
                    elif choice == 2:  # statement that prints out the list of items
                        Cannabis_List.printItems()
                    elif choice == 3:  # Statement that deletes certain item in list of items
                        brand_choice = input("Please enter the brand of Cannabis: ")
                        name_choice = input("Please enter the name: ")
                        Cannabis_List.delItem(brand_choice, name_choice)
                    elif choice == 4:  # Statement that checks for the brand so that he shows all items of that brand
                        choice = input("What brand list would you like to see?: ")
                        Cannabis_List.ItemBrand(brand, choice)
                    elif choice == 5:
                        brand = input("Please enter brand of Cannabis: ")
                        name = input("Please enter name of Cannabis: ")
                        stock = int(input("How much stock would you like to add?: "))
                        Cannabis_List.addToItem(brand, name, stock)
                    elif choice == 6:  # Statement ends program
                        is_sub_running = False
                        print("You exit the Cannabis section")
            elif choice == 5:
                is_sub_running = True  # a sub running variable to run program
                while is_sub_running:  # loop to run program
                    print("~~~~~Substance Counting Program~~~~~")
                    print("1. Add new Zyn")
                    print("2. Print out list of Zyns")
                    print("3. Delete Zyn from list")
                    print("4. Print Brands of Zyn")
                    print("5. Add stock to Existing Zyn")
                    print("6. Exit")
                    choice = int(input("Enter a choice: "))

                    if choice == 1:  # Statement that adds item to list
                        brand = input("What is the brand of the Zyn?: ")
                        name = input("What is the name of the Zyn?: ")
                        stock = int(input("How much?: "))
                        Zyn_List.add(brand, name, stock)
                        print(brand, "|", name, "|", stock, "|", "has been added to the list")
                    elif choice == 2:  # statement that prints out the list of items
                        Zyn_List.printItems()
                    elif choice == 3:  # Statement that deletes certain item in list of items
                        brand_choice = input("Please enter the brand of Zyn: ")
                        name_choice = input("Please enter the name: ")
                        Zyn_List.delItem(brand_choice, name_choice)
                    elif choice == 4:  # Statement that checks for the brand so that he shows all items of that brand
                        choice = input("What brand list would you like to see?: ")
                        Zyn_List.ItemBrand(brand, choice)
                    elif choice == 5:
                        brand = input("Please enter brand of Zyn: ")
                        name = input("Please enter name of Zyn: ")
                        stock = int(input("How much stock would you like to add?: "))
                        Zyn_List.addToItem(brand, name, stock)
                    elif choice == 6:  # Statement ends program
                        is_sub_running = False
                        print("You exit the Zyn section")
            elif choice == 6:
                is_sub_running = True  # a sub running variable to run program
                while is_sub_running:  # loop to run program
                    print("~~~~~Substance Counting Program~~~~~")
                    print("1. Add new Tobacco")
                    print("2. Print out list of Tobacco")
                    print("3. Delete Tobacco from list")
                    print("4. Print Brands of Tobacco")
                    print("5. Add stock to Existing Tobacco")
                    print("6. Exit")
                    choice = int(input("Enter a choice: "))

                    if choice == 1:  # Statement that adds item to list
                        brand = input("What is the brand of the Tobacco?: ")
                        name = input("What is the name of the Tobacco?: ")
                        stock = int(input("How much?: "))
                        Tobacco_List.add(brand, name, stock)
                        print(brand, "|", name, "|", stock, "|", "has been added to the list")
                    elif choice == 2:  # statement that prints out the list of items
                        Tobacco_List.printItems()
                    elif choice == 3:  # Statement that deletes certain item in list of items
                        brand_choice = input("Please enter the brand of Tobacco: ")
                        name_choice = input("Please enter the name: ")
                        Tobacco_List.delItem(brand_choice, name_choice)
                    elif choice == 4:  # Statement that checks for the brand so that he shows all items of that brand
                        choice = input("What brand list would you like to see?: ")
                        Tobacco_List.ItemBrand(brand, choice)
                    elif choice == 5:
                        brand = input("Please enter brand of Tobacco: ")
                        name = input("Please enter name of Tobacco: ")
                        stock = int(input("How much stock would you like to add?: "))
                        Tobacco_List.addToItem(brand, name, stock)
                    elif choice == 6:  # Statement ends program
                        is_sub_running = False
                        print("You exit the Tobacco section")
            elif choice == 7: # this segment is for writing information to file
                try:
                    #Collect content from the lists
                    items = [
                        Vape_List.printItems(),
                        Cigarette_List.printItems(),
                        Cigars_List.printItems(),
                        Cannabis_List.printItems(),
                        Tobacco_List.printItems(),
                        Zyn_List.printItems()
                    ]

                    # Filter out None values and store valid content
                    valid_content = [items]

                    content = "\n".join(valid_content)

                    #Write the content to the file
                    with open('test.txt','w') as file:
                        file.write(content)

                    print("Content successfully written to 'test.txt'.")

                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == 8:
                is_running = False
                print("Thank you for using this program!")
            else:
                pass
    main()
except ValueError as e:
    print(e)
    print("Enter only numbers")

except Exception as e:
    print(e)
    print("Something went wrong")