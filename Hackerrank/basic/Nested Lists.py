if __name__ == '__main__':
    multi_List=[]   # multi list to store both names and scores
    score_list=[]   # to store scores only
    for _ in range(int(input())):
        name = input()
        score = float(input())
        multi_List+=[[name, score]] # adding a list to a list
        score_list+=[score]

    # here our score_list is ordered and sorted storing second element in 
    second_small =sorted(list(set(score_list)))[1]

    # sorting the multi list to match the second smallest element from the score list
    for a,c in sorted(multi_List):
        if second_small == c:
            print(a)