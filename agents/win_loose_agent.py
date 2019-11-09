from game import Game
from agent import Agent
from agents.random_agent import RandomAgent


class WinLooseAgent(Agent):

    def move(self, game: Game, possible_steps=None):
        winning_step, loosing_steps, draw_steps, possible_steps = self.check_next_step(game, possible_steps)
        if winning_step is not None:
            return winning_step

        steps_to_exclude = []
        for step in possible_steps:
            game_clone = game.copy_and_move(step)
            winning_step2, loosing_steps2, draw_steps2, possible_steps2 = self.check_next_step(game_clone)
            if len(loosing_steps2) > 0:
                steps_to_exclude.append(step)
            draw_steps += draw_steps2

        if len(steps_to_exclude) > 0:
            possible_steps = [step2 for step2 in possible_steps if step2 not in steps_to_exclude]

        if len(possible_steps) == 1:
            return possible_steps[0]
        elif len(possible_steps) > 1 and self.agent is not None:
            return self.agent.move(game, possible_steps)
        else:
            agent = RandomAgent(self.label)
            return agent.move(game)

    def check_next_step(self, game, possible_steps=None):
        if possible_steps is None:
            possible_steps = game.get_possible_next_steps()
        draw_steps = []
        loosing_steps = []
        for move in possible_steps:
            game_clone = game.copy_and_move(move)
            winner = game_clone.evaluate()
            if winner == self.label:
                return (move, None, None, possible_steps)
            elif winner == 'draw':
                draw_steps.append(move)
            elif winner is not None:
                loosing_steps.append(move)

        possible_steps = [step for step in possible_steps if step not in loosing_steps]
        return (None, loosing_steps, draw_steps, possible_steps)
