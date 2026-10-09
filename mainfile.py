import SQLfile
import mysql.connector as m
import random as r
#SQLfile.createtable()
def addrec():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIES")
        cur=con.cursor()
        print("CURRENTLY POPULAR SHOWS".center(25,'-'))
        print('1. Backrooms','2. Colony','3. Dhurandhar The Revenge','4. Avengers Doomsday','5. Project Hail Mary',sep='\n')
        mname=input("Please Enter The Name Of The Movie You Want To Watch:")
        if mname.lower()=='backrooms':
            print("Great Pick,This Show Is Airing On The Following Days ~~")
            print('3 June 2026','4 June 2026','6 June 2026','7 June 2026','9 June 2026','11 June 2026',sep='\n')
            mdate=input('Please Enter The Date Suitable For You [DD-MM-YYYY] :')
            print("The Timings Available for the chosen day are :")
            print('08:00 AM','12:00 PM','04:00 PM','07:00 PM','10:30 PM',sep='\t')
            mtime=input('Please enter the time best suited for you[HH:MM AM/PM]:')
            print("The date and time are all set!, Let's get you a seat immediately now...")
            print('Classic Normal [₹260]','CLA Superior [₹310]','Recliner [₹500]',sep='\n')
            stype=input("Please choose your preferred type of seat:")
            L=['A','B','C','D','E','F','G','H','I','J','K','L','M']
            L1=[1,2,3,4,5,6,7,8,9,10,11,12]
            if stype.lower()=='recliner':
                L=['A','B']
                s1=r.choice(L)
                s2=r.choice(L1)
                
                
                
                print("Your Seat Number is ...~~")
                                
        print("To Get Started Please Register With Your Phone Number")
        pno=int(input("Please enter your Phone Number:"))







                  
