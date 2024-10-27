from simulator import simulate_onboarding
import pandas as pd
from tabulate import tabulate

def main():
    customers_count = 100
    results_df, summary_stats = simulate_onboarding(customers_count)
    
    # Print results to terminal
    print(results_df.to_string(index=False))
    
    # Convert DataFrame to Markdown table
    md_table = tabulate(results_df, headers='keys', tablefmt='github', showindex=False)
    
    # Create the Markdown content
    md_content = f"# Onboarding Simulation Results\n\n"
    md_content += f"## Summary Statistics\n\n"
    md_content += f"{summary_stats}\n\n"
    md_content += f"## Detailed Module Results\n\n"
    md_content += f"{md_table}\n"
    
    # Write the Markdown content to a file
    with open('simulation_results.md', 'w') as f:
        f.write(md_content)
    
    print("\nResults have been saved to 'simulation_results.md'.")

if __name__ == "__main__":
    main()