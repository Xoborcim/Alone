#Sarim
import datetime
minutes_used = 0


def get_elapsed_time_minutes():
    global start_time

    current_time = datetime.datetime.now()
    elapsed_time = datetime.datetime(1,5,1) + abs(start_time - current_time)
    return elapsed_time.minute


def another_location_in_story():
    global minutes_used
    max_time_limit = 15

    minutes_used = get_elapsed_time_minutes()
    if minutes_used > max_time_limit:
        print(f'Time is up! It has been {minutes_used} minutes since you started. Your time has run out')

def end_game():
    print("You have lost the game")
    print("Would you like to play again")

#Sarim
def hunger_system():
    hunger_meter = 3
    while hunger_meter > 0:
        if minutes_used == 4,8,12:
            hunger_meter - 1
            print(f'Your hunger has decreased to {hunger_meter}')
            print('eat to increase your hunger meter')
    if hunger_meter == 0:
        print("You have died of hunger")
        end_game()


