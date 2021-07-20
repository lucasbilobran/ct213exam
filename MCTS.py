## Monte Carlos Tree Search Class

class NodeMCTS:
    def __init__(self, state, nnet, is_root=False, parent=None):
        # self.edge = {n(s, a), q(s, a), p(s, a) = [], node = None}
        self.is_root = is_root
        self.parent = parent
        self.state = state
        self.selected_action = None

    def select(self):

    def expand(self):

    def backup(self):



class MCTS:
    def __init__(self, state):
        root = NodeMCTS(state, True)

    def play(self, temperature):
        s = root(state)
