# Cristina Monterroso
import csv


def get_students():
    students = []
    headers = []

    with open(
        "Phyton\9_de_junio\ej2_calificaciones.csv", "r", encoding="utf-8"
    ) as file:
        studens_rows = csv.reader(file, delimiter="\n")

        for i, row in enumerate(studens_rows):
            row_str = row[0]
            if i == 0:
                headers = row_str.lower().split(";")
            else:
                student = row_str.split(";")
                students.append(dict(zip(headers, student)))
    students = sorted(students, key=lambda x: x["apellidos"])
    # devuelve lista de diccionarios ordenados por apellidos
    print(students)
    return students


def calculate_final_grade(students):
    for student in students:
        student["parcial1"] = float(student["parcial1"].replace(",", "."))
        student["parcial2"] = float(student["parcial2"].replace(",", "."))

        practicas = student["practicas"]
        student["practicas"] = float(practicas.replace(",", ".") if practicas else 0)

        student["nota_final"] = round(
            student["parcial1"] * 0.3
            + student["parcial2"] * 0.3
            + student["practicas"] * 0.4,
            2,
        )


def get_results(students):
    passed = []
    failed = []

    # HEX GREEN = '\x1b[32m{}\x1b[0m'  RED = '\x1b[31m{}\x1b[0m'
    green = "\033[1;32m{}\u001b[0m"
    red = "\033[1;31m{}\u001b[0m"

    for student in students:
        student_fullname = f"{student['apellidos']} {student['nombre']}"
        # student['parcial1'] < 4 or student['parcial2'] < 4

        # '75%' = ['7','5','%']
        if int(student["asistencia"][:-1]) < 75 or student["nota_final"] < 5:
            failed.append(student_fullname)
            student["nota_final"] = red.format(student["nota_final"])
            student["resultado"] = "\u001b[41m\u001b[30m\u001b[1mSuspendido\u001b[0m"
        else:
            passed.append(student_fullname)
            student["nota_final"] = green.format(student["nota_final"])
            student["resultado"] = "\u001b[42m\u001b[30m\u001b[1mAprobado\u001b[0m"

    return passed, failed


def print_table(students):
    print(
        f'{"Nombre del alumno":<28}\tAsistencia\tParcial 1\tParcial 2\tPrácticas\tNota final'
    )
    print("-" * 110)
    for student in students:
        print(
            "{apellidos:<20} {nombre:<12}\t{asistencia:<10}\t{parcial1:<9}\t{parcial2:<9}\t{practicas:<9}\t{nota_final:<10}\t{resultado}".format(
                **student
            )
        )
    print()


def main():
    students = get_students()
    calculate_final_grade(students)
    passed, failed = get_results(students)

    print_table(students)
    print(f"Lista de aprobados: {passed}")
    print(f"Lista de suspendidos: {failed}")


if __name__ == "__main__":
    main()
