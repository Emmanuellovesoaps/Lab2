def display_main_menu():
    print('Enter some numbers separated by commas (e.g. 5, 67, 32)')

def calc_average_temperature(num_list):
    Average_Temp = sum(num_list)/len(num_list)
    return Average_Temp

def calc_min_max_temperature(num_list):
    Min_Temp = int(min(num_list))
    Max_Temp = int(max(num_list))
    return (Min_Temp,Max_Temp)

def calc_median_temperature(num_list):
    sorted_list = sorted(num_list)
    length_list = len(sorted_list)
    
    if length_list % 2 == 0:
        median1 = length_list // 2
        median2 = median1 - 1
        median_number = (sorted_list[median1] + sorted_list[median2]) / 2

    else:
        median1 = length_list // 2
        median_number = sorted_list[median1]

    return median_number


def get_user_input():
    user_input = input()
    splitted_numbers = user_input.split(',')
    num_list = [float(num.strip()) for num in splitted_numbers]
    return num_list

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    avg = calc_average_temperature(num_list)
    min_max = calc_min_max_temperature(num_list)
    median = calc_median_temperature(num_list)

    print("The Average Temperature is : ", avg)
    print("The Minimum and Maximum Temperatures : ", min_max, "respectively")
    print("The Median Temperature : " , median)
    
if __name__ == "__main__":
    main()

