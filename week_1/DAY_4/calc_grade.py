student = {}

number_of_subjects = int(input("Enter the number of subjects: "))
for i in range(number_of_subjects):
    subject = input("Enter the subject name: ")
    score = int(input("Enter the score for {}: "))
    student[subject] = score

print(student)
total = sum(student.values())
average = total /len(student)
print(f"total score: {total}")
print(f"average score: {average}")