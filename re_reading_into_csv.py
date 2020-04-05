import csv

def check_file():

    first_bool_lis = ['DUMMessaging15K', 'DUMSocialMedia10K', 'DUMWikipedia4K', 'NUMSearchEngines75K', 'DUMMaps4K', 'DUMEmail20K', 'DUMAdBlocker2K']
    second_bool_lis = ['DUMMessaging30K', 'DUMSocialMedia20K', 'NUMWikipedia8K', 'DUMSearchEngines150K','DUMMaps8K', 'DUMEmail40K', 'DUMAdBlocker4K']
    user_entered_lis = ['MessagingResPrice', 'SocialMediaResPrice','WikipediaResPrice' , 'SearchEnginesResPrice', 'MapsResPrice', 'EmailResPrice', 'AdBlockerResPrice']
    first_val_lis = [15000, 10000, 4000, 75000, 4000, 20000, 2000]
    second_val_lis = [30000, 20000, 8000, 150000, 8000, 40000, 4000]

    file = 'new_reservations.csv'
    with open('reservations.csv') as f_in:
        with open(file, 'w') as csvfile:
            csvReader = csv.DictReader(f_in, delimiter = ';')
            fieldnames = ['Timestamp','Messaging15K','DUMMessaging15K','Messaging30K','DUMMessaging30K','MessagingResPrice','SocialMedia10K','DUMSocialMedia10K','SocialMedia20K','DUMSocialMedia20K','SocialMediaResPrice','Wikipedia4K','DUMWikipedia4K','Wikipedia8K','NUMWikipedia8K','WikipediaResPrice','SearchEngines75K','NUMSearchEngines75K','SearchEngines150K','DUMSearchEngines150K','SearchEnginesResPrice','Maps4K','DUMMaps4K','Maps8K','DUMMaps8K','MapsResPrice','Email20K','DUMEmail20K','Email40K','DUMEmail40K','EmailResPrice','UseAdBlocker','UseAdBlocker','OddsPaidAdsBrowser','NUMOddsPaidAdsBrowser','OddsUseAdBlocker','NUMOddsUseAdBlocker','AdBlocker2K','DUMAdBlocker2K','AdBlocker4K','DUMAdBlocker4K','AdBlockerResPrice','BirthYear','Income','Income_groupsmedian','Status','Working','InSchool','Other','Age','Agegroups']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ';')
            
            writer.writeheader()
            count = 0
            for x in csvReader:
                count += 1

                for i in range(len(first_bool_lis)):
                    try:
                        first_bool_data = x[first_bool_lis[i]]
                        second_bool_data = x[second_bool_lis[i]]
                        user_entered_data = int(x[user_entered_lis[i]])
                        first_val = first_val_lis[i]
                        second_val = second_val_lis[i]
                        
                        if first_bool_data == '0':
                            if second_bool_data == '0':
                                # If he says no to both then his entered value has to be less than second val
                                if user_entered_data < second_val:
                                    user_entered_data = second_val
                            else:
                                if user_entered_data < first_val or user_entered_data > second_val:
                                    user_entered_data = first_val
                        else:
                        # Here they said yes to first one
                            if user_entered_data > first_val:
                                user_entered_data = first_val
                        x[user_entered_lis[i]] = str(user_entered_data)
                
                    except:
                        pass
                writer.writerow(x)
        

def test_file():
    print("\n" * 4)
    check_file()


filename = 'Reservations.csv'


test_file()