from abc import ABC, abstractmethod
from typing import Optional
from .selector import NodeSelector

class SourceStrategy(ABC):
    def __init__(self, selector: NodeSelector):
        self.selector = selector

    @abstractmethod
    def select_source(self, state) -> Optional[int]:
        pass

class MinNCPClusterSource(SourceStrategy):
    """Pool: Nodes in the cluster with the lowest Phi."""
    def select_source(self, state) -> Optional[int]:
        candidate_pool = state.get_cluster_with_min_ncp()
        
        if not candidate_pool:
            return None
            
        return self.selector.select_one(state, candidate_pool)

class GlobalGraphSource(SourceStrategy):
    """Pool: All nodes in the graph."""
    def select_source(self, state) -> Optional[int]:
        candidate_pool = list(state.graph.nodes())
        
        if not candidate_pool:
            return None
            
        return self.selector.select_one(state, candidate_pool)