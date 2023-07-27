number = 6
all_natije = list()
for x in range(number):
    natije = input()
    natije_list = natije.split('-')
    all_natije.append(natije_list)
print(all_natije)
for [k,v] in all_natije[:3]:
    #sum_Iran = 0
    #sum_goal_moghabel = 0
    #sum_goal_Iran = sum_Iran + k
    #sum_goal_moghabel = sum_goal_moghabel + v
    #goal_difference =
    win_count_Ir = 0
    lose_count_Ir = 0
    draw_count_Ir = 0
    if k > v:
        win_count_Ir = win_count_Ir + 1
    elif k < v:
        lose_count_Ir = lose_count_Ir + 1
    elif k == v:
        draw_count_Ir = draw_count_Ir + 1






