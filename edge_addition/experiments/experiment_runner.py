class ExperimentRunner:
    def __init__(self, manager, source_strat, target_strat):
        self.manager = manager
        self.source_strat = source_strat
        self.target_strat = target_strat

    def run_step(self):
        # 1. Select Source
        u = self.source_strat.select_source(self.manager)
        if u is None:
            print("Error: Could not select a valid source node.")
            return False

        # 2. Select Target
        v = self.target_strat.select_target(self.manager, u)
        if v is None:
            print(f"Error: Could not select a valid target for source {u}.")
            return False

        print(f"Attempting to add edge: {u} <--> {v}")

        # 3. Apply Change
        success = self.manager.add_edge(u, v)
        if success:
            print("Success: Edge added.")
        else:
            print("Skipped: Edge already exists.")
            
        return success