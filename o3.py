def sum_avg(marks):
    total = sum(marks)
    average = total/len(marks)
    return total,average

marks = [84,75,79,99,97]
total,average=sum_avg(marks)
print(f"total marks:{total}")
print(f"average marks:{average}")           
