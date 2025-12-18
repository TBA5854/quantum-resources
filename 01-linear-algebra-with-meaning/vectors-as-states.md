# Vectors as States

Quantum computing starts making sense when you stop thinking in bits
and start thinking in **vectors**.

Not scary vectors.
Just arrows with rules.

---

## Why linear algebra shows up at all

If qubits were values, we’d use logic.

But qubits are **states that evolve smoothly**.

Smooth change is described by:
- vectors
- rotations
- projections

That’s linear algebra’s home turf.

---

## A state is a vector

A single qubit state is written as:

|ψ⟩ = a|0⟩ + b|1⟩

This does **not** mean:
- “a chance of 0 and b chance of 1”

It means:
- the state is a vector
- |0⟩ and |1⟩ are basis directions
- a and b are coordinates

Exactly like:
(3, 4) = 3x̂ + 4ŷ

---

## What are a and b really?

The numbers a and b are:
- complex numbers
- amplitudes, not probabilities
- allowed to be negative or imaginary

Probabilities come **later**.

First comes geometry.

---

## Normalization: why length matters

Quantum states must have length 1.

That means:

|a|² + |b|² = 1

This is not a rule added for fun.
It ensures probabilities add up to 1 after measurement.

Think:
- vector length → certainty budget
- measurement spends that budget

---

## Measurement is projection

When you measure:
- you pick a basis
- you project the vector onto that axis
- you square the length of the projection

That squared length is the probability.

Nothing mystical happened.
You just threw away information.

---

## Why complex numbers appear

Complex numbers let vectors:
- rotate smoothly
- encode phase
- interfere constructively or destructively

Without complex numbers,
quantum behavior collapses into classical probability.

They are not optional decoration.

---

## A tiny example

State:

|ψ⟩ = (1/√2)|0⟩ + (1/√2)|1⟩

This vector:
- is exactly halfway between |0⟩ and |1⟩
- gives 50% chance for each outcome
- still contains phase information we haven’t used yet

Two states can give the same probabilities
and still behave differently later.

That difference is **phase**.

---

## Important warning

If you think:
> “This is just probability vectors”

you will get stuck later.

Quantum states are **richer** than probability distributions.
They can cancel each other.

Probabilities can’t.

---

## What to keep in mind

Before touching circuits:
- states are vectors
- gates are matrices
- measurement is projection + information loss

Everything else is detail.

---

Next up:

**`complex-numbers-not-scary.md`**

Where we explain why `i` exists
without summoning trauma from math class.
rrrr