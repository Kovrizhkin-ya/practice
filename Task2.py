mark = int(input("Enter your mark"))
if mark < 0 or mark > 100:
  print("Wrong date")
elif mark < 60:
  print("Unsatisfactory")
elif 60 <= mark <= 64:
  print("Marginal")
elif 65 <= mark <= 74:
  print("Satisfactory")
elif 75 <= mark <= 84:
  print("Good")
elif 85 <= mark <= 94:
  print("Very good")
else:
  print("Excellent")