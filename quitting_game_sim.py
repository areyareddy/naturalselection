import random 
len_list = 100 
inputs = [round(random.random()*100, 4) for _ in range(len_list)]
# You move through the list one by one, and you are tasked with picking exactly one value.
# Your score is the value you pick, and your goal is to maximize this score.
# You have no information about the list aside from its length,
# and after you pass on a value, you cannot retroactively pick it.
# What is the optimal strategy to maximize your score?

# Anything after 0 is banned from being checked. 

class oracle:
    def __init__(self, inputs, cur_index):
        self.inputs = inputs
        self.cur_index = cur_index
        self.score = 0

    def get_value(self):
        return self.inputs[self.cur_index]
    
    def increment_cur_index(self):
        if self.cur_index == len(self.inputs)-1:
            raise Exception("You have reached the end of the list, there are no more values to check.")
        self.cur_index += 1

    def pick_current(self):
        self.score += self.get_value()

    def print_score(self):
        print(f"Score: {self.score}")

oracle_instance = oracle(inputs, cur_index=0)

# Set optimal_strategy here: 
def optimal_strategy(oracle_instance, len_list):
    point = int(len_list // 2.718)
    max_seen_value = 0
    for _ in range(point):
        value = oracle_instance.get_value()
        if value > max_seen_value:
            max_seen_value = value
        oracle_instance.increment_cur_index() 
    
    while oracle_instance.cur_index < len_list-1:
        value = oracle_instance.get_value()
        if value > max_seen_value:
            oracle_instance.pick_current()
            return 
        oracle_instance.increment_cur_index()

    oracle_instance.pick_current()

def current_strategy(oracle_instance, len_list):
    for _ in range(len_list-1):
        oracle_instance.increment_cur_index()
    oracle_instance.pick_current()

# Validation section 
current_strategy(oracle_instance, len_list)
oracle_instance.print_score()
print(f"True maximum: {max(inputs)}")

wins = 0
test_runs = 10000
for _ in range(test_runs):
    inputs = [round(random.random()*100, 4) for _ in range(len_list)]
    oracle_instance = oracle(inputs, cur_index=0)
    current_strategy(oracle_instance, len_list)
    if oracle_instance.score == max(inputs):
        wins += 1
    
print(f"Accuracy: {round(wins/test_runs, 5) * 100}%")
