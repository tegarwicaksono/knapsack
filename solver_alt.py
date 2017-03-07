#!/usr/bin/python
# -*- coding: utf-8 -*-

from recordclass import recordclass
from collections import deque
import heapq

Item = recordclass('Item', 'index value weight')
Node = recordclass('Node', 'level value weight items')
PQNode = recordclass('PQNode', 'level value weight bound items')

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
    def empty(self):
        if (len(self._queue) is 0):
            return True
        else:
            return False

    def length(self):
        return len(self._queue)
    
#def knapsack(capacity, items, int n):
def solve_it_branch_bound_breadth_first(input_data):
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))


    # sorting Item on basis of value per unit
    # weight.
    items = sorted(items,key=lambda Item: Item.weight/Item.value)    
    
    # make a queue for traversing the node
    v = Node(level = -1, value = 0, weight = 0, items = [])
    Q = deque([])
    Q.append(v)
    
    #One by one extract an item from decision tree
    #compute profit of all children of extracted item
    #and keep saving maxProfit
    maxValue = 0    
    bestItems = []
    
    while (len(Q) != 0):
        #Dequeue a node
        v = Q[0]

        Q.popleft()
        
        u = Node(level = None, weight = None, value = None, items = [])
        
        u.level = v.level + 1
        u.weight = v.weight + items[u.level].weight
        u.value = v.value + items[u.level].value
        u.items = list(v.items)       
        u.items.append(items[u.level].index)
        
        if (u.weight <= capacity and u.value > maxValue):
            maxValue = u.value
            bestItems = u.items
        
        bound_u = bound(u, capacity, item_count, items)
                
        if (bound_u > maxValue):
            Q.append(u)
                
        u = Node(level = None, weight = None, value = None, items = [])
        u.level = v.level + 1
        u.weight = v.weight
        u.value = v.value
        u.items = list(v.items)
      
        bound_u = bound(u, capacity, item_count, items)

        if (bound_u > maxValue):
            Q.append(u)
    
    taken = [0]*len(items)    
    for i in range(len(bestItems)):
        taken[bestItems[i]] = 1
    output_data = str(maxValue) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def solve_it_branch_bound_best_first(input_data):
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))


    # sorting Item on basis of value per unit
    # weight.
    items = sorted(items,key=lambda Item: Item.weight/Item.value)    
    
    # make a queue for traversing the node
    v = PQNode(level = -1, value = 0, weight = 0, bound = 0, items = [])
    v.bound = bound(v, capacity,item_count, items)
    Q = PriorityQueue()
    Q.push(v, v.bound)

    #One by one extract an item from decision tree
    #compute profit of all children of extracted item
    #and keep saving maxProfit
    maxValue = 0    
    bestItems = []
    
    while not Q.empty():
        #Dequeue a node
        v = Q.pop()
        if (v.bound > maxValue):
            u = PQNode(level = None, weight = None, value = None, bound = None, items = [])       
            u.level = v.level + 1
            u.weight = v.weight + items[u.level].weight
            u.value = v.value + items[u.level].value
            u.items = list(v.items)       
            u.items.append(items[u.level].index)
        
            if (u.weight <= capacity and u.value > maxValue):
                maxValue = u.value
                bestItems = u.items
        
            u.bound = bound(u, capacity, item_count, items)
                
            if (u.bound > maxValue):
                Q.push(u, u.bound)
                
            u = PQNode(level = None, weight = None, value = None, bound = None, items = [])
            u.level = v.level + 1
            u.weight = v.weight
            u.value = v.value
            u.items = list(v.items)
      
            u.bound = bound(u, capacity, item_count, items)

            if (u.bound > maxValue):
                Q.push(u, u.bound)
    
    taken = [0]*len(items)    
    for i in range(len(bestItems)):
        taken[bestItems[i]] = 1
    output_data = str(maxValue) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data
    
def bound(u, capacity, item_count, items):
    if (u.weight >= capacity):
        return 0
    else:
        result = u.value
        j = u.level + 1
        totweight = u.weight
        
        while (j < item_count and totweight + items[j].weight <= capacity):
            totweight = totweight + items[j].weight
            result = result + items[j].value
            j = j + 1
        
        k = j
        if (k <= item_count - 1):
            result = result + (capacity - totweight)*items[k].value/items[k].weight
        
        return result
        

def solve_it_default(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        print(line)
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    
    print(items)
    
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data
    
def solve_it_dynamic_programming(input_data):
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    #print("item_count = ", item_count, ", capacity = ", capacity)

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        #print(line)
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
        
  
#    for i in range(len(items)):
#        print("item = ", i, ", weight = ", items[i].weight, ", value = ", items[i].value )
        #print(items[i].weight)
        #print(items[i].value)
    
    obj = [[0 for y in range(0,item_count+1)] for x in range(0,capacity+1)]

            
    #for w in range(0, capacity):
    #    for i in range(0,item_count):
    #        print("capacity = ",capacity,", item_count = ", item_count,", obj[",w,"][", i, "] = ", obj[w][i])

    for i in range(1,item_count+1):
        for w in range(1,capacity+1):
            #print(obj[w][i-1])
            obj[w][i] = obj[w][i-1]
            if (items[i-1].weight <= w):
                val = obj[w-items[i-1].weight][i-1] + items[i-1].value
                if obj[w][i] < val:
                    obj[w][i] = val
            #print("w = ", w, ", i = ", i, ", obj[",w,"][",i,"] = ", obj[w][i])
    
    taken = [0]*len(items)

    curr_item = item_count-1
    curr_weight = capacity

    while (curr_item >= 0):
        #print("curr_item = ", curr_item, ", curr_weight = ", curr_weight, "obj[curr_weight][curr_item] = ", obj[curr_weight][curr_item+1])
        if obj[curr_weight][curr_item] != obj[curr_weight][curr_item + 1]:
            taken[curr_item] = 1
            curr_weight = curr_weight - items[curr_item].weight
        #print("taken[curr_item] = ", taken[curr_item])
        curr_item = curr_item - 1

    output_data = str(obj[capacity][item_count]) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data        
    #print("hello")    
 #   print(obj[0][capacity])
   
 
def solve_it(input_data):
    #return solve_it_branch_bound_breadth_first(input_data)
    #return solve_it_branch_bound_best_first(input_data)

    return solve_it_dynamic_programming(input_data)
    #return solve_it_default(input_data)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        #print("I'm here")
        #print(file_location)
        with open(file_location, 'r') as input_data_file:
            #print("in loop")
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

