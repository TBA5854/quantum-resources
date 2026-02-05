# What a Qubit Really Is

A qubit is usually introduced with this sentence:

> “A qubit can be 0 and 1 at the same time.”

This sentence causes more damage than help.

Let’s replace it with something better.

---

## Start with a classical bit

A classical bit is simple:
- it is either 0 or 1
- at any moment, it has a definite value
- uncertainty comes from *us*, not the bit

Even if we don’t know the value, the bit knows.

---

## A qubit is not an uncertain bit

A qubit is **not**:
- a bit we haven’t measured yet
- a probability distribution over 0 and 1
- a coin flip waiting to land

A qubit has a **state**, not a value.

That state lives in mathematics, not in a register.

---

## The right mental model: an arrow

Think of a qubit as an **arrow**.

- the arrow lives in a 2D complex space
- its direction fully defines the qubit
- measurement asks a specific question about that direction

The qubit is always pointing *somewhere*.

---

## Basis states are just reference directions

We give special names to two directions:
- |0⟩
- |1⟩

These are not “the only states”.
They are just **reference axes**, like north and south.

Most qubit states point somewhere in between.

---

## Superposition is geometry, not magic

When we say a qubit is in a superposition:
- we do **not** mean it is both values
- we mean its arrow is not aligned with the measurement axis

Measurement projects the arrow onto that axis.

The probabilities come from angles, not parallel worlds.

---

## Why probabilities appear

When you measure a qubit:
- you choose a basis
- you ask a yes/no question
- the arrow collapses onto one direction

The closer the arrow was to |0⟩,
the more likely you see 0.

This is geometry pretending to be randomness.

---

## What makes qubits special

Two things:
- **phase** (direction around the axis)
- **interference** (directions can cancel)

Classical bits have neither.

This is where quantum power actually lives.

We will come back to this again and again.

---

## What this means practically

Before touching Qiskit, remember:

- a qubit is a vector
- gates rotate vectors
- measurement throws information away

If you forget this, circuits will feel like spells.

If you remember this, circuits start to feel mechanical.

---

## One promise

Nothing in quantum computing will contradict this model.

It will get richer.
It will get more abstract.

But it will never stop being **geometry under pressure**.

---

Next up:

[**`01-linear-algebra-with-meaning/vectors-as-states.md`**](../01-linear-algebra-with-meaning/vectors-as-states.md)

This is where we connect arrows to math — carefully, and without panic.
