#!/usr/bin/env python

#-----------------------------------------------------------------------
#   club.py
#   Authors: Eesha Agarwal and
#   Module for functions related to student's own profile page

from sys import argv, stderr, exit
from psycopg2 import connect
from contextlib import closing
from student import Student

# connecting to postgresql db
conn = connect("")    

# given netid and password, return corresponding Student from database
def get_student_info(netid):
    try:
        with connect(database=DB, user=USERNAME, password=PASSWORD, host=HOST, port= PORT):
            with closing(connection.cursor()) as cursor:
                
                # get student name, netid, year, major, bio
                cursor = cursor.execute(get_student_info_query(), [netid])
                student_info = cursor.fetchone()

                # get students clubs
                clubs = []
                cursor = cursor.execute(get_student_clubs_query(), [netid])
                row = cursor.fetchone()

                while row is not None:
                    club = club[0]
                    if club not in clubs:
                        clubs.append(club)
                    row = cursor.fetchone()

                # get students tags (interests)
                tags = []
                cursor = cursor.execute(get_student_tags_query(), [netid])
                row = cursor.fetchone()

                while row is not None:
                    tag = tag[0]
                    if tag not in tags:
                        tags.append(tag)
                    row = cursor.fetchone()

                student_profile = Student(student_info[0], student_info[1],
                                        student_info[2], student_info[3],
                                        student_info[4], clubs, tags, student_info[5])

                return student_profile

    except Exception as ex:
        print(ex, file = stderr)
        exit(1)

# query to get student ingo
def get_student_info_query():
    stmt_str = "SELECT netid, name, res_college, year, major, bio "
    stmt_str += "FROM student_info "
    stmt_str += "WHERE netid = ?"

    return stmt_str

# query to get student's clubs
def get_student_clubs_query():
    stmt_str = "SELECT club_info.name, clubid "
    stmt_str += "FROM club_info, students_clubs "
    stmt_str += "WHERE students_clubs.clubid = club_info.clubid "
    stmt_str += "AND student_clubs.netid = ? "
    stmt_str += "ORDER BY club_info.name"

    return stmt_str

def get_student_tags_query():
    stmt_str = "SELECT tag_info.name, tagid "
    stmt_str += "FROM tag_info, students_tags "
    stmt_str += "WHERE students_tags.tagid = tag_info.tagid "
    stmt_str += "AND student_tags.netid = ? "
    stmt_str += "ORDER BY tag_info.name"

    return stmt_str

