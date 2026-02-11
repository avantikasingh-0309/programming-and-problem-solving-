m1,m2,m3,m4=map(int,input().split())
tot=m1+m2+m3+m4
print(tot)
a=tot/4
print(f"{a:.2f}")
if a>75:
	print("Distinction\n")
elif(a>=60 and a<75):
	print("First Division\n")
elif(a>=50 and a<60):
	print("Second Division\n")

elif(a>=40 and a<50):
	print("Third Division\n")

else:
	print("Fail")
