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
        try:
            lis = res_price[fieldnames[i]]
            lis.append(line[user_entered_lis[i]])
            res_price[fieldnames[i]] = lis
        except:
            res_price[fieldnames[i]] = [line[user_entered_lis[i]]]
    return res_price

# Creates a new dictionary and sums up the corresponding field names
def sum_numbers(dic, fieldsnames):
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
    return new_dict


def check_file():
    user_entered_lis = ['MessagingResPrice', 'SocialMediaResPrice','WikipediaResPrice' , 'SearchEnginesResPrice', 'MapsResPrice', 'EmailResPrice', 'AdBlockerResPrice']

    res_price_emp = {}
    res_price_stud = {}

    file = 'avg_out.csv'
    with open('new_reservations.csv') as f_in:
        
        with open(file, 'w') as csvfile:
            csvReader = csv.DictReader(f_in, delimiter = ';')
            #fieldnames = ['Timestamp','Messaging15K','DUMMessaging15K','Messaging30K','DUMMessaging30K','MessagingResPrice','SocialMedia10K','DUMSocialMedia10K','SocialMedia20K','DUMSocialMedia20K','SocialMediaResPrice','Wikipedia4K','DUMWikipedia4K','Wikipedia8K','NUMWikipedia8K','WikipediaResPrice','SearchEngines75K','NUMSearchEngines75K','SearchEngines150K','DUMSearchEngines150K','SearchEnginesResPrice','Maps4K','DUMMaps4K','Maps8K','DUMMaps8K','MapsResPrice','Email20K','DUMEmail20K','Email40K','DUMEmail40K','EmailResPrice','UseAdBlocker','UseAdBlocker','OddsPaidAdsBrowser','NUMOddsPaidAdsBrowser','OddsUseAdBlocker','NUMOddsUseAdBlocker','AdBlocker2K','DUMAdBlocker2K','AdBlocker4K','DUMAdBlocker4K','AdBlockerResPrice','BirthYear','Income','Income_groupsmedian','Status','Working','InSchool','Other','Age','Agegroups']
            fieldnames = ['MessagingAVG', 'SocialMediaAVG', 'WikipediaAVG', 'SearchEnginesAVG', 'MapsAVG', 'EmailAVG', 'adblockerAVG', 'percuseadblocker','Status' ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ';')
            status = StatusCounter()
            count_0 = 0
            count_1 = 0
            count_0_emp = 0
            count_1_emp = 0
            writer.writeheader()
            for line in csvReader:
                file_status = line['Status'].lower()
                
                
                if file_status == 'working':
                    status.employed += 1
                    res_price_emp = add_to_dict(res_price_emp, line, user_entered_lis, fieldnames)
                elif 'hool' in file_status:
                    status.in_school += 1 
                    res_price_stud = add_to_dict(res_price_stud,line, user_entered_lis, fieldnames)
                if 'hool' in file_status:
                    if line['UseAdBlocker'] == '0':
                        count_0 += 1
                    else:
                        count_1 += 1
                elif file_status =='working':
                    if line['UseAdBlocker'] == '0':
                        count_0_emp += 1
                    else:
                        count_1_emp += 1
                

            print("Students dont use ", count_0)
            print("Students  use ", count_1)

            print("Emp don't use ", count_0_emp)
            print("Emp use", count_1_emp)


            write_dict_emp = sum_numbers(res_price_emp, fieldnames)
            write_dict_emp['Status'] = 'working'
            percentage = round(100 * float(count_0_emp)/float(status.employed),2)
            write_dict_emp['percuseadblocker'] = round(100 - percentage,2)
            writer.writerow(write_dict_emp)
            
           
            print("percentage ", 100 - percentage)

            write_dict_stud = sum_numbers(res_price_stud, fieldnames)
            write_dict_stud['Status'] = 'school'
            percentage = round(100 * float(count_0)/float(status.in_school),2)
            write_dict_stud['percuseadblocker'] = round(100 - percentage,2)
            writer.writerow(write_dict_stud)

            
            
            status.print_numbers()

def test_file():
    print("\n" * 4)
    check_file()


filename = 'Reservations.csv'


test_file()