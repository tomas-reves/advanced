import os
from os.path import exists

import pytest

from db_init import Base
from mentor_program import add_worker, set_mentor, get_mentor_info

@pytest.fixture(autouse=True)
def add_workers():
    if exists("./darbuotojas2.db"):
        os.remove("./darbuotojas2.db")
    Base.metadata.create_all(engine)
    add_worker("Vakaris", "Pavardenis", "Destytojas")
    add_worker("Remigijus", "Vardenis", "Studentas")
    add_worker("Kastytis", "Eglinskas", "Koordinatorius")


def test_get_mentor_info__one_student():
    set_mentor(1, 2)
    set_mentor(3, 1)

    result = [{
        'mentor_name': "Vakaris",
        'mentor_surname': "Pavardenis",
        'student_name': "Remigijus",
        'student_surname': "Vardenis",
        'student_position': "Studentas"
    }]

    assert get_mentor_info("Vakaris", "Pavardenis") == result


def test_get_mentor_info__multiple_students():
    set_mentor(1, 2)
    set_mentor(1, 3)

    result = [{
        'mentor_name': "Vakaris",
        'mentor_surname': "Pavardenis",
        'student_name': "Remigijus",
        'student_surname': "Vardenis",
        'student_position': "Studentas"
    }, {
        'mentor_name': "Vakaris",
        'mentor_surname': "Pavardenis",
        'student_name': "Kastytis",
        'student_surname': "Eglinskas",
        'student_position': "Koordinatorius"
    }]

    assert get_mentor_info("Vakaris", "Pavardenis") == result
