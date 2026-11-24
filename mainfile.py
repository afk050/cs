import SQLfile
import mysql.connector as m
SQLfile.createtable()
SQLfile.preset()
def addrec():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIE_BOOKINGS")
        cur=con.cursor()
        print("CURRENTLY POPULAR SHOWS".center(25,'-'))
        cur.execute("SELECT movie_name FROM movies")
        mov = [mv[0].lower() for mv in cur.fetchall()]
        for i in mov:
            print(i)
        while True:
            movie_name=input("Please Enter The Name Of The Movie You Want To Watch:")
            if movie_name.lower() not in mov:
                print("Invalid movie name. Please enter a valid movie name.")
            else:
                break
        cur.execute("SELECT movie_id FROM movies WHERE movie_name='{0}'".format(movie_name))
        movie_id= cur.fetchone()[0]
        cur.execute("select Show_id , show_date, show_time from shows where movie_id={0}".format(movie_id))
        shows = cur.fetchall()
        print("The available shows for the selected movie are as follows:")
        for s in shows:
            print(f"Show ID: {s[0]}, Date: {s[1]}, Time: {s[2]}")
        choice = input("Please enter the Show ID you want to book:")
        cur.execute("SELECT show_date, show_time FROM shows WHERE show_id={0}".format(choice))
        show_date, show_time = cur.fetchone()
        if show_date is None or show_time is None:
            print("Invalid Show ID. Please enter a valid Show ID.")
            return
        else:
            print(f"You have selected the show on {show_date} at {show_time}.")


        print("The date and time are all set!, Let's get you a seat immediately now...")
        cur.execute("SELECT show_id FROM shows WHERE movie_id=(SELECT movie_id FROM movies WHERE movie_name='{0}') AND show_date='{1}' AND show_time='{2}'".format(movie_name, show_date, show_time))
        show_id = cur.fetchone()[0]
        cur.execute("SELECT seat_no FROM bookings WHERE show_id={0}".format(show_id))
        booked_seats = [r[0] for r in cur.fetchall()]
        for i in ['A','B','C','D','E','F','G']:
            for j in range(1,10):
                if str(j)+str(i) not in booked_seats:
                    print(str(j)+str(i),end='    ')
                else:
                    print('X ',end='     ')
            print()
        print()
        print("-" * 80)
        print("ALL EYES THIS WAY".center(80))
        print("Row A -> Recliner Seats","Row B-E -> CLA superior Seats","Row F-G -> CLASSIC Seats",sep='\n') 
        while True:
            seat_no=input("Please Enter The Seat Number You Want To Book:").upper()
            if seat_no.upper() in booked_seats:
                print("This seat is already booked. Please choose another seat.")
            else: 
                if seat_no[1].lower()=="a":
                    print("You Have Chosen A Recliner Seat, The Price For This Seat Is 500/-")
                    seat_type="Recliner"
                    paid_amt=500
                elif seat_no[1].lower() in 'bcde':
                    print("You Have Chosen A CLA Superior Seat, The Price For This Seat Is 300/-")
                    seat_type="CLA Superior"
                    paid_amt=300
                elif seat_no[1].lower() in 'fg':
                    print("You Have Chosen A CLASSIC Seat, The Price For This Seat Is 200/-")
                    seat_type="CLASSIC"
                    paid_amt=200
                break
        
        
        print("To continue, please enter your phone number.")
        phone_no=int(input("Please enter your Phone Number:"))
        print("You have been successfully registered with the phone number:", phone_no)
        name=input("Please Enter Your Name:")
        
        
        print("Thank you for registering, ", name, "! Your booking details are as follows:")
        print("=" * 30)
        print("MOVIE TICKET".center(30))
        print("=" * 30)
        print("Movie:", movie_name)
        print("Date:", show_date)
        print("Time:", show_time)
        print("Seat Number:", seat_no)
        print("Seat Type:", seat_type)
        print("Amount Paid:", paid_amt)
        print("=" * 30)
         
        opt=input("Are all the details entered correct? (yes/no):").strip().lower()
        if opt.lower()=='yes':
            cur.execute("SELECT movie_id FROM movies WHERE movie_name='{0}'".format(movie_name))
            movie_id= cur.fetchone()[0]
            cur.execute("SELECT show_id FROM shows WHERE movie_id={0} AND show_date='{1}' AND show_time='{2}'".format(movie_id, show_date, show_time))
            show_id= cur.fetchone()[0]
            cur.execute("INSERT INTO bookings (show_id, phone_no, seat_no, seat_type, paid_amt) VALUES ({0}, {1}, '{2}', '{3}', {4})".format(show_id, phone_no, seat_no, seat_type, paid_amt))
            con.commit()
            cur.execute("SELECT booking_id FROM bookings WHERE show_id={0} AND phone_no={1} AND seat_no='{2}'".format(show_id, phone_no, seat_no))
            booking_id= cur.fetchone()[0]
            print("Your booking has been successfully completed. Your booking ID is:", booking_id)
            print("THANK YOU FOR BOOKING WITH US!! ENJOY YOUR SHOW.")
        else:
            print("Please restart the booking process to make changes.")

    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def viewbookings():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIE_BOOKINGS")
        cur=con.cursor()
        print("Would you like to view all bookings associated with a specific phone number or a particular booking")
        opt=int(input("Please enter your choice [phone_no(1)/particular(2)]: "))
        if opt == 1:
            p_no=int(input("Please enter your phone number to view bookings: "))
            cur.execute("SELECT b.booking_id, b.show_id, b.phone_no, b.seat_no, b.seat_type, b.paid_amt, s.show_date, s.show_time,m.movie_name FROM bookings b, shows s, movies m where b.show_id = s.show_id and s.movie_id = m.movie_id and b.phone_no={0}".format(p_no))
            T = cur.fetchall()
            if T:
                for j in T:
                    print("-" * 30)
                    print("Booking ID:", j[0])
                    print("Show ID:", j[1])
                    print("Movie Name:", j[8])
                    print("Show Date:", j[6])
                    print("Show Time:", j[7])
                    print("Phone Number:", j[2])
                    print("Seat Number:", j[3])
                    print("Seat Type:", j[4])
                    print("Amount Paid:", j[5])
                    print("-" * 30)
            else:
                print("No bookings found for this phone number.")
        elif opt == 2:
            b_id = int(input("Please enter the booking ID to view details: "))
            cur.execute("SELECT * FROM bookings WHERE booking_id={0}".format(b_id))
            T = cur.fetchone()
            cur.execute('select show_date, show_time from shows where show_id={0}'.format(T[1]))
            show_date, show_time = cur.fetchone()
            cur.execute("select movie_name from movies where movie_id=(select movie_id from shows where show_id={0})".format(T[1]))
            if T:
                print("-" * 30)
                print("Movie Name:",cur.fetchone()[0])
                print("Booking ID:", T[0])
                print("Show ID:", T[1])
                print("Show Date:", show_date)
                print("Show Time:", show_time)
                print("Phone Number:", T[2])
                print("Seat Number:", T[3])
                print("Seat Type:", T[4])
                print("Amount Paid:", T[5])
                print("-" * 30)
            else:
                print("No booking found with this ID.")
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def cancelbooking():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIE_BOOKINGS")
        cur=con.cursor()
        b_id = int(input("Please enter the booking ID you wish to cancel: "))
        cur.execute("SELECT * FROM bookings WHERE booking_id={0}".format(b_id))
        T = cur.fetchone()
        if T:
            cur.execute("DELETE FROM bookings WHERE booking_id={0}".format(b_id))
            con.commit()
            print("Booking canceled successfully.")
        else:
            print("No booking found with this ID.")
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def reschedulebooking():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIE_BOOKINGS")
        cur=con.cursor()
        b_id=int(input("Please enter the booking id you wish to reschedule: "))
        print("Please note that only the seat number can be changed during rescheduling. The movie, date, and time remain the same.") 
        cur.execute("select show_id from bookings where booking_id={0}".format(b_id))
        if cur.fetchone() is None:
            print("No booking found with this ID.")
            return
        show_id = cur.fetchone()[0]
        cur.execute("SELECT seat_no FROM bookings WHERE show_id={0}".format(show_id))
        booked_seats = [r[0] for r in cur.fetchall()]
        for i in ['A','B','C','D','E','F','G']:
            for j in range(1,10):
                if str(j)+str(i) not in booked_seats:
                    print(str(j)+str(i),end='    ')
                else:
                    print('X ',end='     ')
            print()
        print()
        print("-" * 80)
        print("ALL EYES THIS WAY".center(80))
        print("Row A -> Recliner Seats","Row B-E -> CLA superior Seats","Row F-G -> CLASSIC Seats",sep='\n') 
        while True:
            seat_no=input("Please Enter The Seat Number You Want To Book:")
            if seat_no in booked_seats:
                print("This seat is already booked. Please choose another seat.")
            else: 
                if seat_no[1].lower()=="a":
                    print("You Have Chosen A Recliner Seat, The Price For This Seat Is 500/-")
                    seat_type="Recliner"
                    paid_amt=500
                elif seat_no[1].lower() in 'bcde':
                    print("You Have Chosen A CLA Superior Seat, The Price For This Seat Is 300/-")
                    seat_type="CLA Superior"
                    paid_amt=300
                elif seat_no[1].lower() in 'fg':
                    print("You Have Chosen A CLASSIC Seat, The Price For This Seat Is 200/-")
                    seat_type="CLASSIC"
                    paid_amt=200
                break
        print("Booking updated successfully.")
        cur.execute("UPDATE bookings SET seat_no='{0}', seat_type='{1}', paid_amt={2} WHERE booking_id={3}".format(seat_no, seat_type, paid_amt, b_id))
        con.commit()
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def addshow():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIE_BOOKINGS")
        cur=con.cursor()
        movie_name=input("Please Enter The Name Of The Movie You Want To Add:")
        cur.execute("insert ignore into movies (movie_name) values ('{0}')".format(movie_name))
        con.commit()
        show_date=input('Please Enter The Date For The Show [DD-MM-YYYY] :')
        show_time=input('Please enter the time for the show [HH:MM:SS]:')
        cur.execute("SELECT movie_id FROM movies WHERE movie_name='{0}'".format(movie_name))
        if cur.fetchone() is None:
            print("Movie not found. Please add the movie first.")
            return
        movie_id= cur.fetchone()[0]
        cur.execute("INSERT INTO shows (movie_id, show_date, show_time) VALUES ({0}, '{1}', '{2}')".format(movie_id, show_date, show_time))
        con.commit()
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def addmovie():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIE_BOOKINGS")
        cur=con.cursor()
        movie_name=input("Please Enter The Name Of The Movie You Want To Add:")
        cur.execute("INSERT INTO movies (movie_name) VALUES ('{0}')".format(movie_name))
        con.commit()
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

