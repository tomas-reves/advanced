from modules.python_kursas import PythonKursas, Kursas

pitonas = PythonKursas("Python", "Vakaris", 200)
java = Kursas("JAV", "Mantas", 520)

pitonas.destyti()
java.destyti()
print(pitonas, java)