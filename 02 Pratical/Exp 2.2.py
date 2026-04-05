#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
#Exp 2.3 : Enrollment Manager
CET = {"Yuvraj Singh", "Vibhav.M","Shreyas Shigwan", "Manthan singh","shivam singh", "Pratik shri", "Madrid" }
JEE = {"pratik ", "Madrid", "Manthan singh", "Pratik shri"}
NEET = {"Yuvraj Singh", "Manthan singh" ,"shivam singh", "Pratik shri"}

print(f"student in CET: {CET}")
print(f"student in JEE: {JEE}")
print(f"student in NEET: {NEET}")

all_student = CET.union(JEE,NEET)
print(f"\nALL ENROLLED STUDENT's:{all_student}")

common_exam = CET.intersection(JEE,NEET)
print(f"\nSTUDENT's IN ALL EXAMINTATION:{common_exam}")

not_neet = CET.intersection(JEE).difference(NEET)
print(f"\nSTUDENT's WHO APPEAR FOR CET AND JEE ONLY:{not_neet}")

not_JEE = CET.intersection(NEET).difference(JEE)
print(f"\nSTUDENT's WHO APPEAR FOR CET AND NEET ONLY:{not_JEE}")
  
   
    