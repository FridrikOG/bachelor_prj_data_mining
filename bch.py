import csv



def check_file(filename, first_bool, second_bool, user_entered, first_val, second_val, count = 0):
    with open (filename) as resFile:
        csvReader = csv.DictReader(resFile, delimiter = ';')
        count += 1
        problem_lis = []
        user_lis = []
        for line in csvReader:
            try:
                # 22
                user_entered_data = int(line[user_entered])
                count +=1
                first_bool_data = line[first_bool]
                second_bool_data = line[second_bool]
                
                if first_bool_data == '0':
                    if user_entered_data == 0:
                        print("Line ", count, " User entered 0")
                    if second_bool_data == '0':
                        # If he says no to both then his entered value has to be less than second val
                        if user_entered_data < second_val:
                            diff = second_val - user_entered_data
                            problem_lis.append((count, "Line. no to both, still lower by ", diff ))
                            user_lis.append([count, diff, user_entered_data])
                    else:
                        # 0 1
                        # User entered data has to be larger than the first but smaller than the second
                        if user_entered_data < first_val:
                            diff = first_val - user_entered_data
                            problem_lis.append((count, "Line. No to first, yes to second. Answer lower than first " , diff))
                            user_lis.append([count, diff, user_entered_data])
                        elif user_entered_data > second_val:
                            diff = user_entered_data - second_val
                            problem_lis.append((count, "Line. No to first, yes to second. Answer higher than second ", diff))
                            user_lis.append([count, diff, user_entered_data])

                else:
                    # Here they said yes to first one
                    if user_entered_data > first_val:
                        diff =  user_entered_data - first_val
                        problem_lis.append((count, " Line: Yes to first, Asnwer higher than first", diff))
                        user_lis.append([count, diff, user_entered_data])
            except:
                pass
        return problem_lis, user_lis
            

def test_file(filename, first_bool, second_bool, user_entered, first_val, second_val):
    print("\n" * 4)
    print("Testing ", first_bool, second_bool, first_val, second_val)
    if first_bool == 'DUMMessaging15K':
        check_lines, user_lis = check_file(filename, first_bool, second_bool, user_entered, first_val, second_val, count = 23)
    else:
        check_lines, user_lis = check_file(filename, first_bool, second_bool, user_entered, first_val, second_val)
    print("HOW MANY ERRORS ", len(check_lines))
    
    for y in check_lines:
        print(y)
    return check_lines, user_lis



filename = 'Reservations.csv'

first_bool_lis = ['DUMMessaging15K', 'DUMSocialMedia10K', 'DUMWikipedia4K', 'NUMSearchEngines75K', 'DUMMaps4K', 'DUMEmail20K', 'DUMAdBlocker2K']
second_bool_lis = ['DUMMessaging30K', 'DUMSocialMedia20K', 'NUMWikipedia8K', 'DUMSearchEngines150K','DUMMaps8K', 'DUMEmail40K', 'DUMAdBlocker4K']
user_entered_lis = ['MessagingResPrice', 'SocialMediaResPrice','WikipediaResPrice' , 'SearchEnginesResPrice', 'MapsResPrice', 'EmailResPrice', 'AdBlockerResPrice']
first_val_lis = [15000, 10000, 4000, 75000, 4000, 20000, 2000]
second_val_lis = [30000, 20000, 8000, 150000, 8000, 40000, 4000]

dict_wrong_cata = {}
total_lis = []
total_total_lis = []
total_avg_with_zero = 0
total_avg_without_zero = 0
for i in range(len(first_bool_lis)):
    first_bool = first_bool_lis[i]
    second_bool = second_bool_lis[i]
    user_entered = user_entered_lis[i]
    first_val = first_val_lis[i]
    second_val = second_val_lis[i]
    returned, user_lis = test_file(filename, first_bool, second_bool, user_entered, first_val, second_val)
    print(user_lis)
    print("LOGGING USER LIS ", user_lis[1][2])
    user_entered_name = user_entered.replace(user_entered[-8:], '')

    dict_wrong_cata[user_entered_name] = user_lis
    
    total_with_zero = 0
    total_without_zero = 0
    for x in user_lis:
        if x[0] not in total_lis:
            total_lis.append(x[0])
        total_total_lis.append(x[0])
        total_with_zero += x[1]

        if x[2] < 300:
            total_without_zero += x[1]

    average_with_zero = round((total_with_zero/len(user_lis)),2)
    average_without_zero = round((total_without_zero/len(user_lis)),2)
    total_avg_with_zero += average_with_zero
    total_avg_without_zero += average_without_zero
    print(user_entered_name, "average incorrect by (with zero) ", total_avg_with_zero)
    print(user_entered_name, "average incorrect by (without zero) ", total_avg_without_zero)

print("Total cases" ,len(total_total_lis))
print("Total unique cases ", len(total_lis))
print("Total average incorrect by (with zero) ", round(total_avg_with_zero/len(dict_wrong_cata),2))
print("Total average incorrect by (without zero) ", round(total_avg_without_zero/len(dict_wrong_cata),2))