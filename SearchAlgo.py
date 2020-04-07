# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:17:23 2019

@author: nisha
"""
import heapq
import math

def MinTarget(node,target):
    min_val=100000
    for i in target:
        diff_x=i[0]-node[0]
        diff_y=i[1]-node[1]
        min_val=min(min_val,math.sqrt(diff_x*diff_x+diff_y*diff_y))
    return min_val

def AStarAlgo():
    min_heap = []
    open_list = {}
    cost_list = {}
    visited_list = {}
    parent_list = {}
    heuristic_list = {}
    open_list[(Start_X,Start_Y)] = 1
    parent_list.update([((Start_X,Start_Y),(-1,-1))])
    cost_list.update([((Start_X,Start_Y),0)])
    found = 0
    Target=[]
    for i in range(N):
        xy = text[4+i+1].split()
        Target_X = int(xy[0])
        Target_Y = int(xy[1])
        Target.append((Target_X,Target_Y)) 
    heuristic_list.update([(start,MinTarget(start,Target))])
    heapq.heappush(min_heap,(heuristic_list[(Start_X,Start_Y)],(Start_X,Start_Y)))
    for i in range(N):
        Target_X = Target[i][0]
        Target_Y = Target[i][1]
        if(Target_X < 0 or Target_Y < 0 or Target_X >= W or Target_Y >= H):
            f.write("FAIL")
            if(i!=N-1):
                f.write("\n")
            continue
        found = 0
        if (Target_X,Target_Y) in visited_list:
            found = 1
        while((bool(min_heap)) and found==0):
            expand_node = heapq.heappop(min_heap)[1]
            if expand_node not in visited_list:
                if expand_node in open_list:
                    del open_list[expand_node]
                visited_list[expand_node]  = 1
            else:
                continue
            if(expand_node == (Target_X,Target_Y)):
                found = 1
            for a,b in coords:
                x_0 = expand_node[0]+a
                x_1 = expand_node[1]+b
                x_x = (x_0,x_1)
                if(x_0 >= 0 and x_1 >= 0 and x_0 < W and x_1 < H):
                    z_diff = abs(Terrain[x_0][x_1] - Terrain[expand_node[0]][expand_node[1]])
                    if(z_diff <= Max_Z):
                        x = cost_list[expand_node]+10+z_diff
                        if(abs(a)==1 and abs(b)==1):
                            x += 4
                        if x_x not in visited_list:
                            if (x_x not in open_list):
                                cost_list[x_x] = x
                                open_list[x_x] = 1
                                heuristic_list.update([(x_x,MinTarget(x_x,Target))])
                                parent_list.update([(x_x,expand_node)])
                                heapq.heappush(min_heap,(cost_list[x_x]+heuristic_list[x_x],x_x))
                            
                            elif (cost_list[x_x] > x):
                                cost_list[x_x] = x
                                parent_list.update([(x_x,expand_node)])
                                heapq.heappush(min_heap,(cost_list[x_x]+heuristic_list[x_x],x_x))
            
        if(found == 0):
            f.write("FAIL")
            if(i!=N-1):
                f.write("\n")
        else:
            x = Target_X
            y = Target_Y
            path = []
            path.append((x,y))
            while (x,y) != (-1,-1):
                parent = parent_list[(x,y)]
                x = parent[0]
                y = parent[1]
                if (x,y) != (-1,-1):
                    path.append(parent)
            path_len = len(path)-1
            for j in range(path_len,-1,-1):
                f.write(str(path[j][0])+","+str(path[j][1])+" ")
            if(i!=N-1):
                f.write("\n")
        
def ucs():
    min_heap = []
    open_list = {}
    cost_list = {}
    visited_list = {}
    parent_list = {}
    open_list[(Start_X,Start_Y)] = 1
    parent_list.update([((Start_X,Start_Y),(-1,-1))])
    cost_list.update([((Start_X,Start_Y),0)])
    found = 0
    heapq.heappush(min_heap,(0,(Start_X,Start_Y)))
    for i in range(N):
        xy = text[4+i+1].split()
        Target_X = int(xy[0])
        Target_Y = int(xy[1])
        if(Target_X < 0 or Target_Y < 0 or Target_X >= W or Target_Y >= H):
            f.write("FAIL")
            if(i!=N-1):
                f.write("\n")
            continue
        found = 0
        if (Target_X,Target_Y) in visited_list:
            found = 1
        while((bool(min_heap)) and found==0):
            expand_node = heapq.heappop(min_heap)[1]
            if expand_node not in visited_list:               
                if expand_node in open_list:
                    del open_list[expand_node]
                visited_list[expand_node]  = 1
            else:
                continue
            if(expand_node == (Target_X,Target_Y)):
                found = 1     
            for a,b in coords:
                x_0 = expand_node[0]+a
                x_1 = expand_node[1]+b
                x_x = (x_0,x_1)
                if(x_0 >= 0 and x_1 >= 0 and x_0 < W and x_1 < H):
                     if(abs(Terrain[x_0][x_1] - Terrain[expand_node[0]][expand_node[1]]) <= Max_Z):
                        x = cost_list[expand_node]+10
                        if(abs(a)==1 and abs(b)==1):
                            x += 4
                        if x_x not in visited_list:
                            if (x_x not in open_list):
                                cost_list[x_x] = x
                                open_list[x_x] = 1
                                parent_list.update([(x_x,expand_node)])
                                heapq.heappush(min_heap,(cost_list[x_x],x_x))
                            
                            elif (cost_list[x_x] > x):
                                cost_list[x_x] = x
                                parent_list.update([(x_x,expand_node)])
                                heapq.heappush(min_heap,(cost_list[x_x],x_x))
            
        if(found == 0):
            f.write("FAIL")
            if(i!=N-1):
                f.write("\n")
        else:
            x = Target_X
            y = Target_Y
            path = []
            path.append((x,y))
            while (x,y) != (-1,-1):
                parent = parent_list[(x,y)]
                x = parent[0]
                y = parent[1]
                if (x,y) != (-1,-1):
                    path.append(parent)
            path_len = len(path)-1
            for j in range(path_len,-1,-1):
                f.write(str(path[j][0])+","+str(path[j][1])+" ")
            if(i!=N-1):
                f.write("\n")


def bfs():
    min_heap = []
    open_list = {}
    cost_list = {}
    visited_list = {}
    parent_list = {}
    open_list[(Start_X,Start_Y)] = 1
    parent_list.update([(start,(-1,-1))])
    cost_list.update([(start,0)])
    found = 0
    heapq.heappush(min_heap,(0,start))
    for i in range(N):
        xy = text[4+i+1].split()
        Target_X = int(xy[0])
        Target_Y = int(xy[1])
        if(Target_X < 0 or Target_Y < 0 or Target_X >= W or Target_Y >= H):
            f.write("FAIL")
            if(i!=N-1):
                f.write("\n")
            continue
        found = 0
        if (Target_X,Target_Y) in visited_list:
            found = 1
        while((bool(min_heap)) and found==0):
            expand_node = heapq.heappop(min_heap)[1]
            if expand_node not in visited_list:
                if expand_node in open_list:
                    del open_list[expand_node]
                visited_list[expand_node]  = 1
            else:
                continue
            if(expand_node == (Target_X,Target_Y)):
                found = 1
            for a,b in coords:
                x_0 = expand_node[0]+a
                x_1 = expand_node[1]+b
                x_x = (x_0,x_1)
                if(x_0 >= 0 and x_1 >= 0 and x_0 < W and x_1 < H):
                    if(abs(Terrain[x_0][x_1] - Terrain[expand_node[0]][expand_node[1]]) <= Max_Z):
                        if (x_x not in open_list and x_x not in visited_list):
                            cost_list[x_x] = cost_list[expand_node]+1
                            open_list[x_x] = 1
                            parent_list.update([(x_x,expand_node)])
                            heapq.heappush(min_heap,(cost_list[x_x],x_x))
                        
        if(found == 0):
            f.write("FAIL")
            if(i!=N-1):
                f.write("\n")
        else:
            x = Target_X
            y = Target_Y
            path = []
            path.append((x,y))
            while (x,y) != (-1,-1):
                parent = parent_list[(x,y)]
                x = parent[0]
                y = parent[1]
                if (x,y) != (-1,-1):
                    path.append(parent)
            
            path_len = len(path)-1
            for j in range(path_len,-1,-1):
                f.write(str(path[j][0])+","+str(path[j][1])+" ")
            if(i!=N-1):
                f.write("\n")


path = "input.txt"
f= open("output.txt","w+")
coords ={(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)}
input_file = open(path,'r')
text = input_file.read().split("\n")
algo = text[0]
wh = text[1].split()
W = int(wh[0])
H = int(wh[1])
xy = text[2].split()
Start_X = int(xy[0])
Start_Y = int(xy[1])
start = (Start_X, Start_Y)
Max_Z = int(text[3])
N = int(text[4])

Terrain = []
for i in range(H):
    li = []
    ele = text[4+N+i+1].split()
    for j in range(W):
        li.append(int(ele[j]))
    Terrain.append(li)
Terrain = list(map(list, zip(*Terrain)))

if(Start_X < 0 or Start_Y < 0 or Start_X >= W or Start_Y >= H):
    for i in range(N):
        f.write("FAIL\n")
else:
    if(algo=="A*"):
        AStarAlgo()
    if(algo=="BFS"):
        bfs()
    if(algo=="UCS"):
        ucs()
f.close()