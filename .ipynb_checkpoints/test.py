def compareStudent(grades1, grades2):
    avg1 = sum(grades1)/len(grades1)
    avg2 = sum(grades2)/len(grades2)
    if avg1 > avg2:
        return avg1
    elif avg1 < avg2:
        return avg2
    else:
        return "They have the same grades.."

shoha = [99,34,652,112,21,54]
brandt = [99,324,3,555,5645]

print(f'The highest GPA is {compareStudent(shoha, brandt)}')