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
                match s:
                    case 'R':
                        curr_pos = (x, y, newdir[d][1])
                    case 'L':
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
