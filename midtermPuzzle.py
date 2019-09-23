#Sarkis Mikaelian - Math 482 - Instant Insanity
#CODE:
import math as math
from itertools import combinations

def cubes_generator(colors):
    cubes = []
    cube = []
    pair = []
    for i in range(180):
        pair.append(colors[i])
        if (i + 1) % 2 == 0:
            cube.append(pair)
            pair = []
        if (i + 1) % 6 == 0:
            cubes.append(cube)
            cube = []
    return cubes

def solve_stack(cubes, visited, solution_num):
    i = 0
    multiplicity = [0 for i in range(30)]
    half_sol_flag = False
    half_sol_counter = 0
    while -1 < i < len(cubes):
        moving_forward = True
        next_half_solution = False
        for j in range(3):

            # This stops the dfs at the third thread
            if i == 0 and solution_num == 1 and j == 2:
                half_sol_flag = False
                moving_forward = False
                break

            if half_sol_flag == False and i == (len(cubes) - 1) and visited[i][j] == solution_num:
                if j < 2:
                    visited[i][j] = 0
                    multiplicity[cubes[i][j][0]-1] -= 1
                    multiplicity[cubes[i][j][1]-1] -= 1
                    j += 1
                else:
                    visited[i][j] = 0
                    multiplicity[cubes[i][j][0]-1] -= 1
                    multiplicity[cubes[i][j][1]-1] -= 1
                    next_half_solution = True

            if next_half_solution:
                break

            if visited[i][j] == 0 and multiplicity[cubes[i][j][0] - 1] + 1 < 3 and multiplicity[cubes[i][j][1] - 1] + 1 < 3:
                visited[i][j] = solution_num
                multiplicity[cubes[i][j][0] - 1] += 1
                multiplicity[cubes[i][j][1] - 1] += 1
                moving_forward = False
                i += 1
                break

        if moving_forward:
            i = i - 1
            done_backtracking = False
            while not done_backtracking and i >= 0:
                for k in range(3):
                    if visited[i][k] == solution_num:
                        visited[i][k] = 0
                        multiplicity[cubes[i][k][0] - 1] -= 1
                        multiplicity[cubes[i][k][1] - 1] -= 1
                        k = k + 1
                        while k < 3:
                            if visited[i][k] == 0 and (multiplicity[cubes[i][k][0] - 1] + 1) < 3 and (multiplicity[cubes[i][k][1] - 1] + 1) < 3:
                                visited[i][k] = solution_num
                                multiplicity[cubes[i][k][0] - 1] += 1
                                multiplicity[cubes[i][k][1] - 1] += 1
                                done_backtracking = True
                                i += 1
                                break
                            k = k + 1
                        break
                if not done_backtracking:
                    i = i - 1
        if i == len(cubes):
            half_sol_flag = True

        if i == len(cubes) and solution_num != 2:
            half_sol_counter += 1
            #print("First Half Solution")
            #for t in range(len(visited)):
                #print(visited[t])
            half_sol_flag = solve_stack(cubes, visited, 2)

            if not half_sol_flag:
                i -= 1

    if i == -1 :
        half_sol_flag = False

    return half_sol_flag

def find_min_obs(cubes):

    min_obs = len(cubes) + 1
    i = len(cubes)

    while i > 0:
        solution = False
        subsets = combinations(cubes, i)

        for subset in subsets:
            visited = [[0, 0, 0] for i in range(len(subset))]
            solution = solve_stack(subset, visited, 1)
            if not solution:
                print("A 'No Solution' was found in a stack of ", i ," cubes!")
                print("Minimum obstacle is now: ", min_obs -1)
                min_obs -= 1
                for element in subset:
                    print(element)
                break
            else:
                print("A Solution Was Found")

        if solution:
            print("Every subset of ", i , " cubes had a solution")
            print("Minimum Obstacle: ", min_obs)
            if min_obs > len(cubes):
                print("No Minimal Obstacle.")
            break
        i -= 1


#A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8

midtermPuzzle=  [[[1,5],[1,2],[1,1]],
				[[1,2],[3,4],[5,5]],
				[[1,3],[3,4],[5,5]],
				[[2,5],[6,7],[7,7]],
				[[1,7],[1,2],[4,8]],
				[[5,5],[7,8],[3,4]],
				[[7,8],[2,3],[4,8]],
				[[4,8],[1,5],[4,8]]]

find_min_obs(midtermPuzzle)