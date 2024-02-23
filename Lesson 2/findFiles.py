# \t » tabulator
# \n » newline
# \r » carriage return

# A for ciklus 0-tól 100-ig halad 10-es lépésekkel, és minden iterációban kiírja a "progress {x}%" szöveget, ahol az {x} helyére az aktuális iteráció értéke kerül. Az end='\r' paraméter azt jelenti, hogy a következő kiírás helyett a kurzor visszalép a sor elejére, így az üzenet helyben frissül, és nem halmozódnak fel az üzenetek. A flush=True paraméter biztosítja, hogy az üzenetek azonnal megjelenjenek a konzolon, anélkül, hogy várnánk a standard output buffer kiürülésére. 

# for x in range(0, 100, 10):
#     print(f"progress {x}%", end='\r', flush=True)
#     time.sleep(0.3)

import time
import sys


fruits = ['apple', 'orange', 'cherry', 'strawberry']

# Az összes elemet kiextraktálja
print(fruits)

# 'Apple' után az összes elemet kiextraktálja
print(fruits[1:])

# 'Orange' és 'Strawberry' közti elemeket extraktálja ki.
print(fruits[2:3])

sys.exit()

if len(sys.argv) != 3:
    print('Invalid arguments! Usage: findFiles.py [serch wildcard] [target directory]')
    sys.exit(1)

print(f'Args num {len(sys.argv)}')
print(f'Args {sys.argv[1:]}')