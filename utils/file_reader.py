from radon.visitors import ComplexityVisitor
from radon.complexity import cc_visit
from code_complexity import call_Chat_gpt_for_time_and_space_complexity, convert_complexity_to_number, give_start_rating
import json

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



def get_cyclomitic_complexity(fun):
#   v = ComplexityVisitor.from_code(fun)
#   result = v.functions
#   print(result)
  return cc_visit(fun)

'''
# class Track:
    
@track_emissions(project_name="bigO(10**4)")
def cal_n(n):
    for i in range(n):
        x=[1, 54, 2, 5, 7]
        x.sort()

@track_emissions(project_name="bigO(10**4 log)")
def cal_nlogn(n):
    num=int(n*math.log(n,2))
    for i in range(num):
        x=[1,54,2]
        x.sort()

@track_emissions(project_name="bigO(n*n)")
def cal_n_n(n):
    for i in range(n):
        for i in range(n):
            x=[1,54,2]
            x.sort()

def bubbleSort(apne_numbers):
    
    n = len(apne_numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if apne_numbers[j] > apne_numbers[j + 1]:
                apne_numbers[j], apne_numbers[j + 1] = apne_numbers[j + 1], apne_numbers[j]



if __name__ == "__main__":
    print(math.log(10**8,2))
    # tracker.start()
    # cal_n(10**4)
    cal_nlogn(10**4)
    # tracker.stop()
'''


file = open('C:\Jatin\GreenSense\green_sense_flask\code_carbon\main.py', "r")
fun = file.read()
file.close()
# resp = call_Chat_gpt_for_time_and_space_complexity(fun)
# resp = json.loads(resp)


resp = {'cal_n': {'time_complexity': 'O(n)', 'space_complexity': 'O(1)'}, 'cal_nlogn': {'time_complexity': 'O(n log n)', 'space_complexity': 'O(1)'}, 'cal_n_n': {'time_complexity': 'O(n^2)', 'space_complexity': 'O(1)'}, 'bubbleSort': {'time_complexity': 'O(n^2)', 'space_complexity': 'O(1)'}}
cyclo_comp = get_cyclomitic_complexity(fun=fun)
# print(cyclo_comp)

for c in cyclo_comp:
    # print(c)
    name, comp = c.name, c.complexity
    resp[name]["cyclo_complexity"] = comp

for res in resp:
    code = resp[res]
    score = convert_complexity_to_number(code["time_complexity"])+convert_complexity_to_number(code["space_complexity"])
    resp[res]["score"] = score
    # print(score)

# Star Rating



print(resp)