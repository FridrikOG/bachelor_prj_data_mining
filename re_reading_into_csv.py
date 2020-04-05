import csv

def check_file():

    first_bool_lis = ['DUMMessaging15K', 'DUMSocialMedia10K', 'DUMWikipedia4K', 'NUMSearchEngines75K', 'DUMMaps4K', 'DUMEmail20K', 'DUMAdBlocker2K']
    second_bool_lis = ['DUMMessaging30K', 'DUMSocialMedia20K', 'NUMWikipedia8K', 'DUMSearchEngines150K','DUMMaps8K', 'DUMEmail40K', 'DUMAdBlocker4K']
    user_entered_lis = ['MessagingResPrice', 'SocialMediaResPrice','WikipediaResPrice' , 'SearchEnginesResPrice', 'MapsResPrice', 'EmailResPrice', 'AdBlockerResPrice']
    first_val_lis = [15000, 10000, 4000, 75000, 4000, 20000, 2000]
    second_val_lis = [30000, 20000, 8000, 150000, 8000, 40000, 4000]


    
    with open('reservations.csv') as f_in, open('new_reservations.csv', 'w') as f_out:
        # Write header unchanged
        header = f_in.readline()
        f_out.write(header)
        csvReader = csv.writer(f_in, delimiter = ';')
        # Transform the rest of the lines
        for line in csvReader:
            f_out.writerow(line)
            try:
                print(line)
                print('\n')
                for i in range(len(first_bool_lis)):
                    user_entered = user_entered_lis[i]
                    #first_bool = line[user_entered]
                    print(user_entered)
                
                
            except:
                print("Problem")
            

def test_file():
    print("\n" * 4)
    check_file()


filename = 'Reservations.csv'


test_file()