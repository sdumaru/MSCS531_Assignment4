import os

# Path to the m5out folder and stats.txt file
STATS_FILE_PATH = 'm5out/stats.txt'

def parse_stats(file_path):
    """Parse the stats.txt file and extract relevant performance metrics."""
    metrics = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Skip comments or empty lines
                if line.startswith("#") or line.strip() == "":
                    continue
                
                # Extract metrics based on their key
                if 'system.cpu.cpi' in line:
                    metrics['CPI'] = float(line.split()[1])
                elif 'system.cpu.commitStats0.numInsts ' in line:
                    metrics['commit_insts'] = int(line.split()[1])
                elif 'system.cpu.numCycles' in line:
                    metrics['num_cycles'] = int(line.split()[1])
                elif 'system.cpu.ipc' in line:
                    metrics['IPC'] = float(line.split()[1])
                elif 'system.cpu.branchPred.committed::total' in line:
                    metrics['branch_predicted'] = int(line.split()[1])
                elif 'system.cpu.branchPred.mispredicted::total' in line: 
                    metrics['branch_mispredicted'] = int(line.split()[1])

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None
    
    return metrics

def main():
    # Parse stats.txt and extract metrics
    stats = parse_stats(STATS_FILE_PATH)
    
    if stats is None:
        print("Error: Unable to parse stats.txt")
        return
    
    commit_insts = stats.get('commit_insts', 0)
    num_cycles = stats.get('num_cycles', 0)
    ipc = stats.get('IPC', 0)
    cpi = stats.get('CPI', 0)
    predicted_branches = stats.get('branch_predicted', 0)
    mispredicted_branches = stats.get('branch_mispredicted', 0)
    
    # Display the metrics
    print(f"Total Cycles: {num_cycles}")
    print(f"Total Committed Instructions: {commit_insts}")
    print(f"Instruction Throughput (IPC): {ipc:.5f} Instructions/Cycle")
    print(f"Average Instruction Latency (CPI): {cpi:.2f} Cycles/Instruction")
    print(f"Predicted Branches: {predicted_branches}")
    print(f"Mispredicted Branches: {mispredicted_branches}")

if __name__ == "__main__":
    main()
