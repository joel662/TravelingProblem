def main():    
    #Data Loading   
    routes = {}
    transistions = 0
    with open("input.txt","r") as file:
        
        file.readline()     #skips the comment
        startGoal = file.readline().strip()

        endGoal = file.readline().split(" ")
        endGoal[len(endGoal)-1] = endGoal[len(endGoal)-1].strip()
        
        lines = file.readlines()  #lines contains all remaining lines
        for a in lines:
            l = a.split(" ")
            start = l[0].split(":")[0]    
            for i in range(1,len(l)):
                temp = l[i].split(",")
                place = temp[0]
                cost = float(temp[1])
                #appends all connections with place and cost
                #increases each transistion
                if start in routes:
                    routes[start].append((place,cost))
                    transistions += 1
                else:
                    routes[start] = [(place,cost)]
                    transistions += 1
    #printing the result of data loading
    print("Data Loading")
    print("Start State:" + startGoal)
    print("End State(s):" , end = "")
    print(endGoal)
    print("State Space:", len(routes))
    print("Total transitions:", transistions)
    print()

    #breadth first search
    def bfs(start,end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in routes:
            return None
        shortest_path = None
        for node in routes[start]:
            if node[0] not in path:                 #node[0] = place
                sp = bfs(node[0], end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path
    
    #printing the results of breadth first search
    print("Breadth First Search")
    for end in endGoal:
        solution = bfs(startGoal,end)
        print("States visited:", end=" ")
        for i in range(1, len(solution) - 1):
            print(solution[i])
        print("Found Path Length:", len(solution))
        for i in range(len(solution)):
            if i == len(solution) - 1:
                print(solution[i])
            else:
                print(solution[i] + " ==>", end=" ")
        print()

    #uniform Search Cost:
    def uniformCostSearch(start, end, path = [],cost = 0):
        path = path + [start]
        if start == end:
            return (path,cost)
        if start not in routes:
            return None
        cheapPath = None
        for node in routes[start]:
            if node[0] not in path:
                cp = uniformCostSearch(node[0],end,path,cost + node[1])
                if cp:
                    if cheapPath is None or cheapPath[1] > cp[1]:
                        cheapPath = cp
        return cheapPath


    #Printing the result of uniform cost search
    print("Uniform Cost Search")
    for end in endGoal:
        solution = uniformCostSearch(startGoal,end)
        print("States visited:", end=" ")
        for i in range(1, len(solution[0]) - 1):
            print(solution[0][i])
        print("Found Path Length:", len(solution[0]), "with total cost of",solution[1])
        for i in range(len(solution[0])):
            if i == len(solution[0]) - 1:
                print(solution[0][i])
            else:
                print(solution[0][i] + " ==>", end=" ")
        print()
        
if __name__ == '__main__':
    main()
    