def revenue():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIE_BOOKINGS")
        cur=con.cursor()
        cur.execute("SELECT Sum(paid_amt) FROM bookings")
        t_revenue = cur.fetchone()[0]
        print("Total Revenue:", t_revenue)
    except m.Error:
        print("Connection Error")
    finally:
        con.close()

while True:
    print("Welcome To The Movie Booking System".center(50,'-'))
    print("1.ADMIN","2.USER",sep='\n')
    role=int(input("Please Enter Your Role:"))
    if role==1:
        print("Please Enter Your Admin Credentials To Continue")
        admin_username=input("Please Enter Your Username:")
        admin_password=input("Please Enter Your Password:")
        if admin_username=="admin" and admin_password=="admin":
            print("Login Successful")
            while True:
                print("1. Add A Show","2. Add A Movie","3. View Revenue","4. Exit",sep='\n')
                choice=int(input("Please Enter Your Choice:"))
                if choice==1:
                    addshow()
                elif choice==2:
                    addmovie()
                elif choice==3:
                    revenue()
                elif choice==4:
                    print("Thank You For Using The Movie Booking System")
                    break
                else:
                    print("Invalid Choice, Please Try Again")
    elif role==2:
        while True:
            print("1. Book A Ticket","2. View booking","3. Cancel Booking","4. Reschedule Booking","5. Exit",sep='\n')
            choice=int(input("Please Enter Your Choice:"))
            if choice==1:
                addrec()
            elif choice==2:
                viewbookings()
            elif choice==3:
                cancelbooking()
            elif choice==4:
                reschedulebooking()
            elif choice==5:
                print("Thank You For Using The Movie Booking System")
                break
            else:
                print("Invalid Choice, Please Try Again")
