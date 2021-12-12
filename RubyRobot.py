# RubyRobot challenge: This was part of RatePay GMBH coding challenge.
# Objective: Prototypes of a squad of ruby robot should be developed.

# A ruby robot is a robot which is able to explore and interact with the outer world in  some degree
# by moving and exploring. We want to navigate our Ruby Robots through an open field and test its
# Geo cache mapping functionality.

# Our robots position is represented by a combination of an x and y co-ordinates and a letter
# representing one of the four cardinal compass points.The test field is divided up into a grid
# to simplify navigation. An example position might be 1, 1, N, meaning our robot is in the bottom
# left corner and facing North.

# In order to control the ruby robot,we can send a simple string of letters. The only valid possible
# letters are 'L', 'R' and 'M'. 'L' and 'R' makes our robot spin 90 degrees left or right respectively,
# without moving from its current position. 'M' means move forward one grid point and maintain the same
# heading. Assume that the square directly North from (x, y) is #(x, y+1).

# ++++++
# Input:
# ++++++
# The first line of input is the upper-right coordinates of the test field, the lower-left coordinates
# are assumed to be 0,0.

# The rest of the input is information to the robots that have been deployed. Each robot has two lines
# of input. The first line gives the robots position, and the second line is a series of instructions
# telling the robot how to explore the test field.

# The position is made up of two integers and a letter separated by spaces, corresponding to the x and y
# co-ordinates and the robot orientation.

# Each robot run will be finished sequentially, which means that the second robot run can not start to
# move until the first one has finished.

# +++++++++++
# Test Input:
# +++++++++++
# 10 10
# 2 3 E
# RMRMRLMRMRMRMR
# 5 4 W
# LMRMLMRMRLMRRM

# ++++++++++++++++
# Expected Output:
# ++++++++++++++++
# 1 2 W
# 3 2 E

# A dictionary that gives us new direction when the robot gets 'R' or 'L' instruction.
# Say for ex, if we instruct robot to turn 'L' and it is already facing 'N', then it will
# turn to 'W'.
newdir = {'N': ['W', 'E'], 'E': ['N', 'S'],
          'S': ['E', 'W'], 'W': ['S', 'N']}

# Instructions, this solution needs Python interpreter 3.10 since we are using new pattern matching
# feature of 3.10 (ie) MATCH statement. 
class RubyRobot:
    def instructRobot(self, fieldSize: tuple, initialpos: list[list], instructions: list):
        res = list()
        max_x, max_y = fieldSize
        curr_pos = initialpos

        for elem in range(0, len(initialpos)):
            curr_pos = initialpos[elem]
            curr_ins = instructions[elem]

            for s in curr_ins:
                x, y, d = curr_pos
                #print('Current direction of robot is:{0} {1} {2}'.format(x, y, d))
                match s:
                    case 'R':
                        #print('Current Direction:{0},Turning right,New direction is:{1}'.format(d, newdir[d][1]))
                        curr_pos = (x, y, newdir[d][1])
                    case 'L':
                        # print('Current Direction:{0},Turning left,New direction is:{1}'.format(d, newdir[d][0]))
                        curr_pos = (x, y, newdir[d][0])
                    case 'M':
                        if (d == 'N') & (y < max_y):
                            y += 1
                        elif (d == 'S') & (y > 0):
                            y -= 1
                        elif (d == 'E') & (x < max_x):
                            x += 1
                        elif (d == 'W') & (x > 0):
                            x -= 1
                        curr_pos = (x, y, d)
                    case _:
                        print('Command not recognized, no action taken by the robot')
            res.append(curr_pos)
        return res


rr = RubyRobot()
final_pos = rr.instructRobot((5, 7),
                             [[5, 0, 'N'], [0, 7, 'S']],
                             ['MMMMMMMMMMRMLLMLMMMMMR', 'MMMMMMMLMMMMM'])
print(final_pos)
