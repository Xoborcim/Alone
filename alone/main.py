import forest
import threading

import resourceManagement

threading.Thread(target=forest.forestBeginning()).start()
threading.Thread(target=resourceManagement.timeTracker())
