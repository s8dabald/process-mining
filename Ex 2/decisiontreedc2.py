
input_string= """Day Forecast Temperature Humidity Wind-strength Tennis
D1 Sunny Hot High Weak No
D2 Sunny Hot High Strong No
D3 Cloudy Hot High Weak Yes
D4 Rainy Mild High Weak Yes
D5 Rainy Cool Normal Weak Yes
D6 Rainy Cool Normal Strong No
D7 Cloudy Cool Normal Strong Yes
D8 Sunny Mild High Weak No
D9 Sunny Cool Normal Weak Yes
D10 Rainy Mild Normal Weak Yes
D11 Sunny Mild Normal Strong Yes
D12 Cloudy Mild High Strong Yes
D13 Cloudy Hot Normal Weak Yes
D14 Rainy Mild High Strong No"""
input_list = input_string.split("\n")#splits into lines
for line in input_list:
    input_list[input_list.index(line)] = line.split(" ")
input_dict = {}
for item in input_list[1:]:

    input_dict[item[0]] = dict( zip(input_list[0][1:],item[1:]) )
node_values = {} #dict oft all possible nodes and value
for x in input_dict['D1']:
    value = []
    for y in input_dict:
        if not value.count(input_dict[y][x]):
            value.append(input_dict[y][x])
    node_values[x] = value
list_of_paths = []
def count_occurences(argu):
    yes = 0
    no = 0
    for x in input_dict.values():
        if all(x.get(key) == value for key, value in argu.items()):
            if x.get('Tennis') == 'Yes':
                yes += 1
            elif x.get('Tennis') == 'No':
                no += 1
    return yes, no

def select_node(path,nodes):
    result = {}
    tennis = 0
    for x in nodes:
        calc = []
        weigths = []
        p=0
        for y in node_values[x]:
            path_new = path.copy()
            path_new[x] = y
            a,b = count_occurences(path_new)
            calc.append([a,b])

        total = 0
        for y in calc:
            total += y[0]+y[1]

        for y in calc:
            a = y[0]
            b = y[1]
            try:
                p += (1-(((a/(a+b))**2)+((b/(a+b))**2)))*((a+b)/total)
            except ZeroDivisionError:
                p+=0

        result[x] = p
    a,b = count_occurences(path)
    tennis = 1-(((a/(a+b))**2)+((b/(a+b))**2))
    for x in result:
        result[x] = tennis - result[x]


    winner = max(result, key=result.get)
    print("result",result)
    print(winner)
    return winner
def recursive_loop(existing_path={}):
    a,b = count_occurences(existing_path)
    if a==0 or b == 0:
        if count_occurences(existing_path) != (0 , 0):
            print(existing_path, count_occurences(existing_path))
            list_of_paths.append(existing_path)
            list_of_paths[list_of_paths.index(existing_path)].update({'result': count_occurences(existing_path)})
        return
    possible_nodes=[]
    for x in node_values:
        if x != 'Tennis' and all(x!= key for key in existing_path.keys()):
            possible_nodes.append(x)

    selected_node = select_node(existing_path, possible_nodes)
   # print("test",existing_path, possible_nodes)
    #try:
    for x in node_values[selected_node]:
        new_path = existing_path.copy()
        new_path[selected_node] = x
        recursive_loop(new_path)
    #except KeyError:
     #   return

def get_paths():
    recursive_loop()
    return list_of_paths
if __name__ == '__main__':
    recursive_loop()