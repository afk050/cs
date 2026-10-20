import SQLfile
import mysql.connector as m
SQLfile.createtable()
def addrec():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIES")
        cur=con.cursor()
        print("CURRENTLY POPULAR SHOWS".center(25,'-'))
        cur.execute("SELECT movie_name FROM movies")
        mov = [mv[0] for mv in cur.fetchall()]
        for i in mov:
            print(i)
        movie_name=input("Please Enter The Name Of The Movie You Want To Watch:")


        print("Great Pick,This Show Is Airing On The Following Days ~~")
        print('3 June 2026','4 June 2026','6 June 2026','7 June 2026','9 June 2026','11 June 2026',sep='\n')
        show_date=input('Please Enter The Date Suitable For You [DD-MM-YYYY] :')
        
        
        print("The Timings Available for the chosen day are :")
        print('08:00 AM','12:00 PM','04:00 PM','07:00 PM','10:30 PM',sep='\t')
        show_time=input('Please enter the time best suited for you[HH:MM AM/PM]:')
        
        
        print("The date and time are all set!, Let's get you a seat immediately now...")
        L=['A','B','C','D','E','F','G']
        cur.execute("SELECT seat_no FROM bookings")
        booked_seats = [r[0] for r in cur.fetchall()]
        for i in L:
            for j in range(1,11):
                if j+str(i) not in booked_seats:
                    print(j+str(i),end='      ')
                else:
                    print('X ',end='      ')
            print()
        print()
        print("---------------------------------------------------------------------------------------")
        print("ALL EYES THIS WAY".center(80))
        print("Row A -> Recliner Seats","Row B-E -> CLA superior Seats","Row F-G -> CLASSIC Seats",sep='\n') 
        seat_no=input("Please Enter The Seat Number You Want To Book:")
        if seat_no[0].lower()=="a":
            print("You Have Chosen A Recliner Seat, The Price For This Seat Is 500/-")
            seat_type="Recliner"
            paid_amt=500
        elif seat_no[0].lower() in 'bcde':
            print("You Have Chosen A CLA Superior Seat, The Price For This Seat Is 300/-")
            seat_type="CLA Superior"
            paid_amt=300
        elif seat_no[0].lower() in 'fg':
            print("You Have Chosen A CLASSIC Seat, The Price For This Seat Is 200/-")
            seat_type="CLASSIC"
            paid_amt=200
        else:
            print("Invalid Seat Number")
        
        
        print("To continue, please register with your phone number.")
        phone_no=int(input("Please enter your Phone Number:"))
        print("You have been successfully registered with the phone number:", phone_no)
        name=input("Please Enter Your Name:")
        
        
        print("Thank you for registering, ", name, "! Your booking details are as follows:")
        print("Movie:", movie_name)
        print("Date:", show_date)
        print("Time:", show_time)
        print("Seat Number:", seat_no)
        print("Seat Type:", seat_type)
        print("Amount Paid:", paid_amt)
         
        opt=input("Are all the details entered correct? (yes/no)")
        if opt.lower()=='yes':
            cur.execute("SELECT movie_id FROM movies WHERE movie_name='{0}'".format(movie_name))
            movie_id= cur.fetchone()[0]
            cur.execute("SELECT show_id FROM shows WHERE movie_id={0} AND show_date='{1}' AND show_time='{2}'".format(movie_id, show_date, show_time))
            show_id= cur.fetchone()[0]
            cur.execute("INSERT INTO bookings (show_id, phone_no, seat_no, seat_type, paid_amt) VALUES ({0}, {1}, '{2}', '{3}', {4})".format(show_id, phone_no, seat_no, seat_type, paid_amt))
            con.commit()
        else:
            print("Please restart the booking process to make changes.")

        
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def addshow():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIES")
        cur=con.cursor()
        movie_name=input("Please Enter The Name Of The Movie You Want To Add:")
        show_date=input('Please Enter The Date For The Show [DD-MM-YYYY] :')
        show_time=input('Please enter the time for the show [HH:MM AM/PM]:')
        cur.execute("SELECT movie_id FROM movies WHERE movie_name='{0}'".format(movie_name))
        movie_id= cur.fetchone()[0]
        cur.execute("INSERT INTO shows (movie_id, show_date, show_time) VALUES ({0}, '{1}', '{2}')".format(movie_id, show_date, show_time))
        con.commit()
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def addmovie():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIES")
        cur=con.cursor()
        movie_name=input("Please Enter The Name Of The Movie You Want To Add:")
        cur.execute("INSERT INTO movies (movie_name) VALUES ('{0}')".format(movie_name))
        con.commit()
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

while True:
    print("Welcome To The Movie Booking System".center(50,'-'))
    print("1. Book A Ticket","2. Add A Show","3. Add A Movie","4. Exit",sep='\n')
    choice=int(input("Please Enter Your Choice:"))
    if choice==1:
        addrec()
    elif choice==2:
        addshow()
    elif choice==3:
        addmovie()
    elif choice==4:
        print("Thank You For Using The Movie Booking System")
        break
    else:
        print("Invalid Choice, Please Try Again")
