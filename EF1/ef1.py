
class EF1:
    def __init__(self, agents, items, vals):
        self.agents = agents
        self.items = items
        self.vals = vals
        self.allocation = dict()
        for agent in agents:
            self.allocation[agent] = []
        self.allocated = []
        

    def allocate(self):
        agent_idx = 0
        while len(self.vals[agent_idx]) > 0:
            agent = self.agents[agent_idx]
            max_item_idx = self.vals[agent_idx].index(max(self.vals[agent_idx]))
            self.allocation[agent].append(self.items[max_item_idx])
            self.items.pop(max_item_idx)
            for val in self.vals:
                val.pop(max_item_idx)
            agent_idx += 1  
            if agent_idx == len(self.agents):
                agent_idx = 0
        print(self.allocation)


ef1 = EF1(["a", "b"], ["book", "food","money"], [[0, 1,0.6], [1, 0,0.4]])
ef1.allocate()
