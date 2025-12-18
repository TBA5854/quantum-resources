# Reset vs Uncompute

At some point, you will want to “clear” a qubit.

Qiskit offers a tempting button:

```python
qc.reset(qubit)
```

This file explains why that button is dangerous.

---

## What `reset` actually does

`reset`:
- forces a qubit into |0⟩
- destroys all entanglement
- irreversibly erases information

It is **not** the inverse of anything.

It is measurement plus reinitialization.

---

## Why reset breaks quantum algorithms

Quantum algorithms rely on:
- coherence
- entanglement
- phase relationships

`reset` kills all three instantly.

If the qubit was entangled,
you just destroyed information elsewhere too.

---

## The common beginner instinct

“I used this qubit as workspace.
Now I want it clean.”

Classically, that’s fine.

Quantumly, that’s a trap.

---

## Uncompute: the correct approach

Instead of reset:
- reverse the computation
- return ancillas to |0⟩
- preserve global coherence

This is called **uncomputation**.

If you computed something with:
```
U
```

You clean it with:
```
U†
```

---

## Why uncompute works

Uncomputation:
- removes garbage
- preserves entanglement structure
- keeps phase intact
- is fully reversible

This is what quantum mechanics allows.

---

## A simple example

Bad approach:

```python
qc.cx(a, ancilla)
qc.reset(ancilla)
```

Good approach:

```python
qc.cx(a, ancilla)
qc.cx(a, ancilla)
```

Same classical effect.
Very different quantum meaning.

---

## When reset is acceptable

`reset` is okay when:
- you are done with the entire computation
- you do not care about coherence
- you are preparing fresh inputs

Usually:
- at the very beginning
- or after final measurement

Almost nowhere else.

---

## A warning about simulators

Simulators make `reset` look harmless.

Real hardware does not.

Noise + reset = chaos.

---

## How to recognize reset bugs

Symptoms:
- algorithm works without reset
- fails when reset is added
- outputs become random or trivial

This is not coincidence.

---

## A safe rule

If you are unsure:
> **Do not use reset.**

Use uncomputation until you fully understand the consequences.

---

## What to remember

- reset destroys information
- uncompute preserves structure
- reversibility is sacred
- ancillas must leave clean

Quantum computation is careful bookkeeping.

`reset` throws the books away.