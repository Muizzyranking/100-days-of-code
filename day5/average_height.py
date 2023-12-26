student_heights = input("Input a list of student heights ").split()
total = 0
lenght = 0
for heights in student_heights:
    total += int(heights)
    lenght += 1

avg = round(total / lenght)

print(avg)
