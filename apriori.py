import itertools

t1 = ["Deodorant", "Shower gel", "Toothpaste"]
t2 = ["Shower gel", "Razor blades", "Toothpaste"]
t3 = ["Chewing gum", "Toothpaste"]
t4 = ["Deodorant", "Toothpaste", "Shower gel"]
t5 = ["Toothpaste", "Shower gel", "Deodorant", "Razor blades"]
t6 = ["Chewing gum"]
t7 = ["Deodorant", "Chewing gum", "Shower gel"]

result = []
min_support = 0.5
shopping_basket = [t1, t2, t3, t4, t5, t6, t7]


def counter (items):

    counti = 0
    for basket in shopping_basket:
        #if items[0] in basket:
        if len(items)>1:

            items_changed = [item for sub in items for item in sub]
            #print(items,"in counter")
            if all(item in basket for item in items_changed):
                counti += 1
        else:
            if all(item in basket for item in items):
                counti += 1
    return counti
def support(items):
    sup = counter(items) / len(shopping_basket)
    return sup
def eliminate(item):

    if support(item) >= min_support:
        result.append(item)

def new_combination(items):
    next_round=[]
    #print(items)
    for i in range(len(items)): #goes through all lists
        #print(i)
        for j in range(i+1,len(items)): #goes through the rest

            matches = 0
            for a in items[i]: #goes through items in list 1
                for b in items[j]: #same for list2
                    if a == b:
                        matches += 1
            if matches == len(items[i])-1:
                #print(items[i],items[j])
                new_list = items[i]+items[j]
                #print(new_list, "new list")
                try:
                    new_list = list(set(new_list))
                except TypeError:
                    flat = list(itertools.chain.from_iterable(new_list))
                    new_list = list(set(flat))

                #print(new_list)
                newer_list =[]
                for b in new_list:
                    newer_list.append([b])
                next_round.append(newer_list)
    #print(next_round)
    return next_round
def round1():
    print("===Apriori Algorithm===\n")
    print("===Finding all 1-item-sets===")
    unique_items =[]
    all_items=[]
    for basket in shopping_basket:
        all_items += basket
    all_items = list(set(all_items))
    for item in all_items:
        if item not in unique_items:
            unique_items.append([item])
    print("1-item-sets, count, support")
    for items in unique_items:
        print(items,counter(items),f"{support(items):.2f}")
        eliminate(items)
    print("\nCurrent item-sets after removing items with support < 0.5\n",result,"\n")

def apriori_loop():
    round1()
    for i in range(len(shopping_basket)+1):
        next_round=[]
        for items in result:
            #print(items)
            if len(items) ==i+1:
                #print(items)
                next_round.append(items)

        current_round = new_combination(next_round)
        if current_round == []:
            return
        print(f"{i+2}-item-sets, count, support")
        for x in current_round:
            print(x, counter(x),f"{support(x):.2f}")
            eliminate(x)


        print("\nCurrent item-sets after removing items with support < 0.5\n", result, "\n")
        i += 1

def confidence(x,y): #y is x->y
    return support(y)/support(x)
def final_calculation():
    apriori_loop()
    print("assosiation rule, support, confidence")
    for item_sets in result:
        if len(item_sets)>1:
            for x,y in itertools.permutations(item_sets, len(item_sets)):
                print(f"{x}->{y}, {support(item_sets):.2f}, {confidence(x,item_sets):.2f}")


final_calculation()








