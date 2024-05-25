import os
import pickle
filepath = 'score.bin'

def input_scores():
    scores = []
    i = 1
    print(f'[점수입력]')
    while True:
        s = int(input(f'#{i}? '))
        if s<0:
            break
        scores.append(s)
        i +=1
    return scores

def get_average(lst):
    total = 0
    for s in lst:
        total +=s
    a = total / len(lst)
    return a

def save_data(scores,filepath):
    with open(filepath,'wb') as file:
        pickle.dump(scores,file)

def load_data(filepath):
    with open(filepath,'rb') as file:
        scores = pickle.load(file)
    return scores

scores = input_scores()
a = get_average(scores)
print(f'\n[점수출력]')
print(f'개인점수 : ',end='')
print(f'{scores}')
print(f'평균: {a:.2f}')

if os.path.exists(filepath):
    grade = load_data(filepath)
    print('\n[파일읽기]')
    print(f'\n[점수출력]')
    print(f'개인점수 : ',end='')
    print(f'{grade}')
    print(f'평균: {a:.2f}')
else:
    scores = []

save_data(scores,filepath)



    




