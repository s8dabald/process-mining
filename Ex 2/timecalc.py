import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('ProcessMiningSampleLog.csv')
df = df.sort_values(by=['Case ID', 'Complete Timestamp'])
df['Complete Timestamp'] = pd.to_datetime(df['Complete Timestamp'])
#print(df.head())
df['delta'] = df.groupby('Case ID')['Complete Timestamp'].diff()
def counter(type ="min"):
    result ={}
    counter={}
    for case in df['Case ID'].unique():
        df_cases = df[df['Case ID'] == case]
        last = ""
        for row in df_cases.itertuples():
            if last != "":
                #print("In Case", row._1,"from", last, "-", row.Activity, "it took", row.delta)
                transition =last + '  -  '+ row.Activity
                if transition not in result:
                    result.update({transition: row.delta})
                    counter.update({transition:1})
                elif type == "avg":
                    a = result[transition]
                    b = counter[transition]
                    result.update({transition: a+row.delta})
                    counter.update({transition: b+1})
                else:
                    if type =="min" and result[transition] > row.delta:
                        result.update({transition:row.delta})
                    elif type =="max" and result[transition] < row.delta:
                        result.update({transition: row.delta})
            last = row.Activity

    if type == "avg":
        for x in result.keys():
            a = result[x]
            b = counter[x]
            result.update({x:a/b})
    return result

types = {"Average transition time":"avg","Minimal transition time": "min","Maximum transition time": "max"}

for x in types.keys():
    print(x)
    values = counter(types[x])
    for y in values.keys():
        print(y,values[y])
    print("\n")
