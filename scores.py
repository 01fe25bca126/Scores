scores=[]
print("Enter 4 scores:")
for i in range(4):
  s=int (input(f"Scores {i+1}: "))
  scores.append(s)
total=sum(scores)
average=total/4
largest=max(scores)
smallest=min(scores)
print("\nScores:",scores)
print("Total:",total)
print("Average:",average)
print("largest:",largest)
print("smallest:",smallest)
