class Processing:
    def AgeCategorized(x):
        if x == "18-24":
            return 1
        elif x == "25-29":
            return 2
        elif x == "30-34":
            return 3
        elif x == "35-39":
            return 4
        elif x == "40-44":
            return 5
        elif x == "45-49":
            return 6
        elif x == "50-54":
            return 7
        elif x == "55-59":
            return 8
        elif x == "60-64":
            return 9
        elif x == "65-69":
            return 10
        elif x == "70-74":
            return 11
        elif x == "75-79":
            return 12
        else:
            return 13

    def to_numeric(x):
    
        if x == "Yes":
            return 1
        elif x == "No":
            return 0
        else:
            pass
    
    def DiabeticNumeric(x):
        if x == "Yes":
            return 1
        elif x == "No":
            return 0
        elif x == "No, borderline diabetes":
            return 0
        else:
            return 1

class SingleColumn:
    def AgeCategory(x):
        if x == "18-24":
            return 1
        elif x == "25-29":
            return 2
        elif x == "30-34":
            return 3
        elif x == "35-39":
            return 4
        elif x == "40-44":
            return 5
        elif x == "45-49":
            return 6
        elif x == "50-54":
            return 7
        elif x == "55-59":
            return 8
        elif x == "60-64":
            return 9
        elif x == "65-69":
            return 10
        elif x == "70-74":
            return 11
        elif x == "75-79":
            return 12
        else:
            return 13

    def GenHealth(x):
        if x == "Fair":
            return [1, 0, 0, 0]
        elif x == "Good":
            return [0, 1, 0, 0]
        elif x == "Poor":
            return [0, 0, 1, 0]
        elif x == "Very good":
            return [0, 0, 0, 1]

    def Gender(x):
        if x == "Male":
            return 1
        elif x == "Female":
            return 0
        
    def to_numeric(x):
        if x == "Yes":
            return 1
        elif x == "No":
            return 0