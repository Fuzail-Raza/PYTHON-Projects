
questions = [["Who holds the record for the highest individual score in Test cricket?", "Sachin Tendulkar", "Brian Lara", "Don Bradman", "Chris Gayle", "Brian Lara"],
             ["Which country won the ICC Cricket World Cup in 2019?",
                 "India", "Australia", "England", "New Zealand", "England"],
             ["Who is the highest run-scorer in the history of One Day Internationals (ODIs)?", "Ricky Ponting",
              "Virat Kohli", "Kumar Sangakkara ", "Sachin Tendulkar", "Sachin Tendulkar"],
             ["In cricket, what is the term used to describe a dismissal in which a batsman is bowled without scoring any runs?",
              "Stumped ", "Run Out", "LBW (Leg Before Wicket) ", "Golden Duck", "Golden Duck"],
             ["Who is the fastest bowler to reach 100 wickets in Test cricket?", "Shane Warne",
              "Muttiah Muralitharan", "Dale Steyn ", "Glenn McGrath", "Dale Steyn"]
             ]
levels=[1000,2000,3000,4000,5000]
# print(questions)


name = input("Enter PLayer Name : ")

print("Welcome ", name, " TO KBC")
win = 0
for i in range(len(questions)):
    print("Question for Rs./",levels[i])
    print(questions[i][0])
    print(f"a {questions[i][1]}       b {questions[i][2]}")
    print(f"c {questions[i][3]}       d {questions[i][4]}")
    while True:
        ans = input("Enter correct option or q to exit: ")
        match ans:
            case 'a':
                ans = 1
                break
            case 'b':
                ans = 2
                break
            case 'c':
                ans = 3
                break
            case 'd':
                ans = 4
                break
            case 'q':
                if(i-1<0):
                    win=0
                else:
                   win= levels[i-1]
                print("Thanks for playing You Won Rs./",win,"-")
                exit()
            case _:
                print("Wrong Option")
    if ans == questions[i].index(questions[i][5]):
          print("Correct Answer")
          win += levels[i]
    else:
        print("Wrong Answer")
        if(i-2<0):
            win=0
        else:
            win=levels[i-2]
        print("Correct answer is : ", questions[i][5])
        break
print("Your Won Rs./ ", win, "-")
