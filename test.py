from app import db
from models import Student, Club, Tag, Review

from db1 import get_student_ratings, student_search

def club_search(search):
    clubs = None
    search_query = '%' + search + '%'
    clubs = Club.query.filter((Club.name.ilike(search_query) | Club.tags.any(Tag.name.ilike(search_query)))).all()
    for club in clubs:
        print(club)

def add_tag(name):
    tag = Tag(name)
    db.session.add(tag)
    db.session.commit()

if __name__ == "__main__":
    # add_tag('Instruments')
    # add_tag('Movies')
    # add_tag('MCU')
    # add_tag('Baseball')
    # add_tag('Basketball')
    # add_tag('Beachball')
    # add_tag('Sports')
    # add_tag('Bowling')
    # add_tag('Cricket')

    student = Student.query.filter_by(netid = 'eagarwal').first()
    reviews = student.reviews
    for review in reviews:
        print(review)

<<<<<<< HEAD
    club = Club.query.filter_by(clubid = "3").first()
    reviews = club.reviews

    for review in reviews:
        print(review.inclusivity)

    ratings = get_student_ratings("eagarwal")
    print(ratings)
=======
    club = Club.query.filter_by(clubid = 3).first()
    reviews = club.reviews
    for review in reviews:
        print(review.diversity)
        print(review)
>>>>>>> b843059bcfb1144af4b828109a42c96ca1d07ba2

    # search = 'a'
    # student_search('a')
