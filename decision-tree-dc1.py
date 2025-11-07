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
print(input_dict)

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
def node_calc():
    for x in input_dict['D1']:
        possible_values = []
        result= 0
        for y in input_dict:
            if not possible_values.count([x,input_dict[y][x]]):
                possible_values.append([x,input_dict[y][x]])
        for value in possible_values:
            argu = {value[0]: value[1]}
            a,b = count_occurences(argu)
            possible_values[possible_values.index(value)].append(a+b)
            possible_values[possible_values.index(value)].append(entropy(a,b))
        #print(possible_values)
        print(possible_values)
        for value in possible_values:
            result += value[2]/sum(y[2] for y in possible_values) * value[3]
        print(x,result)


            #print(value, a, b,entropy(a,b))
        #print(possible_values)



#print(count_occurences(Forecast='Sunny',Temperature='Hot'))
node_calc()