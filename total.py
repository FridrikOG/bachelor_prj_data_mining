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

# Source: https://px.hagstofa.is/pxis/pxweb/is/Samfelag/Samfelag__vinnumarkadur__vinnumarkadsrannsokn__3_arstolur/VIN00901.px/table/tableViewLayout1/?rxid=e78da67c-0aff-412e-87d6-6118773509e8
# All numbers for Iceland

# Working full time Iceland (more than 35 hours a week)
# 16 to 74 years old
WORKING_FULL_TIME = 155900
TOTAL_PEOPLE = 257300
TOTAL_OTHER_PEOPLE = TOTAL_PEOPLE - WORKING_FULL_TIME



def add_to_dict(res_price,line, user_entered_lis, fieldnames):
    for i in range(len(user_entered_lis)):
        try:
            lis = res_price[fieldnames[i]]
            lis.append(line[user_entered_lis[i]])
            res_price[fieldnames[i]] = lis
        except:
            res_price[fieldnames[i]] = [line[user_entered_lis[i]]]
    return res_price

# Creates a new dictionary and sums up the corresponding field names
def sum_numbers(dic, fieldsnames, multiplier):
    new_dict = {}
    for key in (dic.keys()):
        lis = dic[key]
        #print(key)
        new_lis = []
        for y in lis:
            
            if y != '':
                new_lis.append(y)
                try:
                    new_dict[key] += int(y)
                except:
                    new_dict[key] = int(y)
        print(new_dict[key], key)
        
        new_dict[key] = round(new_dict[key]/len(new_lis),0)
        new_dict[key] = round(new_dict[key]* multiplier,2)
        try:
            new_dict['sum'] += new_dict[key]
        except:
            new_dict['sum'] = new_dict[key]
    return new_dict


def check_file():
    user_entered_lis = ['MessagingResPrice', 'SocialMediaResPrice','WikipediaResPrice' , 'SearchEnginesResPrice', 'MapsResPrice', 'EmailResPrice', 'AdBlockerResPrice']

    res_price_emp = {}
    res_price_other = {}

    file = 'total_out.csv'
    with open('new_reservations.csv') as f_in:
        
        with open(file, 'w') as csvfile:
            csvReader = csv.DictReader(f_in, delimiter = ';')
            #fieldnames = ['Timestamp','Messaging15K','DUMMessaging15K','Messaging30K','DUMMessaging30K','MessagingResPrice','SocialMedia10K','DUMSocialMedia10K','SocialMedia20K','DUMSocialMedia20K','SocialMediaResPrice','Wikipedia4K','DUMWikipedia4K','Wikipedia8K','NUMWikipedia8K','WikipediaResPrice','SearchEngines75K','NUMSearchEngines75K','SearchEngines150K','DUMSearchEngines150K','SearchEnginesResPrice','Maps4K','DUMMaps4K','Maps8K','DUMMaps8K','MapsResPrice','Email20K','DUMEmail20K','Email40K','DUMEmail40K','EmailResPrice','UseAdBlocker','UseAdBlocker','OddsPaidAdsBrowser','NUMOddsPaidAdsBrowser','OddsUseAdBlocker','NUMOddsUseAdBlocker','AdBlocker2K','DUMAdBlocker2K','AdBlocker4K','DUMAdBlocker4K','AdBlockerResPrice','BirthYear','Income','Income_groupsmedian','Status','Working','InSchool','Other','Age','Agegroups']
            fieldnames = ['MessagingAVG', 'SocialMediaAVG', 'WikipediaAVG', 'SearchEnginesAVG', 'MapsAVG', 'EmailAVG', 'adblockerAVG','Status','sum', 'population', 'per_person' ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ';')
            status = StatusCounter()
            writer.writeheader()
            for line in csvReader:
                file_status = line['Status'].lower()
                if file_status == 'working':
                    status.employed += 1
                    res_price_emp = add_to_dict(res_price_emp, line, user_entered_lis, fieldnames)
                else:
                    status.in_school += 1 
                    res_price_other = add_to_dict(res_price_other,line, user_entered_lis, fieldnames)
           

            write_dict_emp = sum_numbers(res_price_emp, fieldnames, WORKING_FULL_TIME)
            write_dict_emp['Status'] = 'working'
            write_dict_emp['population'] = WORKING_FULL_TIME
            write_dict_emp['per_person'] = write_dict_emp['sum']/WORKING_FULL_TIME
            writer.writerow(write_dict_emp)
            write_dict_stud = sum_numbers(res_price_other, fieldnames, TOTAL_OTHER_PEOPLE)
            write_dict_stud['Status'] = 'other'
            write_dict_stud['population'] = TOTAL_OTHER_PEOPLE
            write_dict_stud['per_person'] = write_dict_stud['sum']/TOTAL_OTHER_PEOPLE
            writer.writerow(write_dict_stud)

            

def test_file():
    print("\n" * 4)
    check_file()


filename = 'Reservations.csv'


test_file()