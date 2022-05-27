"""TDD metodu - Pamėginti parašyti AsmensKodas klasę bei testą paskutinių 4 asmens kodo simbolių grąžinimui:
Pasirašyti testą (RED -> Fail)
Pasirašyti klasę, kuri grąžina reikšmę (GREEN -> Pass)
Jei reikia, patobulinti, parefactorinti testą (REFACTOR)
PAPILDOMAI - galite tokiu principu parašyti daugiau testų. Pvz. ištestuoti visą kodą, jo ilgį ir t.t
"""

import unittest
from main import PersonalCode

class TestKodas(unittest.TestCase):

    test_code = "38910257458"

    def test_return_last_four_numbers(self):
        self.kodas = PersonalCode(self.test_code)
        self.assertEqual(self.kodas.return_last_4(), self.test_code[-4:])