questions = [
  ["1. who created python?",
   ["A. james gosling","B. guido van rossum","C. dennis ritchie","D. bjarne stroustrup"],"B"],

   ["2. which language is used for web development?",
   ["A. java","B. python","C. c++","D. javascript"],"D"],

  ["3. which language is used for machine learning?",
   ["A. java","B. python","C. c++","D. javascript"],"B"],

   ["4. which language is used for data science?",
   ["A. java","B. python","C. c++","D. javascript"],"B"],

   ["5. which language is used for game development?",
   ["A. java","B. python","C. c++","D. javascript"],"C"],

   ["6. which language is used for web scraping?",
   ["A. java","B. C++","C. python","D. javascript"],"C"],

   ["7. which language is used for data analysis?",
   ["A. java","B. python","C. c++","D. javascript"],"B"],

   ["8. which language is used for data visualization?",
   ["A. python","B. java","C. c++","D. javascript"],"A"],

   ["9. which language is used for data mining?",
   ["A. java","B. python","C. c++","D. javascript"],"B"],

   ["10. which language is used for data engineering?",
   ["A. java","B. javascript","C. c++","D. python"],"D"],
]
prizes=[1000,2000,5000,10000,20000,40000,80000,160000,320000,640000]


print("="*60)
print("📍          WELCOME TO KAUN BANEGA CROREPATI         📍")
print()
print("     Answer All Questions Correctly to Win the Game     ")
print()
print("                 Let's Begin the Game        ")
print("-"*60)


money_won = 0
score= 0
for question in questions:
   print("\n\n"+question[0])
   print()
   for option in question[1]:
     print(option)
   print()
   answer = input("Enter Your Answer : ").upper()
   if answer== question[2]:
      money_won = prizes[score]
      print("✅Correct Answer!")
      print(f"💰You Won ₹{money_won}")
      score += 1
   else:
      print("❌Wrong Answer!")
      print("💀Game Over!")
      print(f"💰You Take Home ₹{money_won}")
      break
if score == len(questions):
  print("\n")
  print("\n🏆 CONGRATULATIONS! YOU WON THE GAME!")
  print(f"💰Total Prize Money: ₹{money_won}")
  print("="*60)
