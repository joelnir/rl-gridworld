import numpy as np

from constants import *
from policy import *

class GridWorld():
    def __init__(self, height, width):
        self.q = np.zeros((height, width, 4))
        self.value = np.zeros((height, width,))
        self.reward = np.zeros((height, width))

        self.width = width
        self.height = height

        self.placing = False # If currently placing agent

        self.policy = random_policy
        self.learning_rate = DEFAULT_LR
        self.discount = DEFAULT_DISCOUNT # Discount factor

        self.start_pos = DEFAULT_START
        self.agent_pos = self.start_pos # y, x

        self.episodic = DEFAULT_EPISODIC
        self.train = DEFAULT_TRAIN

        self.epsilon = DEFAULT_EPSILON # Epsilon for epsilon-greedy policies

        # List of observers
        self.observers = []

    def step(self):
        # Take one step following current policy
        action_i = self.policy(self)
        pos_delta = ACTIONS[action_i]
        new_x = max(0, min(self.width-1, self.agent_pos[1] + pos_delta[1]))
        new_y = max(0, min(self.height-1, self.agent_pos[0] + pos_delta[0]))

        [old_y, old_x] = self.agent_pos

        moved = (old_y != new_y) or (old_x != new_x)
        old_reward = self.reward[old_y, old_x]

        # Reset if episodic and reward
        if self.episodic and (old_reward != 0):
            self.agent_pos = self.start_pos

            self.value[old_y, old_x] = self.reward[old_y, old_x]

        elif moved:
            if self.train:
                # Q-learning
                old_q = self.q[old_y, old_x, action_i]
                learned_val = old_reward + self.discount*self.value[new_y, new_x]
                self.q[old_y, old_x, action_i] = (1 - self.learning_rate)*old_q +\
                    self.learning_rate*learned_val

                # Update value
                self.value[old_y, old_x] = self.q[old_y, old_x].max()

            # Update position
            self.agent_pos = [new_y, new_x]

        self.update()

    def reset_position(self):
        self.agent_pos = self.start_pos
        self.update()

    def set_policy(self, new_policy):
        self.policy = new_policy

    def set_train(self, train):
        self.train = train

    def set_start_pos(self, y, x):
        self.start_pos = [y, x]
        self.reset_position()

    def set_policy(self, new_policy):
        self.policy = new_policy

    def set_epsilon(self, new_eps):
        self.epsilon = new_eps

    def set_placing(self, placing):
        self.placing = placing

    def set_learning_rate(self, new_lr):
        self.learning_rate = new_lr

    def set_discount(self, new_df):
        self.discount = new_df

    def set_episodic(self, episodic):
        self.episodic = episodic

    def update_reward(self, new_reward, y, x):
        self.reward[y, x] = new_reward
        self.update()

    def is_placing(self):
        return self.placing

    def get_value(self, y, x):
        return self.value[y, x]

    def get_reward(self, y, x):
        return self.reward[y, x]

    def get_size(self):
        return self.value.shape

    def get_position(self):
        return tuple(self.agent_pos)

    def get_max_value(self):
        return self.value.max()

    def get_min_value(self):
        return self.value.min()

    def add_observer(self, observer):
        self.observers.append(observer)

    # Tell all observers to repaint
    def update(self):
        for obs in self.observers:
            obs.repaint()

