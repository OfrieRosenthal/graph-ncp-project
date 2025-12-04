import pandas as pd
import networkx as nx

class RealGraphStateManager:
    def __init__(self, graph: nx.Graph, ncp_dataframe: pd.DataFrame):
        self.graph = graph
        self.ncp_df = ncp_dataframe
        
        # Cache for quick access
        self.min_ncp_nodes = [] 
        
        # Parse data immediately
        self._update_state_from_dataframe()

    def _update_state_from_dataframe(self):
        """Parses 'phi' and 'nodes' columns from the DataFrame."""
        if self.ncp_df.empty:
            self.min_ncp_nodes = []
            return

        # 1. Find row with min 'phi'
        best_row_idx = self.ncp_df['phi'].idxmin()
        best_row = self.ncp_df.loc[best_row_idx]

        # 2. Parse 'nodes' string (space separated) into integers
        node_str = str(best_row['nodes']).strip()
        if node_str:
            self.min_ncp_nodes = [int(n) for n in node_str.split()]
        else:
            self.min_ncp_nodes = []
            
        # Debug print
        print(f"  [State] Min NCP Cluster Size: {len(self.min_ncp_nodes)} (Phi: {best_row['phi']:.4f})")

    # --- Methods for Strategies ---

    def get_cluster_with_min_ncp(self):
        return self.min_ncp_nodes

    def get_cluster_for_node(self, node_id):
        # If node is in the min cluster, return that cluster set so we can avoid it
        if node_id in self.min_ncp_nodes:
            return set(self.min_ncp_nodes)
        return set()

    def add_edge(self, u, v):
        if self.graph.has_edge(u, v):
            return False
        
        self.graph.add_edge(u, v)
        # Note: In a real loop, you would re-run NCP algorithms here 
        # and update self.ncp_df, then call self._update_state_from_dataframe()
        return True