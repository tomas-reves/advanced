from typing import Sequence
from db_init import *

def add_worker(name, surname, position):
    session.add(name, surname, position)
    session.commit()


def set_mentor(mentor_id: int, student_id: int):
    pass


def get_mentor_info(mentor_name, mentor_surname) -> Sequence[dict]:
    # Issitraukti is duomenu bazes ir uzpildyti
    return [{
        'mentor_name': mentor_name,
        'mentor_surname': mentor_surname,
        'student_name': student_name,
        'student_surname': student_surname,
        'student_position': student_position
    }]
