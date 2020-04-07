import csv
import string

class StatusCounter():
    def __init__(self, unemployed = 0, employed = 0 , in_school = 0, retired = 0, disabled = 0):
        self.unemployed = unemployed
        self.employed = employed
        self.in_school = in_school
        self.retired = retired
        self.disabled = disabled
    
    def print_numbers(self):
        print("Number of employed ", self.employed)
        print("Number of in school ", self.in_school)




def add_to_dict(res_price,line, user_entered_lis, fieldnames):
    for i in range(len(user_entered_lis)):
        print([line[user_entered_lis[i]]])
        print(fieldnames[i])
        try:
            lis = res_price[fieldnames[i]]
            lis.append(line[user_entered_lis[i]])
            res_price[fieldnames[i]] = lis
        except:
            res_price[fieldnames[i]] = [line[user_entered_lis[i]]]
    return res_price

# Creates a new dictionary and sums up the numbers
# Returns the new number
def sum_numbers(dict, fieldsnames)


def check_file():
    user_entered_lis = ['MessagingResPrice', 'SocialMediaResPrice','WikipediaResPrice' , 'SearchEnginesResPrice', 'MapsResPrice', 'EmailResPrice', 'AdBlockerResPrice']

    res_price_emp = {}
    res_price_stud = {}

    file = 'avg_out.csv'
    with open('new_reservations.csv') as f_in:
        with open(file, 'w') as csvfile:
            csvReader = csv.DictReader(f_in, delimiter = ';')
            #fieldnames = ['Timestamp','Messaging15K','DUMMessaging15K','Messaging30K','DUMMessaging30K','MessagingResPrice','SocialMedia10K','DUMSocialMedia10K','SocialMedia20K','DUMSocialMedia20K','SocialMediaResPrice','Wikipedia4K','DUMWikipedia4K','Wikipedia8K','NUMWikipedia8K','WikipediaResPrice','SearchEngines75K','NUMSearchEngines75K','SearchEngines150K','DUMSearchEngines150K','SearchEnginesResPrice','Maps4K','DUMMaps4K','Maps8K','DUMMaps8K','MapsResPrice','Email20K','DUMEmail20K','Email40K','DUMEmail40K','EmailResPrice','UseAdBlocker','UseAdBlocker','OddsPaidAdsBrowser','NUMOddsPaidAdsBrowser','OddsUseAdBlocker','NUMOddsUseAdBlocker','AdBlocker2K','DUMAdBlocker2K','AdBlocker4K','DUMAdBlocker4K','AdBlockerResPrice','BirthYear','Income','Income_groupsmedian','Status','Working','InSchool','Other','Age','Agegroups']
            fieldnames = ['MessagingAVG', 'SocialMediaAVG', 'WikipediaAVG', 'SearchEnginesAVG', 'MapsAVG', 'EmailAVG', 'adblockerAVG','Status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ';')
            status = StatusCounter()

            writer.writeheader()
            for line in csvReader:
                file_status = line['Status'].lower()
                if file_status == 'working':
                    status.employed += 1
                    res_price_emp = add_to_dict(res_price_emp, line, user_entered_lis, fieldnames)
                elif 'hool' in file_status:
                    status.in_school += 1 
                    res_price_stud = add_to_dict(res_price_stud,line, user_entered_lis, fieldnames)
            print(res_price_emp)

            
            writer.writerow()

            status.print_numbers()

def test_file():
    print("\n" * 4)
    check_file()


filename = 'Reservations.csv'


test_file()