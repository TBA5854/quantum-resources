# Statevector vs Measurement

Quantum beginners often feel like something is being hidden from them.

That feeling is correct.

Qiskit lets you see the quantum state **only until you measure**.
After that, most information is gone forever.

This file makes that loss explicit.

---

## Two ways to look at a circuit

There are exactly two perspectives:

### 1. Statevector view
- full quantum state
- complex amplitudes
- phase included
- **not accessible on real hardware**

### 2. Measurement view
- classical bitstrings
- probabilities only
- phase destroyed
- **the only thing hardware gives you**

These views are not interchangeable.

---

## The same circuit, two realities

Consider this circuit:

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.h(0)
```

Before measurement, the state is:

(|0⟩ + |1⟩) / √2

Now let’s look at it both ways.

---

## Statevector view

```python
from qiskit.quantum_info import Statevector

sv = Statevector.from_instruction(qc)
sv
```

You see:
- amplitudes
- relative phase
- full information

This is the **quantum truth** of the system.

---

## Measurement view

Now add measurement:

```python
qc.measure_all()
```

And simulate counts:

```python
from qiskit_aer import Aer
from qiskit import transpile

backend = Aer.get_backend("qasm_simulator")
job = backend.run(transpile(qc, backend), shots=1024)
job.result().get_counts()
```

You see:
- `0` and `1`
- roughly 50% each
- **no phase information**

---

## What was lost?

Everything except probabilities.

Specifically:
- relative phase → gone
- interference potential → gone
- reversibility → gone

Measurement does not *reveal* the state.

It **destroys it**.

---

## Why this distinction matters

Many quantum algorithms:
- look trivial when measured early
- only make sense in statevector form
- rely on phase buildup before collapse

If you only look at counts:
- quantum algorithms look random
- speedups look fake
- circuits look pointless

This is why intuition must come first.

---

## Deferred measurement principle

Any measurement that can be delayed:
- should be delayed
- exists only for classical output

Quantum computation happens **before** observation.

---

## What to remember

- statevectors carry meaning
- measurement destroys structure
- probabilities are shadows of geometry