import csv
variable = 0

def set_highscore(score):
    with open('highscore.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            variable = row[0]
    try:
        value = int(score)
    except:
        value = 0

    if int(variable) < value:
        with open('highscore.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            try:
                if value > writer.writerow([value]):
                    1
            except:
                0

def get_highscore():
    variable = 0
    with open('highscore.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            variable = row[0]
    return variable