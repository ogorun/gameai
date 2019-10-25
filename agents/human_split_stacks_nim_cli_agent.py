from agent import Agent
from game import Game
from games.split_stacks_nim import SplitStacksNim


class HumanSplitStacksNimCliAgent(Agent):

    def move(self, game: SplitStacksNim, possible_states=None):
        available_moves = game.get_possible_moves()
        while True:
            stacks_num = len(game.state)
            choice = input(f'Your move (stack number/first part size)? State: {game.state}')
            stack, part = [int(el.strip()) for el in choice.split('/')]
            for current_stack, current_part in available_moves:
                if stack == current_stack and part == current_part:
                    return game.move_to_state((stack, part))

            print('Not available')
