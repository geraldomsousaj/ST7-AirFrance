import pandas as pd

# initializing parameters
passenger_id = 0

class Passenger:
    def __init__(self, group_index, passenger_id, description, transit_time=0):
        """
            group_index : 
            passenger_id : 
            description : men, women, wheelchair, child
            business_economic : class (Business, Economic)
            transit_time : optional parameter (inf if there is not transit time)
        
        """
        self.group_index = group_index
        self.passenger_id = passenger_id
        self.description = description
        # self.business_economic = business_economic
        self.transit_time = transit_time
        self.weight()
    
    def weight(self):
        if self.description == 'women':
            self.weight = 70
        elif self.description == 'men':
            self.weight = 85
        elif self.description == 'child':
            self.weight = 35
        else: 
            self.weight = 70 # need to check this value

class Group:

    def __init__(self, id_group, num_women, num_men, transit_time=0):
        self.id_group = id_group
        self.num_women = num_women
        self.num_men = num_men
        self.transit_time = transit_time

        self.members = []

        global passenger_id

        for i in range(self.num_women):
            self.members.append(Passenger(
                self.id_group,
                passenger_id,
                'women',
                self.transit_time
            ))
            passenger_id+=1
        
        for i in range(self.num_men):
            self.members.append(Passenger(
                self.id_group,
                passenger_id,
                'men',
                self.transit_time
            ))
            passenger_id+=1
        
        return
    
    
def read_and_preprocess(file, date):
    df = pd.read_excel(file, date)
    
    df['TransitTime (min)'] = df['TransitTime'].apply(lambda x: float(str(x).split(':')[0])*60+float(str(x).split(':')[1]))

    df[['Femmes', 'Hommes', 'Enfants', 'WCHR', 'WCHB']] = df[['Femmes', 'Hommes', 'Enfants', 'WCHR', 'WCHB']].fillna(0)

    return df

def get_list_passengers(df):
    list_groups = {}

    for idx, row in df.iterrows():

        list_groups[int(idx)] = Group(
            id_group=int(idx),
            num_women=int(row['Femmes']),
            num_men=int(row['Hommes']),
            transit_time=row['TransitTime (min)']
        )
    
    return list_groups

