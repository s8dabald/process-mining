from math import log
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
list_of_paths =[]
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
def entropy(a,b):
    if a/(a+b)==0 or b/(b+a)==0 or a/(b+a)==1 or b/(b+a)==1:
        return 0
    return -((a/(a+b) * log(a/(a+b),2))+(b/(a+b) * log(b/(a+b),2)))

def node_calc(existing_path={}):
    all_entropies={}
    for x in input_dict['D1']: #go through attributes using Day 1
        possible_values = []
        result= 0
        for y in input_dict:
            if not possible_values.count([x,input_dict[y][x]]):
                possible_values.append([x,input_dict[y][x]])
        for value in possible_values:

            argu = {value[0]: value[1]}
            argu.update(existing_path)

            a,b = count_occurences(argu)
            try:
                possible_values[possible_values.index(value)].append(a+b)
                possible_values[possible_values.index(value)].append(entropy(a,b))
            except ZeroDivisionError:
                if possible_values[possible_values.index(value)][0] == 'Tennis':
                    print (existing_path,count_occurences(existing_path),"no more splits left")
                    list_of_paths.append(existing_path)
                    list_of_paths[list_of_paths.index(existing_path)].update({'result': count_occurences(existing_path)})

                    return()

                possible_values[possible_values.index(value)].append(1)
        if x == 'Tennis':
            if possible_values[0][1]=='No':

                all_entropies[x] = entropy(possible_values[0][2], possible_values[1][2])

            elif possible_values[0][1]=='Yes':

                all_entropies[x]= entropy(possible_values[1][2], possible_values[0][2])

        else:
            for value in possible_values:
                result += value[2]/sum(y[2] for y in possible_values) * value[3] #weighted entropy for node
            all_entropies[x]= result

    tennis = all_entropies['Tennis']
    for key in all_entropies:
        all_entropies[key] = tennis-all_entropies[key] #calc gain
    print ("\ncurrently taken path:",existing_path,"\ngain from that node:",all_entropies)
    winner = max(all_entropies, key=all_entropies.get)
    print("next node:",winner)
    return(winner)

def recursive_loop(existing_path={}):
    last_win = node_calc(existing_path)
    if not last_win:
        return

    currently =[]
    for x in input_dict:

        if not currently.count({last_win: input_dict[x][last_win]}):
            currently.append({last_win: input_dict[x][last_win]})
    for x in currently:
        check = existing_path.copy()
        check.update(x)
        recursive_loop(check)

def get_paths():
    recursive_loop()
    return(list_of_paths)

if __name__ == '__main__':
    recursive_loop()
