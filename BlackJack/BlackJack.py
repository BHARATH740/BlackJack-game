import random
from art import logo

print(logo)
cards = [11,2,3,4,5,6,7,8,9,10]

You =[random.choice(cards), random.choice(cards)]
Dealer =[random.choice(cards), random.choice(cards)]
current_score = sum(You)

print(f"Your cards : [{You[0]}, {You[1]}], current score: {current_score}")
print(f"Computer's first card: {Dealer[0]}")

is_new_card= input("Type 'y' to get another card, type 'n' to pass: ")
if is_new_card == "y":
    You.append(random.choice(cards))
    current_score = sum(You)
    print(f"Your cards : [{You[0]}, {You[1]}, {You[2]}], current score: {current_score}")
    print(f"Computer's first card: {Dealer[0]}")

final_score1 = sum(You)
final_score2 = sum(Dealer)
if is_new_card == "y":
    print(f"Your final hand : [{You[0]}, {You[1]}, {You[2]}], final score: {final_score1}")
    print(f"Computer's final hand: [{Dealer[0]}, {Dealer[1]}] ,final score: {final_score2}")
elif is_new_card == "n" :
    print(f"Your final hand : [{You[0]}, {You[1]}], final score: {final_score1}")
    print(f"Computer's final hand: {Dealer[0]}, {Dealer[1]} ,final score: {final_score2}")

if final_score1 > 21 :
    print("You went over. You lose")
elif final_score1 <21 :
    if final_score1 < final_score2 :
        if final_score2 < 16 :
            Dealer.append(random.choice(cards))
            print("Computer's final score is below 16, so it took another card.")
            final_score1 = sum(You)
            final_score2 = sum(Dealer)
            print(f"Your final hand : [{You[0]}, {You[1]}, {You[2]}], final score: {final_score1}")
            print(f"Computer's final hand: {Dealer[0]}, {Dealer[1]}, {Dealer[2]} ,final score: {final_score2}")
            if final_score1 < final_score2 <= 21:
                print("You lose, as computer's final score is nearest to 21")
            elif final_score2 < final_score1 <= 21:
                print("Hurray!!You win.")
        else:
            print("You lose, as computer's final score is nearest to 21")
            
    elif final_score2 < final_score1:
        print("Hurray!!You win.")
elif final_score1 == 21:
        print("Hurray!!You win.It's a BlackJack")
elif final_score1 == final_score2:
    print("It is a DRAW!!")

    





input()