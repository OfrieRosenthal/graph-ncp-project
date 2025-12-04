import os
import csv
import networkx as nx
from datetime import datetime

class ExperimentRunner:
    def __init__(self, manager, source_strat, target_strat, experiment_name="exp", snapshot_interval=None):
        """
        :param manager: The GraphStateManager instance.
        :param source_strat: Strategy for picking source nodes.
        :param target_strat: Strategy for picking target nodes.
        :param experiment_name: A label for the output folder.
        :param snapshot_interval: Integer. If set (e.g., 10), saves the graph every 10 steps. 
                                  If None, only saves when you call save_final_state().
        """
        self.manager = manager
        self.source_strat = source_strat
        self.target_strat = target_strat
        self.snapshot_interval = snapshot_interval
        
        # --- SETUP FOLDER STRUCTURE ---
        # Creates: results/20251204_153000_exp_name/
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.output_dir = os.path.join("../results", f"{timestamp}_{experiment_name}")
        self.snapshots_dir = os.path.join(self.output_dir, "graph_snapshots")
        
        os.makedirs(self.output_dir, exist_ok=True)
        if self.snapshot_interval:
            os.makedirs(self.snapshots_dir, exist_ok=True)
        
        # --- SETUP CSV LOG ---
        self.log_file = os.path.join(self.output_dir, "log.csv")
        self._init_log_file()
        
        print(f"Initialized Experiment. Results will be saved to: {self.output_dir}")

    def _init_log_file(self):
        """Creates the CSV file with headers."""
        headers = ["step", "source_node", "target_node", "success", "notes"]
        with open(self.log_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    def log_step(self, step_num, u, v, success, notes=""):
        """Appends a single row to the log."""
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([step_num, u, v, success, notes])

    def run_step(self, step_num):
        """
        Executes one iteration: Select Source -> Select Target -> Add Edge.
        """
        # 1. Select Source
        u = self.source_strat.select_source(self.manager)
        if u is None:
            self.log_step(step_num, -1, -1, False, "No Source Found")
            return False

        # 2. Select Target
        v = self.target_strat.select_target(self.manager, u)
        if v is None:
            self.log_step(step_num, u, -1, False, "No Target Found")
            return False

        # 3. Add Edge (Modify Memory)
        success = self.manager.add_edge(u, v)
        
        # 4. Log Result
        msg = "Added" if success else "Edge Exists"
        self.log_step(step_num, u, v, success, msg)
        print(f"Step {step_num}: {u} -> {v} ({msg})")

        # 5. Check Snapshot Interval
        # Only save if we actually changed the graph (success) and interval is set
        if success and self.snapshot_interval:
            if step_num > 0 and (step_num % self.snapshot_interval == 0):
                self._save_graph_file(f"graph_step_{step_num}.csv")
                
        return success

    def save_final_state(self):
        """Call this at the end of your notebook loop."""
        print("Saving final graph state...")
        self._save_graph_file("final_graph.csv")

    def _save_graph_file(self, filename):
        """Helper to dump the current graph memory to disk."""
        # Determine where to save based on if it is a snapshot or final
        if "final" in filename:
            path = os.path.join(self.output_dir, filename)
        else:
            path = os.path.join(self.snapshots_dir, filename)
            
        # Write as Space-Separated Edgelist (Best for SNAP/LGC)
        # data=False ensures we don't write weights, just node IDs
        nx.write_edgelist(self.manager.graph, path, data=False)
        print(f"  [IO] Saved graph to {path}")