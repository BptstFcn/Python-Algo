"""
        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

# Computes the number of shelfs the cat needs to jump on, from start to finish
def cat_tree(start: int, finish: int) -> int:
    # Simple check so everything should be good
    if finish <= start:
        return 0

    shelf_count: int = 0        # As we begin on a shelf, should we count from 1 ?
    diff: int = finish - start  # Difference between start and finish

    # In order to find the quickest path, we want our difference to be a multiple of 3 so the cat can jump 3 by 3
    # As long as the difference is not a multiple of 3, we jump 1 by 1
    while diff % 3 != 0:
        diff -= 1
        shelf_count += 1

    # Once we do get a multiple of 3, then we can make the cat jump as fast as possible
    shelf_count += diff // 3 # Optimization made for this case
    
    # while diff > 1:
    #    diff -= 3
    #    shelf_count += 1

    return shelf_count

# Returns the path taken by the cat in order to go to its favorite shelf
def cat_tree_path(start: int, finish: int) -> list[int]:
    path: list[int] = [start]   # We always begin at start so it's worth putting it here
    diff: int = finish - start  # Difference between start and finish
    shelf_number: int = start   # Number of the shelf on which the cat is

    # In order to find the quickest path, we want our difference to be a multiple of 3 so the cat can jump 3 by 3
    # As long as the difference is not a multiple of 3, we jump 1 by 1
    while diff % 3 != 0:
        shelf_number += 1
        diff -= 1
        path.append(shelf_number) # Here we add the actual shelf number

    # Once we do get a multiple of 3, then we can make the cat jump as fast as possible
    while diff > 1:
        shelf_number += 3
        diff -= 3
        path.append(shelf_number)

    return path

# Programs main function, this is where it all begins :)
if __name__ == '__main__':
    solution = catTree(1, 18)
    print(solution)
    solution2 = catTreePath(1, 48)
    print(solution2)
