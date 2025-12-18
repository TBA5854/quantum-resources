# Qiskit Basics

Up to now, everything has lived in ideas and geometry.

This section is where we finally touch code.

The goal here is **not** to rush into circuits,
but to learn how Qiskit represents the things you already understand.

---

## A warning before we begin

Qiskit is a tool.

It does not explain quantum computing.
It assumes you already know what you’re doing.

If you treat Qiskit as the explanation,
everything will feel arbitrary.

So we won’t.

---

## Two worlds in Qiskit

Qiskit constantly switches between two worlds:

- the **quantum world** (states, gates, amplitudes)
- the **classical world** (bits, registers, measurement results)

Most beginner confusion comes from mixing these accidentally.

We will be explicit every time.

---

## Circuits are descriptions, not execution

A `QuantumCircuit` is:
- a blueprint
- a mathematical object
- a description of transformations

It is **not**:
- a running program
- a sequence of executed steps
- a live system

Nothing “happens” until simulation or execution.

---

## Statevector vs measurement

There are two ways to look at a circuit:

1. **Statevector view**
   - full amplitudes
   - phase included
   - no measurement

2. **Measurement view**
   - classical outcomes
   - probabilities only
   - phase destroyed

These are not equivalent.

We will start in statevector mode on purpose.

---

## Why simulators matter

Real quantum hardware:
- is noisy
- hides statevectors
- forces measurement early

Simulators let us:
- see amplitudes directly
- inspect phase
- build intuition safely

Learning without simulators is like learning physics blindfolded.

---

## What this section will cover

In this section, we will:
- build our first circuit
- inspect statevectors
- apply single-qubit gates
- delay measurement as long as possible

No algorithms yet.
No speedups.
Just mechanics.

---

## How to read the notebooks

Each notebook follows this rhythm:
- build a state
- apply one idea
- inspect the result
- explain what changed

If a cell feels mysterious,
stop there.
That’s the point.

---

## One rule to keep in mind

If your output is:
- all zeros
- empty
- “nothing happened”

It usually means:
- you measured too early
- or you looked at the wrong world

We will fix this repeatedly.

---

## What to remember

Qiskit is not quantum computing.

It is a language for **describing quantum geometry**.

If you keep that frame,
the syntax will stop feeling hostile.

---

Next up:

**`first-circuit.ipynb`**

Where we build the smallest possible circuit
and refuse to measure it.
