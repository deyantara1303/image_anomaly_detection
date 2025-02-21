import subprocess
import argparse

DEFAULT_CONFIG = "configs/tools/benchmarks/benchmark_default.yaml"

def run_benchmark(config_path):
    """Runs the Anomalib benchmark using anomalib subcommand and benchmark_X.yaml path as command-line argument"""
    command = ["anomalib", "benchmark", "--config", config_path]
    try:
        subprocess.run(command, check=True)
        print(f"Benchmark completed successfully using config: {config_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Benchmark execution failed with exit code {e.returncode}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Anomalib benchmark Parser")
    parser.add_argument("config_path", nargs="?", default=DEFAULT_CONFIG, help="Path to the benchmark config file")
    args = parser.parse_args()
    run_benchmark(args.config_path)