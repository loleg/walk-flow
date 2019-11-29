import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("Basel_Daten.csv", delimiter=';')
    locs = sorted(list(set(data['SiteName'])))
    data_list = {loc:data[data['SiteName'] == loc] for loc in locs}
    data_loc_list = {}
    for loc, loc_data in data_list.items():
        dates = [x.split('+') for x in loc_data['DateTimeFrom'].values]
        loc_data = loc_data.assign(TimeStamp=[x[0] for x in dates], Duration=[x[1] for x in dates])
        loc_data = loc_data.set_index('TimeStamp')
        loc_data = loc_data[['Total', 'Duration', 'Year', 'Month', 'Weekday', 'HourFrom']]
        data_loc_list[loc] = loc_data
    for i in range(len(locs)):
        print("%s\n%s\n-----\n"%(locs[i], data_loc_list[locs[i]]))