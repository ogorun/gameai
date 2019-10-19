from game import Game
from agent_decorator import AgentDecorator
from agents.random_agent import RandomAgent


class WinLooseDecorator(AgentDecorator):

    def move(self, game: Game, possible_steps=None):
        winning_step, loosing_steps, draw_steps, possible_steps = self.check_next_step(game, possible_steps)
        if winning_step is not None:
            return winning_step

        steps_to_exclude = []
        for state in possible_steps:
            game_clone = game.next_state_clone(state)
            winning_step2, loosing_steps2, draw_steps2, possible_steps2 = self.check_next_step(game_clone)
            if len(loosing_steps2) > 0:
                steps_to_exclude.append(state)
            draw_steps += draw_steps2

        if len(steps_to_exclude) > 0:
            possible_steps = [state2 for state2 in possible_steps if state2 not in steps_to_exclude]

        if len(possible_steps) == 1:
            return possible_steps[0]
        elif len(possible_steps) > 1:
            return self.agent.move(game, possible_steps)
        else:
            agent = RandomAgent(self.label)
            return agent.move(game)

    def check_next_step(self, game, possible_states=None):
        if possible_states is None:
            possible_states = game.get_possible_next_states()
        draw_steps = []
        loosing_steps = []
        for state in possible_states:
            game_clone = game.next_state_clone(state)
            winner = game_clone.evaluate()
            if winner == self.label:
                return (state, None, None, possible_states)
            elif winner == 'draw':
                draw_steps.append(state)
            elif winner is not None:
                loosing_steps.append(state)

        possible_states = [state for state in possible_states if state not in loosing_steps]
        return (None, loosing_steps, draw_steps, possible_states)

