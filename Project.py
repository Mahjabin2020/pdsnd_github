import pandas as pd
import numpy as np
import time
from time import sleep

hyp = "-"*40
fails = []



def time_stats():
    print(hyp+"\nFetching time-related statistics.....\n\n")
    sleep(2)
    t= time.time()

    #month
    
    months = ["fill","January","February","March","April","May","June"]
    
    m_mode = int(data["Start Time"].dt.month.mode())

    month = months[m_mode]

    print(hyp + "\nMost popular month: " + month)

    #weekday

    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    w_mode = int(data["Start Time"].dt.weekday.mode())

    weekday = weekdays[w_mode]
    print("\n\nMost popular day of the week: " + weekday)

    #hour

    h_mode = int(data["Start Time"].dt.hour.mode())

    print("\n\nMost popular hour of the day: " + str(h_mode) + "\n" + hyp)
    print("\nTime taken for this operation: " + str(time.time() - t) + " seconds\n")

def station_stats():
    print(hyp+"\nFetching Station-related statistics......\n\n")
    sleep(2)
    t = time.time()

    #start station

    s_station = data["Start Station"].mode().to_string(index = False)

    print(hyp + "\nMost popular start station: " + s_station)

    #end station

    e_station = data["End Station"].mode().to_string(index = False)

    print("\nMost popular end station: " + e_station)

    #trip

    trip = data.groupby(["Start Station","End Station"]).size().sort_values(ascending = False).idxmax()
    print("\nMost popular trip('Start Station','End Station'): " + "\n" + str(trip) + "\n" + hyp)

    print("\nTime taken for this operation: " + str(time.time() - t) + " seconds\n")
    
def trip_duration():
    print(hyp+"\nFetching Trip Duration-related statistics......\n\n")
    sleep(2)
    t = time.time()

    #total

    total = data["Trip Duration"].sum()
    print(hyp + "\nTotal travel time: " + str(total) + " seconds\n")

    #average

    avg = data["Trip Duration"].mean()
    print("Average travel time: " + str(avg) + " seconds\n" + hyp)
    print("\nTime taken for this operation: " + str(time.time() - t) + " seconds\n")


def user_info():
    print(hyp+"\nFetching User Info-related statistics......\n\n")
    sleep(2)
    t = time.time()

    #user type

    type_count = data["User Type"].value_counts()
    print(hyp + "\nNumber of users in each user type: \n\n" + str(type_count) + " <----- Ignore this line")

    if inp.lower() != "washington" and inp.lower() != "3":

          #gender

          gen_count = data["Gender"].value_counts()
          print("\nNumber of users of each gender: \n\n" + str(gen_count) + " <----- Ignore this line")

          #birth
          print("\nStatistics related to the birth year of users:\n")
          a = int(data["Birth Year"].min())
          print("\n  Earliest Birth Year: " + str(a))

          b = int(data["Birth Year"].max())
          print("\n  Most recent Birth Year: " + str(b))

          c = data["Birth Year"].mode().to_string(index = False)
          print("\n  Most common Birth Year: " + str(c) + "\n")
    print(hyp + "\n\nTime taken for this operation: " + str(time.time() - t) + " seconds\n") 

def raw_data():
    while True: 
       inp = input("\nWould you like to view 5 rows of individual trip data?\nEnter yes or no: ").lower()
       if inp == "yes":
           start = 0
           while True:
               print("\n\n")
               print(data.iloc[start:start+5])
               start += 5
               if start == 300000:
                   print("\nThere is no further data.\n")
                   fails.append("no data")
                   break
               while True:
                 cont = input("\n\nDo you wish to continue?\nEnter yes or no: ").lower()
               
                 if cont == "yes":
                   break
                 elif cont == "no":
                   fails.append("no cont")
                   break
                 else:
                   print("Your input was not correct.")
               if len(fails) != 0:
                   break
       elif inp == "no":
           break
       else:
           print("\nYour input was not correct.")
        
           re_inp = input(hyp+"\nDo you want to restart?\n('Yes' or 'No')\n")
           if re_inp.lower() != "yes":
              print("Thanks for your time! Please close and re-open the program if you want to try again. ")
              sleep(3000000)
              break
           
       if len(fails) != 0:
           break
               
        
    
print("Hi there! Let's have a look at some US bikeshare data together!")
while True:
 while True:
     inp = input("\nWhich city do you want to know statistics about?\n1.Chicago\n2.New York City\n3.Washington\n(Please enter the city name or 1/2/3)\n\n")
 
     if inp.lower() == "1" or inp.lower() == "chicago":
        data = pd.read_csv('chicago.csv')
        break
     elif inp.lower() == "2" or inp.lower() == "new york city":
        data = pd.read_csv("new_york_city.csv")
        break
     elif inp.lower() == "3" or inp.lower() == "washington":
        data = pd.read_csv("washington.csv")
        break
     else: 
        print("\nYour input was not correct.")
        
        re_inp = input(hyp+"\nDo you want to restart?\n('Yes' or 'No')\n")
        if re_inp.lower() != "yes":
           print("Thanks for your time! Please close and re-open the program if you want to try again. ")
           fails.append(1)
           sleep(3000000)
           break   
     
 if len(fails) == 0 or fails[0] == "no cont" or fails[0] == "no data":
  data["Start Time"] = pd.to_datetime(data["Start Time"])
 
