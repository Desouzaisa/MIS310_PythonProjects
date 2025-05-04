#Calculate the weighted average
#Based on Average Course Grade Program

def calc_average(tests, quizzes, midterm, project, final_exam, homework):
    #Calculate average of tests and quizzes
    test_avg = sum(tests) / len(tests)
    quiz_avg = sum(quizzes) / len(quizzes)

    #Apply the weights
    average = ((test_avg * 0.20) + (quiz_avg * 0.20) + (midterm * 0.15) + (project * 0.20) +
        (final_exam * 0.15) + (homework * 0.10))
    return average

#Return a letter grade based on the score
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#Main program
def main():
    print("Enter your grades for the following:")

    #Get test scores
    tests = []
    for i in range(2):
        score = float(input(f"Test {i+1} score: "))
        tests.append(score)

    #Get quiz scores
    quizzes = []
    for i in range(4):
        score = float(input(f"Quiz {i+1} score: "))
        quizzes.append(score)

    #Get single scores
    midterm = float(input("Midterm exam score: "))
    project = float(input("Project score: "))
    final_exam = float(input("Final exam score: "))
    homework = float(input("Homework average: "))

    #Calculate final average
    average = calc_average(tests, quizzes, midterm, project, final_exam, homework)
    grade = determine_grade(average)

    # Show results
    print("\n====== Final Results ======")
    print(f"Final Weighted Average: {average:.2f}")
    print(f"Final Letter Grade: {grade}")

#Run the program
main()
