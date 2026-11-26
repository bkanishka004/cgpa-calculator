
def calculate_cgpa(grade_points, credits):
    return sum(grade_points) / len(grade_points)


if __name__ == "__main__":
    grades = [9, 8, 10, 7, 8]
    credits = [4, 3, 4, 2, 3]

    cgpa = calculate_cgpa(grades, credits)
    print(f"Your CGPA is: {cgpa}")
