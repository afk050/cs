import mysql.connector as m
def createdatabase():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234")
        cur=con.cursor()
        cur.execute("create database if not exists MOVIES")
    except m.Error:
        print("Connection Error")
    finally:
        con.close()
def createtable():
    try:
        createdatabase()
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIES")
        cur=con.cursor()
        cur.execute("create table if not exists movies(movie_id int auto_increment primary key ,movie_name varchar(30) not null)")
        cur.execute("create table if not exists shows(show_id int auto_increment primary key ,movie_id int not null,show_date date not null,show_time time not null,foreign key(movie_id) references movies(movie_id), unique key unique_show(movie_id,show_date,show_time))")
        cur.execute("create table if not exists bookings(booking_id int auto_increment primary key ,show_id int not null,phone_no bigint not null,seat_no varchar(3) not null,seat_type varchar(25) not null,paid_amt int not null,foreign key(show_id) references shows(show_id),unique key unique_seat_per_show(seat_no,show_id))")
    except m.Error:
        print("Connection Error")    
    finally:
        con.close()
def preset():
    try:
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIES")
        cur=con.cursor()
        cur.execute("INSERT ignore INTO movies (movie_name) VALUES ('Avengers: Endgame'),('colony'),('The Dark Knight'),('Inception'),('Interstellar')")
        con.commit()
        timings=['10:00','13:00','16:00','19:00','22:00']
        date='2026-10-'
        for i in range(1, 6):
            for movie in ['Avengers: Endgame','colony','The Dark Knight','Inception','Interstellar']:
                cur.execute("SELECT movie_id FROM movies WHERE movie_name='{0}'".format(movie))
                movie_id= cur.fetchone()[0]
                newdate=date+str(i)
                for j in timings:
                    cur.execute("INSERT ignore INTO shows (movie_id, show_date, show_time) VALUES ({0}, '{1}', '{2}')".format(movie_id, newdate, j))
        con.commit()
    except m.Error:
        print("Connection Error")
    finally:
        con.close()