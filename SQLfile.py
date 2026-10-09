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
        create_database()
        con=m.connect(host="localhost",user="root",passwd="1234",database="MOVIES")
        cur=con.cursor()
        cur.execute("create table if not exists Backrooms(Booking_id int auto increment primary key,Phone_No bigint not null,Name varchar(25),Seat_no varchar(3),Seat_Type varchar(25),Paid_amt int,Date_of_show date,Start_Time time,unique key unique_seat_per_show(seat_no,date_of_show,start_time));")
        cur.execute("create table if not exists Colony(Booking_id int auto increment primary key,Phone_No bigint not null,Name varchar(25),Seat_no varchar(3) ,Seat_Type varchar(25),Paid_amt int,Date_of_show date,Start_Time time,unique key unique_seat_per_show(seat_no,date_of_show,start_time));")
        cur.execute("create table if not exists Dhurandhar_The_Revenge(Booking_id int auto increment primary key,Phone_No bigint not null,Name varchar(25),Seat_no varchar(3),Seat_Type varchar(25),Paid_amt int,Date_of_show date,Start_Time time,unique key unique_seat_per_show(seat_no,date_of_show,start_time));")
        cur.execute("create table if not exists Avengers_Doomsday(Booking_id int auto increment primary key,Phone_No bigint not null,Name varchar(25),Seat_no varchar(3),Seat_Type varchar(25),Paid_amt int,Date_of_show date,Start_Time time,unique key unique_seat_per_show(seat_no,date_of_show,start_time));")
        cur.execute("create table if not exists Project_Hail_Mary(Booking_id int auto increment primary key,Phone_No bigint not null,Name varchar(25),Seat_no varchar(3),Seat_Type varchar(25),Paid_amt int,Date_of_show date,Start_Time time,unique key unique_seat_per_show(seat_no,date_of_show,start_time));")
    except m.Error:
        print("Connection Error")
    finally:
        con.close()
