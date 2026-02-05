# Classical Control vs Quantum Control

At some point, every beginner asks:

> “Why can’t I just use an `if` statement?”

This file explains why that question quietly breaks quantum programs.

---

## Two very different ideas

There are **two kinds of control** in quantum computing:

1. **Quantum control**
   - controlled gates (CNOT, CZ, controlled-U)
   - control is a *qubit*
   - works without measurement

2. **Classical control**
   - `if` statements
   - control is a *measured bit*
   - requires collapse

They are not interchangeable.

---

## Quantum control (the good kind)

A controlled quantum gate means:

> “Apply this operation *if the control qubit is |1⟩*”

But crucially:
- the control qubit is **not measured**
- superposition is preserved
- entanglement is allowed

Example:

```python
qc.cx(control, target)
```

If the control is in superposition,
both paths happen coherently.

This is quantum logic.

---

## Classical control (the dangerous kind)

Classical control means:

> “Measure something, then decide what to do”

Example:

```python
if bit == 1:
    do_something()
```

This requires:
- measurement
- collapse
- loss of phase

Once you do this,
quantum interference is over.

---

## Why beginners mix them up

Because visually:

- “control qubit”
- “if condition”

sound similar.

But physically:
- one preserves superposition
- the other destroys it

The difference is fundamental.

---

## A common broken pattern

You want to do something like:

> “If this qubit is |1⟩, apply a gate”

So you write:

```python
qc.measure(q, c)
if c == 1:
    qc.x(target)
```

This does **not** mean what you think.

You just:
- collapsed the qubit
- converted quantum flow into classical flow
- destroyed coherence

---

## The correct quantum way

Use controlled gates:

```python
qc.cx(q, target)
```

or for arbitrary operations:

```python
controlled_gate = gate.control()
qc.append(controlled_gate, [q, target])
```

No measurement required.
No collapse.
Full interference preserved.

---

## When classical control is actually needed

Some algorithms require classical feedback:
- teleportation
- error correction
- adaptive measurements

In these cases:
- measurement result controls later gates
- collapse is intentional
- classical bits are part of the algorithm

If you don’t explicitly need this,
avoid classical control.

---

## A simple rule

If you want:
- superposition → use quantum control
- decision after observation → use classical control

Mixing them accidentally kills algorithms.

---

## Debugging tip

If your algorithm:
- works until you add an `if`
- suddenly outputs garbage
- loses quantum advantage

Check for accidental classical control.

---

## What to remember

- quantum control ≠ classical `if`
- measurement is the dividing line
- controlled gates preserve coherence
- classical control ends it

If you keep these separate,
your circuits stop betraying you.