from agent import Agent
from games.split_stacks_nim import SplitStacksNim


class HumanSplitStacksNimCliAgent(Agent):

    def move(self, game: SplitStacksNim, possible_steps=None):
        possible_steps = game.get_possible_next_steps()
        while True:
            choice = input(f'Your move (stack number/first part size)? State: {game.state}')
            stack, part = [int(el.strip()) for el in choice.split('/')]
            for current_stack, current_part in possible_steps:
                if stack == current_stack and part == current_part:
                    return (stack, part)

            print('Not available')
