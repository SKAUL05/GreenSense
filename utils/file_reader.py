from code_complexity import call_Chat_gpt_for_time_and_space_complexity, convert_complexity_to_number, give_start_rating,get_cyclomitic_complexity
import json
import math

def get_file_data(file_name):
    file = open(file_name)
    file_data = file.readlines()
    file.close()    
    return file_data

def extract_functions(file_data):
    fun = []
    i=0
    file_len = len(file_data)
    while i<file_len and " def " not in file_data[i]:
        i+=1
    print(file_data[i])
    one_fun= file_data[i]
    i+=1
    while i<file_len:
        if " def " in file_data[i]:
            fun.append(one_fun)
            one_fun = file_data[i]
        else:
            if "@" not in file_data[i]:
                one_fun+=file_data[i]
        i+=1
    fun.append(one_fun.split("if __name__")[0])

    return fun
# fun = []

def get_functions_from_file(file_names: list):
    funs=[]
    for file_name in file_names:
        # file = open(file_name)
        # file_data = file.readlines()
        # file.close()

        file_data = get_file_data(file_name)

        funs=extract_functions(file_data)
    
    return funs




# C:\Jatin\GreenSense\green_sense_flask\code_carbon\main.py
def get_score_for_code(file_path):
    file = open(file_path, "r")
    fun = file.read()
    file.close()
    print("Calling ChatGPT API to Get Complexities")
    resp = call_Chat_gpt_for_time_and_space_complexity(fun)
    resp = json.loads(resp)
    # print(resp)


    # resp = {'cal_n': {'time_complexity': 'O(n)', 'space_complexity': 'O(1)'}, 'cal_nlogn': {'time_complexity': 'O(n log n)', 'space_complexity': 'O(1)'}, 'cal_n_n': {'time_complexity': 'O(n^2)', 'space_complexity': 'O(1)'}, 'bubbleSort': {'time_complexity': 'O(n^2)', 'space_complexity': 'O(1)'}}
    print("Getting Cyclomatic Complexity")
    cyclo_comp = get_cyclomitic_complexity(fun=fun)
    # print(cyclo_comp)

    for c in cyclo_comp:
        name, comp = c.name, c.complexity
        resp[name]["cyclo_complexity"] = comp
    

    for res in resp:
        code = resp[res]
        score = convert_complexity_to_number(code["time_complexity"])+convert_complexity_to_number(code["space_complexity"])+code["cyclo_complexity"]
        resp[res]["score"] = score
        # print(score)
    
    return resp

# Star Rating


if __name__ == "__main__":
    # unoptimised
    print("unoptimised Code")
    score_resp_unoptimised = {'factorial': {'time_complexity': 'O(n)', 'space_complexity': 'O(n)', 'cyclo_complexity': 2, 'score': 22}, 'fibonacci': {'time_complexity': 
'O(2^n)', 'space_complexity': 'O(n)', 'cyclo_complexity': 2, 'score': 112}}
    path = 'utils/unoptimised_code.py'
    score_resp_unoptimised = get_score_for_code(path)
    


    # unoptimised
    print("\n\noptimised Code")
    score_resp_optimised = {'fibonacci': {'time_complexity': 'O(n)', 'space_complexity': 'O(n)', 'cyclo_complexity': 2, 'score': 22}, 'factorial': {'time_complexity': 
'O(n)', 'space_complexity': 'O(1)', 'cyclo_complexity': 2, 'score': 13}}
    path = 'utils/optimised_code.py'
    score_resp_optimised = get_score_for_code(path)
    # print(score_resp_unoptimised)
    # print(score_resp_optimised)
    print("\n\n")
    for function in score_resp_unoptimised:
        print(f"Calculating Score for Function {function}")
        old_score, new_score = score_resp_unoptimised[function]["score"],score_resp_optimised[function]["score"]
        print(f"Score for unoptimised Function {old_score}")
        print(f"Score for optimised Function {new_score}")
        print(f"Calculating Sart Rating for Function {function}")
        star_rating = give_start_rating(old_score,new_score)
        # print(star_rating)
        old_star, new_star = star_rating["old_code"], star_rating["new_code"]
        old_extra = 0 if math.ceil(old_star)==old_star else 1
        new_extra = 0 if math.ceil(new_star)==new_star else 1
        print("Old Code Star Rating:"+"\u2B50"*math.floor(old_star)+"\u2605"*old_extra)
        print("New Code Star Rating:"+"\u2B50"*math.floor(new_star)+"\u2605"*new_extra)
        print("\n\n")


    
# grinning face

# print("⭐","\U00002605")
# print("\u2605")
# print('\u2B50\U0001F3FB')
# print("\u2B50") # This will print the half yellow star emoji
# print("\U00002BE8")
# print("\U00002605")
# print("\N{loudly crying face}")
# print(emoji.emojize('Python is :half_star:'))