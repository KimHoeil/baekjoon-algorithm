from sys import stdin
n_people = int(stdin.readline())
sub_trees = [[] for _ in range (n_people)]


input_list = list(map(int, stdin.readline().split()))

# 트리의 뒤에서부터 리스트 순회
for i in range(len(input_list)-1, -1, -1):
    if len(sub_trees[i]) == 0:
        sub_trees[input_list[i]].append(0)
    else:
        sub_trees[i].sort(reverse=True)

        for j in range(len(sub_trees[i])):
            sub_trees[i][j] += (j+1)

        maxValue = max(sub_trees[i])
        sub_trees[input_list[i]].append(maxValue)

print(max(sub_trees[0]))


        
