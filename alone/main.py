import forest
import cave
gameWon = False
forestExitCave = False
while not gameWon:
    if forest.inForest:
        if not forestExitCave:
            forest.forestBeginning()
        elif forestExitCave:
            forest.forestDarkEast()
    elif cave.inCave:
        forestExitCave = True
        forest.inRoomDarkEast = True
        cave.caveEntrance()
