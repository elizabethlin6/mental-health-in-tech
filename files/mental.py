import csv

def extract_data(filename, column_names):

    filecsv = open(filename)               # Reads in CSV file
    input_file = csv.DictReader(filecsv)   # creates a dictionary for each row

    list = []


    for line in input_file:                # create dict for one line/per engineer

            engineer_dict = {}
            for column in column_names:
                person = line[column]
                person = person.replace("'",'')
                engineer_dict[column] = person
            list.append(engineer_dict)

    return list

def analyze_dict(list):
    greater_35 = 0
    less_35 = 0

    for engineer in list:
        if int(engineer['Age']) >= int(35):
            greater_35 += 1
        else:
            less_35 += 1
    total = int(greater_35 + less_35)
    print "The number of engineers in this study that are older than 35 is:", greater_35
    print "The number of engineers in this study that are younger than 30 is:", less_35
    print "The total people in this study is", total

    return [greater_35, less_35, total]


def from_us(list):
    us_from = 0
    for engineer in list:
        if engineer['Country'] == 'United States':
            us_from += 1
    return us_from

def gender(gender_dict):
    male_count = 0.0
    female_count = 0.0
    unknown = 0.0
    
    for person in gender_dict:
        if person['Gender'] == 'Male':
            male_count += 1.0
        elif person['Gender'] == 'Female':
            female_count += 1.0
        else:
            unknown += 1.0
    return (male_count, female_count, unknown)
    
def mental_gender_distribution(gender_dict):
    gender_list = []
    females = 0
    males = 0
    other = 0
    for person in gender_dict:
        if person["treatment"] == 'Yes' or 'Y':
            value = person['Gender']
            gender_list.append(value)

    for gender_type in gender_list:
        if gender_type == 'Female':
            females += 1
        elif gender_type == 'Male':
            males += 1
        else:
            other += 1
    return (len(gender_list), females, males, other)
    
            
            
        
    


def intro():
    print "This is Elizabeth's attempt to read in some CSV files to practice Python!"

def main():
    intro()
    full_dict = extract_data('mental_health_tech.csv', ["Age","Gender","Country","treatment"])
    print
    list_info = analyze_dict(full_dict)
    print
    print "The number of people in this study that are from United States:", from_us(full_dict)
    value = list_info[2] - from_us(full_dict)
   # print "That means out of the", list_info[2], "people in this study," value, "are not other countries other than United States."
    gender_dict = extract_data('mental_health_tech.csv', ["Gender"])
   # print gender_dict
    gender_tuple = gender(gender_dict)
    male_count = gender_tuple[0]
    female_count = gender_tuple[1]
    unknown = gender_tuple[2]
  #  total = male_count + female_count + unknown
 #   print total
#    print gender(gender_dict)
    counts = mental_gender_distribution(full_dict)
    print "The ratio of men to women in this study is", counts[2], ":", counts[1]

if __name__ == "__main__":
     main()
