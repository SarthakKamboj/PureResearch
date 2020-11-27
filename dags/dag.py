from __future__ import annotations
from typing import List, Dict

ResourceEval = Dict[str, int]
AgentAlloc = Dict[int, ResourceEval]


class Agent:
    def __init__(self, agent_id: int, evals: ResourceEval):
        self.id = agent_id
        self.resources_obtained: List[str] = []
        self.resource_evals = evals
        self.envy_of: List[Agent] = []
        self.envy_self: List[Agent] = []

    def add_resource(self, resource: str) -> None:
        self.resources_obtained.append(resource)

    def _get_relative_agent_bundle_sum(self, agent: Agent) -> int:
        agent_resources = agent.resources_obtained
        agent_bundle_relative_to_self = {
            r: self.resource_evals[r] for r in agent_resources}
        print(agent_bundle_relative_to_self)
        return sum(agent_bundle_relative_to_self.values())

    def eval_envyness_of_agent(self, other_agent: Agent) -> None:
        other_agent_sum = self._get_relative_agent_bundle_sum(other_agent)
        self_sum = self._get_relative_agent_bundle_sum(self)
        print(f'other agent: {other_agent_sum}, self: {self_sum}')
        if other_agent_sum > self_sum:
            self.envy_of.append(other_agent)


class DAG:
    def __init__(self, alloc: AgentAlloc) -> None:
        self.agents: List[Agent] = []
        for agent_id in alloc:
            new_agent = Agent(agent_id, alloc[agent_id])
            self.agents.append(new_agent)

    def add_item(self, item: string) -> None:
        return
