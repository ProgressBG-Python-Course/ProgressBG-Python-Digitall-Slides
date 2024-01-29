def get_user_data():
    return {
                "name" : "ada",
                "height": "189",
                "weight": "55"
            }

def calc_BMI(name,height, weight):
    print(name,height, weight)

user_data = get_user_data()
bmi = calc_BMI(**user_data )
