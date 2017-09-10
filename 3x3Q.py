##Author: Zarreen Naowal Reza
##Email: zarreen.naowal.reza@gmail.com
##Title: Using Q-learning algorithm for optimal path finding in a 3x3 grid 
##Used the concept explained by http://mnemstudio.org/path-finding-q-learning-tutorial.htm

import numpy as np
import time
start_time = time.time()

class Grid_Exploration:
    
  def __init__(self, gamma, start, goal):
      self.gamma = gamma
      self.start = start
      self.goal = goal

  def init_matrix(self):
      #initialize the reward matrix, grid no. 6 is a block, grid no. 7 is -100 and grid 8 is 100 (the goal state) 
     self.r = np.matrix('-1 0 -1 0 -1 -1 -1 -1 -1; 0 -1 0 -1 -1 -1 -1 -1 -1 ;'
                  '-1 0 -1 -1 -1 -1 -1 -100 -1; 0 -1 -1 -1 0 -1 -1 -1 -1;'
                  '-1 -1 -1 0 -1 0 -1 -1 -1; -1 -1 -1 -1 0 -1 -1 -1 100;'
                  '-1 -1 -1 -1 -1 -1 -1 -1 -1; -1 -1 -100 -1 -1 -1 -1 -1 0;'
                  '-1 -1 -1 -1 -1 0 -1 0 100')
     print(self.r)
     self.length = len(self.r)
     #initialize the q-matrix
     self.q = np.matrix ([[0]*self.length for x in range (self.length)])

  def update_Q_matrix(self):
    
    for episodes in range(10):
        current_state = self.start
          
        while True:
              
              action_table = []
              next_action_table = []
              all_actions = []
              if current_state == self.goal:
                  break
              for x in range(self.length):#negative reward means no path, thus we take only the non-negative values or the paths
                  if self.r[(current_state,x)] >=0:
                       action_table.append(x)
              
              action = np.random.choice(action_table) #choose a random action from all the available actions
              
              for y in range(self.length):#take all next possible actions from the chosen action
                  if self.r[(action,y)] >=0:
                       next_action_table.append(y)
              
              for index in range(len(next_action_table)):
                
                all_actions.append(self.q[(action,next_action_table[index])])
                #add all the rewards from q-matrix for all possible next actions
              
              next_max_q_action = max(all_actions) #take the action with the maximum q-value
              
              self.q[(current_state,action)] =  self.r[(current_state,action)] + (self.gamma * next_max_q_action)
              #Q(state, action) = Reward(state, action) + Gamma * Max[Q(next_state, all possible actions)]
              
              current_state = action

    print("Grid Converges! Converged grid is:")
    print(self.q)

  def find_optimal_path(self, start, goal):
    current_state = start
    goal_state = goal
    action_sequence = '-'
    
    while True:
      action_table = []
    
      action_sequence = action_sequence + str(current_state) + "-" #concatenate the path it took to reach the goal
      
      if current_state == goal_state:
        break
      
      for actions in range(self.length):
        action_table.append(self.q[(current_state,actions)])#take all action's q-values from current state 
            
      next_action_value = max(action_table)
      if(next_action_value == 0): #if max value is 0, that means there is no path towards goal from that state
        print("path is terminated, cannot reach goal state!")
        break
      next_action = action_table.index(next_action_value) #get the index of the max value in the action_table list
      
      current_state = next_action
      
      
    print("optimal path sequence: ",action_sequence)

rl = Grid_Exploration(0.8,0,8)
rl.init_matrix()  
rl.update_Q_matrix()
rl.find_optimal_path(2,8)
print("total execution time: %s seconds" % (time.time() - start_time))



















