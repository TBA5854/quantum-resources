import json
import re

notebooks = [
    "/home/tba/quantum/02-single-qubit-world/bloch-sphere.ipynb",
    "/home/tba/quantum/02-single-qubit-world/single-qubit-gates.ipynb"
]

def fix_notebook(nb_path):
    print(f"Fixing {nb_path}...")
    with open(nb_path, 'r') as f:
        nb = json.load(f)
    
    modified = False
    
    # 1. Add imports to the first code cell
    try:
        first_code_cell = next(cell for cell in nb['cells'] if cell['cell_type'] == 'code')
        source_lines = first_code_cell['source']
        
        has_bloch_vector = any('plot_bloch_vector' in line for line in source_lines)
        has_pauli = any('Pauli' in line for line in source_lines)
        
        new_imports = []
        if not has_bloch_vector:
            new_imports.append("from qiskit.visualization import plot_bloch_vector\n")
        if not has_pauli:
            new_imports.append("from qiskit.quantum_info import Pauli\n")
            
        if new_imports:
            first_code_cell['source'] = new_imports + source_lines
            modified = True
            print("  Added imports.")
    except StopIteration:
        print("  No code cells found.")
        return

    # 2. Fix plot_bloch_multivector calls
    # Regex to capture arguments: plot_bloch_multivector( arg1 , arg2 ... )
    # This is simple matching, assuming single line calls mostly
    call_pattern = re.compile(r'(\s*)plot_bloch_multivector\(([^)]+)\)')

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            lines = cell['source']
            for line in lines:
                match = call_pattern.search(line)
                if match:
                    indent = match.group(1)
                    args_str = match.group(2)
                    
                    # Split args by comma, detecting ax
                    args = [a.strip() for a in args_str.split(',')]
                    state_var = args[0]
                    
                    ax_var = None
                    if len(args) > 1:
                        # Check for positional or keyword arg for axis
                        # Usually axis is passed as 2nd arg (wrongly) or keyword
                        for arg in args[1:]:
                            if 'ax' in arg: # Heuristic: arg mentions 'ax'
                                if '=' in arg:
                                    # ax=ax1
                                    key, val = arg.split('=')
                                    if key.strip() == 'ax':
                                        ax_var = val.strip()
                                else:
                                    # just 'ax' passed positionally
                                    ax_var = arg.strip()
                    
                    if ax_var:
                        # Construct replacement
                        replacement = (
                            f"{indent}plot_bloch_vector([\n"
                            f"{indent}    {state_var}.expectation_value(Pauli('X')),\n"
                            f"{indent}    {state_var}.expectation_value(Pauli('Y')),\n"
                            f"{indent}    {state_var}.expectation_value(Pauli('Z'))\n"
                            f"{indent}], ax={ax_var})\n"
                        )
                        new_source.append(replacement)
                        modified = True
                        print(f"  Fixed call in line: {line.strip()}")
                    else:
                        # Valid usage (single argument), keep it or maybe replace if we want consistency?
                        # Plan said: "Replace problematic calls". Single arg calls work fine usually (creates new figure).
                        # But `bloch-sphere.ipynb` has correct single arg calls too?
                        # Wait, single arg calls create new figure. If user wants to reuse figure/ax, they must use plot_bloch_vector.
                        # The error happens when ax IS passed. So we only fix if ax is detected.
                        new_source.append(line)
                else:
                    new_source.append(line)
            cell['source'] = new_source

    if modified:
        with open(nb_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print("  Saved changes.")
    else:
        print("  No changes made.")

for nb_path in notebooks:
    fix_notebook(nb_path)
