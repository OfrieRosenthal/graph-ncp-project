from abc import ABC, abstractmethod
from typing import Optional
from .selector import NodeSelector

class TargetStrategy(ABC):
    def __init__(self, selector: NodeSelector):
        self.selector = selector

    @abstractmethod
    def select_target(self, state, source_node) -> Optional[int]:
        pass

class OutsideClusterTarget(TargetStrategy):
    """Pool: Any node NOT in the source node's cluster."""
    def select_target(self, state, source_node) -> Optional[int]:
        source_cluster = state.get_cluster_for_node(source_node)
        all_nodes = set(state.graph.nodes())
        
        # Candidate pool = All nodes - Nodes in source's cluster
        candidate_pool = list(all_nodes - source_cluster)
        
        if not candidate_pool:
            return None
            
        return self.selector.select_one(state, candidate_pool)