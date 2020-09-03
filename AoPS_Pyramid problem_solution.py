f = open("pyramid_sample_input.txt","r")
input_data = f.readline()
input_data = input_data.split(" ")
target = int(input_data[-1])
pyramid = []
input_data = f.readline()
while input_data:
    path = list(map(int,input_data.split(",")))
    pyramid.append(path)
    input_data = f.readline()
n = len(pyramid)
res = []
def dfs(x,y,target,path):
    if pyramid[x][y] == target and len(path) == n-1:
        res.append(path)
        return
    elif pyramid[x][y] > target:
        return
    else:
        if pyramid[x][y] == 0:
            return
        if target % pyramid[x][y] == 0 and x+1 < n:
            nxt_target = target // pyramid[x][y]
            dfs(x+1,y,nxt_target,path+"L")
            if y + 1 < n:
                dfs(x+1,y+1,nxt_target,path+"R")
        else:
            return
dfs(0,0,target,"")
print(res[0])
f.close()
