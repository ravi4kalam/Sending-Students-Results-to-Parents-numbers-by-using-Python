import matplotlib.pyplot as plt
def student_info():
    names=eval(input(" ENTER STUDENT NAMES "))
    print(names)
    percentage=eval(input(" ENTER STUDENTS PERCENTAGE "))
    print(percentage)
    plt.xlabel("STUDENT NAMES ")
    plt.ylabel("STUDENT PERCENTAGE ")
    plt.xlim(xmin=0,xmax=len(names))
    plt.ylim(ymin=0,ymax=100)
    plt.plot(names,percentage)

    plt.grid=(True)
    # plt.show()
    plt.bar(names,percentage)
    plt.title("STUDENT PERCENTAGE GRAPH ")
    plt.show()
s=student_info()




