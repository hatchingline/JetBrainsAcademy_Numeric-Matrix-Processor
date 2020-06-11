score_percentage = int(input()) / int(input()) * 100
if score_percentage < 60:
    print("F")
elif 60 <= score_percentage < 70:
    print("D")
elif 70 <= score_percentage < 80:
    print("C")
elif 80 <= score_percentage < 90:
    print("B")
elif 90 <= score_percentage <= 100:
    print("A")
else:
    pass
