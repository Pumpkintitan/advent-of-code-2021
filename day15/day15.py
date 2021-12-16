import heapq
file = open("day15.txt").read().split("\n")
board = []
for i in range(len(file)):
    board.append([])
    l = []
    for j in range(len(file[i])):
        l.append(int(file[i][j]))
    board[i] += l
    for k in range(4):
        nl = []
        for n in l:
            nl.append(n%9 + 1)
        board[i] += nl
        l = nl

for i in range(4 * len(board)):
    board.append([])
    for j in range(len(board[i])):
        board[-1].append(board[i][j]%9 + 1)

def path(previous, s): 
    '''
    `previous` is a dictionary chaining together the predecessor state that led to each state
    `s` will be None for the initial state
    otherwise, start from the last state `s` and recursively trace `previous` back to the initial state,
    constructing a list of states visited as we go
    '''
    if s is None:
        return []
    else:
        return path(previous, previous[s])+[s]

class Frontier_PQ:
    ''' frontier class for uniform search, ordered by path cost '''
    
    def __init__(self, start, cost):
        self.states = {}
        self.q = []
        self.add(start, cost)
        
    def add(self, state, cost):
        ''' push the new state and cost to get there onto the heap'''
        heapq.heappush(self.q, (cost, state))
        self.states[state] = cost

    def pop(self):
        (cost, state) = heapq.heappop(self.q)  # get cost of getting to explored state
        self.states.pop(state)    # and remove from frontier
        return (cost, state)

    def replace(self, state, cost):
        ''' found a cheaper route to `state`, replacing old cost with new `cost` '''
        self.states[state] = cost
        for i, (oldcost, oldstate) in enumerate(self.q):
            if oldstate==state and oldcost > cost:
                self.q[i] = (cost, state)
                heapq._siftdown(self.q, 0, i) # now i is posisbly out of order; restore
        return

def getnext(i,j):
    r = []
    if i > 0:
        r.append((i-1,j))
    if i < len(board[0]) - 1:
        r.append((i+1,j))
    if j > 0:
        r.append((i,j-1))
    if j < len(board) - 1:
        r.append((i,j+1))
    return r

v = {(0,0):None}
s = []
fq = Frontier_PQ((0,0), 0)
while len(fq.q) > 0:
    c,a = fq.pop()
    s.append(a)
    adj = getnext(a[0], a[1])
    for p in adj:
        if p not in v:
            if p not in fq.states:
                fq.add(p, board[p[0]][p[1]] + c)
                v[p] = a
            elif board[p[0]][p[1]] + c < fq.states[p]:
                fq.replace(p, board[p[0]][p[1]] + c)
                v[p] = a
    if a == (len(board)-1, len(board)-1):
        break

p = (len(board)-1, len(board)-1)
pa = []
tot = 0
while p != (0,0):
    tot += board[p[0]][p[1]]
    p = v[p]
# pp = path(v, (len(board)-1, len(board)-1))
# print(pp)
# tot = 0
# for p in pp:
#     tot += board[p[0]][p[1]]
print(tot)