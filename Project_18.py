# 18. Treasure Island Programme

print("Welcome To Treasure Island.")
print("Your Mission Is The Find The Treasure")
Choice1 = input('You\'re at crossroad, Where Do You Want To Go?'
                'Type "Left" Or "Right".\n').lower()

if Choice1 == "left":
    Choice2 = input('You\'ve Come To a Lake.'
                    'There Is An Island In The Middle Of The Lake. '
                    'Type "Wait" To Wait For a Boat. '
                    'Type "Swim" To Swim Across.\n').lower()
    if Choice2 == "wait":
        Choice3 = input("You Arrive At The Island Unharmed. "
                        "There Is House With 3 Doors. One Red, "
                        "One Yellow And One Blue. "
                        "Which Colour Do You Choose?\n").lower()
        if Choice3 == "red":
            print("It's a Room Full Of Fire. Game Over")
        elif Choice3 == "yellow":
            print("You Found The Treasure. You Win!")
        elif Choice3 == "Blue":
            print("You Enter a Room Of Beasts. Game Over.")
        else:
            print("You Choose a Door That Doesn't Exist. Game Over.")
    else:
        print("You Got Attacked By An Angry Trout. Game Over.")
else:
    print("You Fell In a Hole. Game Over.")



        
                
        

