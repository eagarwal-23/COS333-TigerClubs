#!/usr/bin/env python

#-----------------------------------------------------------------------
#   club.py
#   Authors: Eesha Agarwal and
#   Module for functions related to student's own profile page

from sys import argv, stderr, exit
from psycopg2 import connect, sql
from contextlib import closing
from student import Student
import os

# add database details as constants
DB = 'd8hudjmal9i0pc'
USERNAME = 'rvwhfgtoycqubz'
PASSWORD = 'e0cb0aca7c7da7773f28d1905455da0f9bf5e83d1a0b98be573e86a621c168e9'
HOST = 'ec2-23-23-199-57.compute-1.amazonaws.com'
PORT = '5432'

#DB_URL = 'postgres://rvwhfgtoycqubz:e0cb0aca7c7da7773f28d1905455da0f9bf5e83d1a0b98be573e86a621c168e9@ec2-23-23-199-57.compute-1.amazonaws.com:5432/d8hudjmal9i0pc'
#DATABASE_URL = os.environ['DATABASE_URL']
DB_DEFAULT = "postgres://rvwhfgtoycqubz:e0cb0aca7c7da7773f28d1905455da0f9bf5e83d1a0b98be573e86a621c168e9@ec2-23-23-199-57.compute-1.amazonaws.com:5432/d8hudjmal9i0pc"
DB_URL = os.environ.get('DATABASE_URL', DB_DEFAULT)


DB = 'd8hudjmal9i0pc'
USERNAME = 'rvwhfgtoycqubz'
PASSWORD = 'e0cb0aca7c7da7773f28d1905455da0f9bf5e83d1a0b98be573e86a621c168e9'
HOST = 'ec2-23-23-199-57.compute-1.amazonaws.com'
PORT = '5432'

# given netid and password, return corresponding student info from database
# for student profile page
def get_student_infop():
    try:
        conn = connect(database=DB, user=USERNAME, password=PASSWORD, host=HOST, port= PORT)
        cursor = conn.cursor()
            #with closing(connection.cursor()) as cursor:
                
        # get student name, netid, year, major, bio
        all = "SELECT * FROM tigerclubtest.club_info;"
        print(conn.get_dsn_parameters())
        cursor = cursor.execute(all)
        result = cursor.fetchone()
        print("results:", result)
        cursor.close()
        conn.close()
        return result

    except Exception as ex:
        print(ex, file = stderr)
        exit(1)