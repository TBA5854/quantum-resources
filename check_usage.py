import json
import glob

notebooks = [
    "/home/tba/quantum/02-single-qubit-world/bloch-sphere.ipynb",
    "/home/tba/quantum/02-single-qubit-world/single-qubit-gates.ipynb",
    "/home/tba/quantum/04-qiskit-basics/first-circuit.ipynb",
    "/home/tba/quantum/04-qiskit-basics/statevector-vs-measurement.ipynb"
]

for nb_path in notebooks:
    print(f"Checking {nb_path}...")
    try:
        with open(nb_path, 'r') as f:
            nb = json.load(f)
        
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'code':
                source = "".join(cell['source'])
                if 'plot_bloch_multivector' in source:
                    print(f"--- Cell {i} ---")
                    print(source)
                    print("----------------")
    except Exception as e:
        print(f"Error reading {nb_path}: {e}")
