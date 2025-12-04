from abc import ABC, abstractmethod
import random

class NodeSelector(ABC):
    @abstractmethod
    def select_one(self, state, candidates):
        """
        :param state: GraphStateManager instance
        :param candidates: List[int] of candidate node IDs
        :return: int (selected node ID)
        """
        pass

class RandomSelector(NodeSelector):
    def select_one(self, state, candidates):
        return random.choice(candidates)

class MaxDegreeSelector(NodeSelector):
    def select_one(self, state, candidates):
        # Sort by degree descending (using NetworkX graph)
        # We assume candidates is not empty (handled by caller)
        return sorted(candidates, key=lambda n: state.graph.degree[n], reverse=True)[0]

# Placeholder for future logic
class WorstLocalNCPSelector(NodeSelector):
    def select_one(self, state, candidates):
        # TODO: Implement get_local_ncp in GraphStateManager later
        # return sorted(candidates, key=lambda n: state.get_local_ncp(n), reverse=True)[0]
        # For now, behaves like random to prevent crashing:
        return random.choice(candidates)