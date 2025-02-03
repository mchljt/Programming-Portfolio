#Michael Joseph Tjokro S10257089 P07 13 August 2023

#Function to read data from a CSV file
def read_csv(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()
    return data

#Function to parse CSV data and convert it to a list of dictionaries
def parse_csv(data):
    #initialise an empty list to store carpark dictionaries
    carpark_list = []
    #iterate through each line of data
    for line in data:
        ##split the data into individual carpark information items
        carpark_info = line.strip().replace('"','').split(",",3)
        #create a dictionary to store carpark information
        carpark_dict = {
            "Carpark No": carpark_info[0],
            "Carpark Type": carpark_info[1],
            "Type of Parking System": carpark_info[2],
            "Address": carpark_info[3],
        }
        #appends the carpark dictionary to the carpark_list
        carpark_list.append(carpark_dict)
    #returns the list of carpark dictionaries
    return carpark_list

#Main program
file_path = "carpark-information.csv"       #define path to CSV file
data = read_csv(file_path)                  #read data from the CSV file using the read_csv function
carpark_list = parse_csv(data)              #parse the CSV data to create a list of carpark dictionaries using the parse_csv function
options_list = []
valid_options = []
valid_filenames = ["carpark-availability-v1.csv","carpark-availability-v2.csv"]         #Valid file name options
for i in range(0,11):
    valid_options.append(str(i))             #Valid menu options

while True:
    print("")
    print("MENU")
    print("="*4)
    #Menu
    print("[1]  Display Total Number of Carparks in 'carpark-information.csv'")
    print("[2]  Display All Basement Carparks in 'carpark-information.csv'")
    print("[3]  Read Carpark Availability Data File")
    print("[4]  Print Total Number of Carparks in the File Read in [3]")
    print("[5]  Display Carparks Without Available Lots")
    print("[6]  Display Carparks With At Least x% Available Lots")
    print("[7]  Display Addresses of Carparks With At Least x% Available Lots")
    print("[8]  Display All Carparks at Given Location")
    print("[9]  Display Carpark with the Most Parking Lots")
    print("[10] Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
    print("[0]  Exit")
    option = input("Enter your option: ")          #input option
    while option not in valid_options:                  #validating entered option
        print("Invalid option. Please re-enter option.")
        option = input("Enter your option: ")
    options_list.append(option)                         #appending entered option to a list to check if 3 has been entered
    if option!="0":
        #option1
        if option == "1":
            print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
            print("Total Number of carparks in 'carpark-information.csv':",str(len(carpark_list)-1)+".") #subtracted 1 to exclude header
        #option2
        elif option == "2":
            #initialise counter for basement carparks
            basement_count = 0
            #display option and information header
            print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
            print("{:<10} {:<20} {:<5}".format("Carpark No","Carpark Type","Address"))
            #iterate through carpark list
            for i in carpark_list:
                #check if carpark type is "BASEMENT CAR PARK"
                if i["Carpark Type"] == "BASEMENT CAR PARK":
                    #print carpark information for basement carparks
                    print("{:<10} {:<20} {:<5}".format(i["Carpark No"],i["Carpark Type"],i["Address"]))  
                    basement_count+=1
            #print the total number of basement carparks
            print("Total number:",basement_count)
        #option3
        elif option == "3":
            print("Option 3: Read Carpark Availability Data File")
            filename = input("Enter the file name: ").lower()
            while filename not in valid_filenames:                  #validating entered file name
                print("Invalid file name entered. Please re-enter file name.")
                filename = input("Enter the file name: ").lower()
            #opens and reads user-entered file
            file = open(filename)
            print(file.readline().strip())                          #printing timestamp
        #option4
        elif (option == "4" and options_list.count("3")==0):
            print("Please ensure that option 3 has been selected and completed before selecting this option.")
        elif (option == "4" and options_list.count("3")!=0):
            filename_count = 0
            print("Option 4: Print Total Number of Carparks in the File Read in [3]")
            #opens and reads file in [3]
            file = open(filename)
            file.readline()                                         #exclude timestamp
            file.readline()                                         #exclude headers
            #iterate through each line in the file to count carparks
            for i in file:
                filename_count+=1       #increment the counter for each line (each carpark)
            #print the total number of carparks in the file
            print("Total number of Carparks in the File:",filename_count)
        #option5
        elif (option == "5" and options_list.count("3")==0):
            print("Please ensure that option 3 has been selected and completed before selecting this option.")
        elif (option == "5" and options_list.count("3")!=0):
            print("Option 5: Display Carparks without Available Lots")
            #opens and reads file in [3]
            file = open(filename)
            file.readline()                                         #exclude timestamp
            file.readline()                                         #exclude headers
            empty_count = 0         #counter for carparks without available lots
            #iterate through each line in the file
            for i in file:
                i = i.strip().split(",")        #split the line into a list
                #check if the number of available lots is 0
                if i[2] == "0":
                    print("Carpark Number:",i[0])       #print the carpark number
                    empty_count+=1                      #increment the counter for empty carparks
                else:
                    continue
            #print the total number of carparks without available lots
            print("Total Number:",empty_count)
        #option6
        elif (option == "6" and options_list.count("3")==0):
            print("Please ensure that option 3 has been selected and completed before selecting this option.")
        elif (option == "6" and options_list.count("3")!=0):
            print("Option 6: Display Carparks With At Least x% Available Lots")
            percent_required = input("Enter the percentage required: ")
            #validates input percentage
            while True:
                if not percent_required.replace(".", "", 1).isdigit():
                    print("Invalid input! Please enter a value between 0 and 100 (inclusive).")
                    percent_required = input("Enter the percentage required: ")
                elif float(percent_required) < 0 or float(percent_required) > 100:
                    print("Invalid input! Please enter a value between 0 and 100 (inclusive).")
                    percent_required = input("Enter the percentage required: ")
                else:
                    break  #valid input, exit the loop
            #print header for the output
            print("{:<15} {:>15} {:>15} {:>15}".format("Carpark No","Total Lots","Lots Available","Percentage"))
            #opens and reads the file in [3]
            file = open(filename)
            file.readline()     #excludes timestamp                    
            file.readline()     #excludes headers
            carpark_percent_count = 0
            #process each line in the file
            for i in file:
                i = i.strip().split(",")
                #calculate carpark percentage
                if int(i[1])!=0:                
                    carpark_percent = (int(i[2])/int(i[1]))*100
                if int(i[1]) == 0:              
                    carpark_percent = 0
                #checks if carpark meets percentage requirement
                if carpark_percent >= float(percent_required):
                    #print carpark info
                    print("{:<15} {:>15} {:>15} {:>15.1f}".format(i[0],i[1],i[2],carpark_percent))
                    carpark_percent_count+=1
                else:
                    continue
            #print total number of carparks that meet the criteria
            print("Total Number:",carpark_percent_count)
        #option7
        elif (option == "7" and options_list.count("3")==0):
            print("Please ensure that option 3 has been selected and completed before selecting this option.")
        elif (option == "7" and options_list.count("3")!=0):
            print("Option 7: Display Addresses of Carparks With At Least x% Available Lots")
            percent_required = input("Enter the percentage required: ")
            #validate the input percentage
            while True:
                if not percent_required.replace(".", "", 1).isdigit():
                    print("Invalid input! Please enter a value between 0 and 100 (inclusive).")
                    percent_required = input("Enter the percentage required: ")
                elif float(percent_required) < 0 or float(percent_required) > 100:
                    print("Invalid input! Please enter a value between 0 and 100 (inclusive).")
                    percent_required = input("Enter the percentage required: ")
                else:
                    break  #valid input, exit the loop
            #header for the output
            print("{:<15} {:>15} {:>20} {:>15} {:>5}".format("Carpark No","Total Lots","Lots Available","Percentage","Address"))
            #opens and reads the file in [3]
            file = open(filename)
            file.readline()             #excludes timestamp
            file.readline()             #excludes headers
            carpark_no_list = []        
            carpark_percent_count = 0
            #extract carpark numbers from carpark_list
            for j in carpark_list:
                carpark_no_list.append(j["Carpark No"])
            #process each line in the file
            for i in file:
                i = i.strip().split(",")
                #calculate carpark percentage
                if int(i[1])!=0:                            
                    carpark_percent = (int(i[2])/int(i[1]))*100
                if int(i[1]) == 0:                          
                    carpark_percent = 0
                #check if carpark meets percentage requirement
                if carpark_percent >= float(percent_required):  
                    if i[0] not in carpark_no_list:
                        #print carpark info without address
                        print("{:<15} {:>15} {:>20} {:>15.1f} {:<5}".format(i[0],i[1],i[2],carpark_percent," "))
                        carpark_percent_count+=1
                    for x in carpark_list:                  
                        if i[0] == x["Carpark No"]:
                            #print carpark info with address
                            print("{:<15} {:>15} {:>20} {:>15.1f} {:<5}".format(i[0],i[1],i[2],carpark_percent,x["Address"]))
                            carpark_percent_count+=1
                else:
                    continue
            #print the total number of carparks that meet the criteria
            print("Total number:",carpark_percent_count)
        #option8
        #checks if option 8 is selected and option 3 has been completed
        elif (option == "8" and options_list.count("3") == 0):
            print("Please ensure that option 3 has been selected and completed before selecting this option.")
        #option 8 selected and option 3 completed
        elif (option == "8" and options_list.count("3")!=0):
            print("Option 8: Display All Carparks at Given Location")
            carpark_location_count = 0
            location = input("Please enter a location: ").upper()   #prompts user for location input
            file = open(filename)   #opens and reads file in option 3
            file.readline()         #excludes timestamp
            file.readline()         #excludes headers
            carparks_found = False #Flag to track if carparks were found at specified location
            #loops through the file to find carparks at given location
            for y in carpark_list:
                if location in y["Address"]:
                    # Set flag to indicate carparks are found at the specified location
                    carparks_found  = True
                    break
            #checks if carparks are found at the specified location
            if not carparks_found:
                print("No carparks found in the specified location.")
            else:
                #displays header for the result table
                print("{:<15} {:>15} {:>20} {:>15} {:>5}".format("Carpark No","Total Lots","Lots Available","Percentage","Address"))
                #loop through the carpark list to match location and display data
                for j in carpark_list:
                    if location in j["Address"]:
                        #read carpark data from file in [3]
                        file = open(filename)
                        file.readline()     #excludes timestamp
                        file.readline()     #excludes headers
                        for x in file:
                            x = x.strip().split(",")
                            if j["Carpark No"] == x[0]:
                                #calculates percentage available
                                if int(x[1])!=0:
                                    carpark_percent = (int(x[2])/int(x[1]))*100
                                else:
                                    carpark_percent = 0
                                #Display carpark information
                                print("{:<15} {:>15} {:>20} {:>15.1f} {:>5}".format(x[0],x[1],x[2],carpark_percent,j["Address"]))                   
                                carpark_location_count+=1
                            else:
                                continue
                    else:
                        continue
                #Display total number of carparks found at the location
                print("Total number of carparks found:",carpark_location_count)
        #option9
        elif (option == "9" and options_list.count("3") == 0):
            print("Please ensure that option 3 has been selected and completed before selecting this option.")
        elif (option == "9" and options_list.count("3") != 0):
            print("Option 9: Display Carpark with the Most Parking Lots")
            highest = 0
            #Open and read file in [3]
            file = open(filename)
            file.readline()     #exclude timestamp
            file.readline()     #exclude headers
            #loop through the file to find the carpark with the most parking lots
            for i in file:
                i = i.strip().split(",")
                if int(i[1]) > highest:
                    highest = int(i[1])
                    carpark_number = i[0]
                    total_lots = highest
                    lots_available = i[2]
                    percentage = (int(lots_available)/int(total_lots))*100  #calculates percentage
                    #find matching carpark information from carpark_list
                    for j in carpark_list:
                        if carpark_number == j["Carpark No"]:
                            carpark_type = j["Carpark Type"]
                            parking_system = j["Type of Parking System"]
                            address = j["Address"]
                        else:
                            continue
                else:
                    continue
            #Display carpark details with the most parking lots
            print("Carpark Number:",carpark_number)
            print("Carpark Type:",carpark_type)
            print("Type of Parking System:",parking_system)
            print("Total Lots:",total_lots)
            print("Lots Available:",lots_available)
            print("Percentage: {:.1f}%".format(percentage))
            print("Address:",address)
        #option10
        elif (option == "10" and options_list.count("3") == 0):
            print("Please ensure that option 3 has been selected and completed before selecting this option.")
        elif (option == "10" and options_list.count("3") != 0):
            print("Option 10: Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
            #open and read file in [3]
            file = open(filename)
            timestamp = file.readline()     #reads timestamp
            headers = file.readline()       #reads headers
            #initialisation
            option3_lst = []
            carpark_no_list = []
            line_count = 0
            #loop through the file to gather carpark data for sorting
            for i in file:
                info_lst = []
                i = i.strip().split(",")
                info_lst.append(int(i[2]))  #Lots available
                info_lst.append(int(i[1]))  #total lots
                info_lst.append(i[0])       #carpark number
                option3_lst.append(info_lst)
            option3_lst.sort()      #sort the gathered carpark information by lots available
            #creating a list of carpark numbers for easy checking
            for y in carpark_list:
                carpark_no_list.append(y["Carpark No"])
            #Creating a new CSV file for writing carpark availability with addresses
            with open("carpark-availability-with-addresses.csv","w") as file:
                #writing timestamp and headers to new file
                file.write(timestamp)
                file.write(headers.strip())
                file.write(",Address\n")
                line_count+=2
                #loop through sorted carpark information and carpark list
                for j in option3_lst:
                    for x in carpark_list:
                        if j[2] not in carpark_no_list:
                            file.write(j[2]+",")
                            file.write(str(j[1])+",")
                            file.write(str(j[0])+",")
                            if x["Address"]!="":
                                file.write(" \n")
                                line_count+=1
                            break
                        else:
                            if j[2] == x["Carpark No"]:
                                file.write(j[2]+",")
                                file.write(str(j[1])+",")
                                file.write(str(j[0])+",")
                                if x["Address"]!="":
                                    file.write('"'+x["Address"]+'"'+'\n')
                                    line_count+=1
            #print information about new file
            print("Filename:","carpark-availability-with-addresses.csv")
            print("Number of lines written into file:",line_count)
    #option0
    elif option == "0":
        break
