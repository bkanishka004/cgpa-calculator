
def calculate_cgpa(grade_points, credits):
    total_weighted_points = sum(
        grade * credit for grade, credit in zip(grade_points, credits)
    )
    total_credits = sum(credits)

    return total_weighted_points / total_credits


if __name__ == "__main__":
    grades = [9, 8, 10, 7, 8]
    credits = [4, 3, 4, 2, 3]

    cgpa = calculate_cgpa(grades, credits)
    print(f"Your weighted CGPA is: {cgpa:.2f}")
