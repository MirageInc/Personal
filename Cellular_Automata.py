from tkinter import *
import math
import time

M = Tk()

def relist(l):
    nl = [] # New list of [[thing, # of thing],...
    fl = [] # List of things already found.
    np = 0 # Cursor for how far previously looked
    finished = False
    while finished == False:
        for i in range(np, len(l)):
            if l[np] not in fl:
                break
            if np == len(l)-1:
                finished = True
                break
            else:
                np += 1
        nl.append([l[np], 0])
        fl.append(l[np])
        for i in range(1, len(l)):
            if l[i] == l[np]:
                nl[len(nl)-1][1] += 1
    del nl[len(nl)-1]
    nl[0][1] += 1
    return nl

#SCREEN CONSTANTS

leng = 500
width = 500

grid_l = 10
grid_w = 10

canvas = Canvas(M, width=leng, height=width)
canvas.pack()

#GRID

line_spacing = (int(leng/grid_l), int(width/grid_w))

for i in range(1, grid_l):
    canvas.create_line((line_spacing[0]*i, 0), (line_spacing[0]*i, leng))
for i in range(1, grid_w):
    canvas.create_line((0, line_spacing[1]*i), (width, line_spacing[1]*i))

grid = [[(i*line_spacing[0],j*line_spacing[1]) for j in range(0, grid_w)] for i in range(0, grid_l)]

def cell(x, y, col):
    canvas.create_polygon((grid[x][y],grid[x+1][y],grid[x+1][y+1],grid[x][y+1]),fill=col)

# AUTOMATON OBJECT

lcol = ["black","red","yellow","gold","orange","green","blue","navy","indigo","purple","violet"]

# nhood (Neighbourhood) consists of vectors, so (1,1) means current x+1 and current y+1.

# states is the number of different alive automaton states, where 1 denotes the states as alive, dead.

# lruleset (so called "Long Rule Set") generates the numerical equivalent of every situation (where each state in the neighbourhood is considered a digit base (states))
# so that they all default map to the "dead" state. Rules are inputted in the form (situation_number, state).

# qruleset (so called "Quick Rule Set") defines rules by saying that if a certain set of states appear in the neighbourhood with occurrence larger than
# or equal to some m and smaller than or equal to some n, where there can be individual n & m for each state mentioned. Rules are inputted in
# the form ((state_1, m_1, n_1), (state_2, m_2, n_2),...,(state_k, m_k, n_k))

# TO ADD:
# - draw() method, with frame_rate argument.

class Automaton:
    def __init__(self, states, nhood, rules=[], statecol=[], grid=[]):
        if states < 1:
            print("Invalid state number.")
        else:
            self.nhood = nhood
            self.states = states
            if len(lcol) <= states-1:
                print("Colours must specified for this number of states")
            if statecol == [] and len(lcol) > states-1:
                self.statecol = lcol[:states-1]
            self.lruleset = [0 for i in range(0, states**(states**len(nhood)))]
            self.qruleset = []
            for i in rules:
                if len(i) == 2 and type(i[0]) != tuple:
                    self.lruleset[i[0]] = i[1]
                if len(i) > 0 and type(i[0]) == tuple:
                    self.qruleset.append(i)
                    
                        
        if grid == []:
            self.grid = [[0 for i in range(0, grid_w)] for j in range(0, grid_l)]
        if self.nhood == "V":
            self.nhood = ((1,0),(-1,0),(0,1),(0,-1))
        if self.nhood == "M":
            self.nhood = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))

    def update(self):
        for x in range(0, grid_l):
            for y in range(0, grid_w):
                state_l = []
                state = ''
                for i in self.nhood:
                    coords = [(x+i[0])%grid_l,(y+i[1])%grid_w]
                    i_state = self.grid[(x+i[0])%grid_l][(y+i[1])%grid_w]
                    state_l.append(i_state)
                    state += str(i_state)
                state_l = relist(state_l)
                self.grid[x][y] = self.ruleset[int(state, self.states+1)]

    def draw(self):
        for x in range(0, grid_l-1):
            for y in range(0, grid_w-1):
                col = self.grid[x][y]-1
                if col > -1:
                    cell(x, y, self.statecol[col])

conway = Automaton(2, "M")
