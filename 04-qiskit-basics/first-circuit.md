# First Circuit (Without Measurement)

This is the smallest meaningful quantum circuit you can build.

No algorithms.  
No tricks.  
No measurement.

Just a qubit and a rotation.

---

## The goal of this circuit

We want to:
- create a single qubit
- apply one gate
- inspect the **statevector**

If you measure here, you miss the point.

---

## Step 1: create a circuit

In Qiskit, a circuit is a container.

One qubit.  
Zero classical bits.

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc
```

At this point:
- nothing has happened
- the qubit is in |0⟩
- the statevector is `[1, 0]`

---

## Step 2: apply a gate

Let’s apply a Hadamard gate.

```python
qc.h(0)
qc
```

Geometrically:
- the qubit moved from the north pole
- to the equator of the Bloch sphere

Mathematically:
- the state is (|0⟩ + |1⟩)/√2

---

## Step 3: inspect the statevector

We do **not** measure.

We simulate.

```python
from qiskit.quantum_info import Statevector

sv = Statevector.from_instruction(qc)
sv
```

You should see two amplitudes:
- equal magnitude
- possibly complex
- phase intact

This is the real quantum state.

---

## Step 4: what not to do yet

Do **not** do this:

```python
qc.measure_all()
```

If you measure now:
- the statevector collapses
- phase is lost
- the circuit becomes classical

We are not ready for that yet.

---

## Why this matters

Most beginner tutorials start with:
- build circuit
- measure
- look at counts

That hides:
- phase
- interference
- geometry

We are going the other way on purpose.

---

## A useful experiment

Try this:
- add a Z gate after H
- inspect the statevector again
- compare probabilities vs amplitudes

The probabilities will look the same.  
The state is not.

That difference will matter later.

---

## What to remember

- circuits describe transformations
- simulators reveal states
- measurement hides information

If you internalize this now, everything later becomes easier.

---

### Next file

**`statevector-vs-measurement.md`**

Where we directly compare  
“what the computer knows”  
vs  
“what you are allowed to see”.