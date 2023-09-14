'''
    Author: Shazzam Austin
    Course: Scientific Computing with Python
    Project: Probability Calculator
    Website: FreeCodeCamp.org
    
    Date (Start): April 17, 2023
    Date (End): April 21, 2023
'''

import copy
import random
# Consider using the modules imported above.
''' References:
    - How to use **kwargs: https://stackoverflow.com/questions/60418497/how-do-i-use-kwargs-in-python-3-class-init-function
    - https://www.geeksforgeeks.org/python-random-module/
    - https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
'''

class Hat:
    
    def __init__(self, **color_balls_kwargs):
        self.contents = []
        #self.__dict__.update(color_balls_kwargs)

        # For each key, value pair in the color balls collection
        for key, val in color_balls_kwargs.items():
            # For each color in the collection, loop "i" times and add the color
            # to the contents "i" number of times.
            for i in range(val):
                self.contents.append(key)

    '''
        Remove balls at random from contents and return those balls as a list of strings. 
         
        The balls should not go back into the hat during the draw, similar to an 
        urn experiment without replacement. 
         
        If the number of balls to draw exceeds the available quantity, return all the balls.
    '''    
    def draw(self, num_of_balls_to_draw):
        removed_balls = [] # balls being removed at random from the hat
        #num_of_balls_in_hat = len(self.contents) # shows the colour balls and the number of them in the hat.

        # If the number of balls to draw exceeds the available quantity, return all the balls.
        if num_of_balls_to_draw > len(self.contents):
            return self.contents

        # Remove balls at random from contents a given number of times
        removed_balls = random.sample(self.contents, num_of_balls_to_draw)

        # For each ball that has been removed
        for ball in removed_balls:
            # Remove them from contents, to show that they have been removed.
            self.contents.remove(ball)
            
        return removed_balls



#############################################################################################################################

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M_count = 0
    # For-Loop for the actons to be taken for each experiment 
    # a specific number of times (i.e. num_experiments)
    for i in range(num_experiments):
        # Draw out the balls, and make copies of the expected balls and the hat.
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)

        colors_obtained = hat_copy.draw(num_balls_drawn)

        # For each color that was gotten
        for color in colors_obtained:
            # if the color is an expected ball
            if color in expected_balls_copy:
                # subtarct 1 from its value to show that a ball of the 
                # expected color was found. 
                expected_balls_copy[color] -= 1
                
        # if all drawn balls are in the array of expected balls
        if all(j <= 0 for j in expected_balls_copy.values()):
            # The experiment was a success
            M_count += 1

    prob = M_count / num_experiments

    return prob

