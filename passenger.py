class Passenger:
    def __init__(self, group_index, passenger_id, description, business_economic, transit_time=0):
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
        self.business_economic = business_economic
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