#--------------------------------------------------------------------------------------------------------#
#                                            FILTER                                                      #
#--------------------------------------------------------------------------------------------------------#
  

  while True:    
         print("Do you want to filter your data?\n\n1.'I wish to filter by month'\n2.'I wish to filter by both month and day of the week'\n3.'I do not wish to filter my data'")
         inp1 = input("Please enter(1-3): ")  
         if inp1 == "1":
             
             while True:
                 print("\nWhich month do you want stats about?\n 1.January\n 2.February\n 3.March\n 4.April\n 5.May\n 6.June")
                 inp2 = input("Please enter(1-6): ")
                 if inp2 == "1":
                     data = data[data["Start Time"].dt.month == 1]
                     break
                 elif inp2 == "2":
                     data = data[data["Start Time"].dt.month == 2]
                     break
                 elif inp2 == "3":
                     data = data[data["Start Time"].dt.month == 3]
                     break
                 elif inp2 == "4":
                     data = data[data["Start Time"].dt.month == 4]
                     break
                 elif inp2 == "5":
                     data = data[data["Start Time"].dt.month == 5]
                     break
                 elif inp2 == "6":
                     data = data[data["Start Time"].dt.month == 6]
                     break   
                 else:
                     print("\nYour input was not correct.")
        
                     re_inp2 = input(hyp+"\nDo you want to restart?\n('Yes' or 'No')\n")
                     if re_inp2.lower() != "yes":
                          print("Thanks for your time!\nPlease close and re-open the program if you want to try again.")
                          fails.append(1)
                          sleep(3000000)
                          break 
                 
             break

                 

         elif inp1 == "2":
             while True:
                 print("\nWhich month do you want stats about?\n 1.January\n 2.February\n 3.March\n 4.April\n 5.May\n 6.June")
                 inp2 = input("Please enter(1-6): ")
                 if inp2 == "1":
                     data = data[data["Start Time"].dt.month == 1]
                     break
                 elif inp2 == "2":
                     data = data[data["Start Time"].dt.month == 2]
                     break
                 elif inp2 == "3":
                     data = data[data["Start Time"].dt.month == 3]
                     break
                 elif inp2 == "4":
                     data = data[data["Start Time"].dt.month == 4]
                     break
                 elif inp2 == "5":
                     data = data[data["Start Time"].dt.month == 5]
                     break
                 elif inp2 == "6":
                     data = data[data["Start Time"].dt.month == 6]
                     break   
                 else:
                     print("\nYour input was not correct.")
        
                     re_inp2 = input(hyp+"\nDo you want to restart?\n('Yes' or 'No')\n")
                     if re_inp2.lower() != "yes":
                          print("Thanks for your time!\nPlease close and re-open the program if you want to try again.")
                          fails.append(1)
                          sleep(3000000)
                          break
             while True:
                 print("\nWhich day of the week do you want stats about?\n 1.Monday\n 2.Tuesday\n 3.Wednesday\n 4.Thursday\n 5.Friday\n 6.Saturday\n 7.Sunday")
                 inp3 = input("Please enter(1-7): ")
                 if inp3 == "1":
                     data = data[data["Start Time"].dt.weekday == 0]
                     break
                 elif inp3 == "2":
                     data = data[data["Start Time"].dt.weekday == 1]
                     break
                 elif inp3 == "3":
                     data = data[data["Start Time"].dt.weekday == 2]
                     break
                 elif inp3 == "4":
                     data = data[data["Start Time"].dt.weekday == 3]
                     break
                 elif inp3 == "5":
                     data = data[data["Start Time"].dt.weekday == 4]
                     break
                 elif inp3 == "6":
                     data = data[data["Start Time"].dt.weekday == 5]
                     break
                 elif inp3 == "7":
                     data = data[data["Start Time"].dt.weekday == 6]
                     break
                 else:
                     print("\nYour input was not correct.")
        
                     re_inp2 = input(hyp+"\nDo you want to restart?\n('Yes' or 'No')\n")
                     if re_inp2.lower() != "yes":
                          print("Thanks for your time!\nPlease close and re-open the program if you want to try again.")
                          fails.append(1)
                          sleep(3000000)
                          break 
                 
             break          
                 
             
             


         elif inp1 == "3":
             break
         else:
             print("\nYour input was not correct.")
        
             re_inp3 = input(hyp+"\nDo you want to restart?\n('Yes' or 'No')\n")
             if re_inp3.lower() != "yes":
                print("Thanks for your time!\nPlease close and re-open the program if you want to try again.")
                fails.append(1)
                sleep(300000)
                break

#--------------------------------------------------------------------------------------------------------
            
  if len(fails) == 0 or fails[0] == "no cont" or fails[0] == "no data":
    time_stats()
    station_stats()
    trip_duration()
    user_info()
    raw_data()
    restart_full = input(hyp+"\nDo you want to restart the entire process?\n('Yes' or 'No')\n")
    if restart_full.lower() != "yes":
           print("Thanks for your time!")
           sleep(3)
           break
