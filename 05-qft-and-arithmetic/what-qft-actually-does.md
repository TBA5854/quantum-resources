# What QFT Actually Does

The Quantum Fourier Transform is often introduced as a formula.

That’s unfortunate.

QFT is not a trick.
It is a **relabeling of information** —
from amplitudes into phase relationships.

Let’s build that intuition carefully.

---

## Start with something familiar

Classical Fourier Transform:
- takes a signal in time
- expresses it in frequencies

QFT does something similar, but subtler.

It takes:
- information stored in basis states
- and expresses it as **relative phase rotations**

---

## One qubit first

Consider a single qubit in state:

\[
|ψ⟩ = |0⟩
\]

Applying QFT to one qubit is just:
- a Hadamard gate

That’s it.

This already tells you something important:
QFT begins by creating superposition.

---

## Two qubits: where things get interesting

Now consider two qubits storing a number:

\[
|x⟩ = |x_1 x_0⟩
\]

Where:
- \(x_1\) is the most significant bit
- \(x_0\) is the least significant bit

After QFT:
- the state is no longer a simple basis vector
- information moves into phase rotations

---

## What happens conceptually

After QFT:
- each qubit is in superposition
- each qubit’s phase depends on less significant bits
- no qubit holds the full number alone

The number is now **distributed**.

---

## Controlled phase rotations

The core operation of QFT is:
- controlled phase shifts

Each bit contributes:
- a smaller and smaller rotation
- to higher-order qubits

This is why you see angles like:
- π
- π/2
- π/4
- π/8

They are binary fractions of a full turn.

---

## Why angles look weird

When you see:
- \(e^{2πi x / 2^n}\)

don’t panic.

It means:
- “rotate by x parts out of 2ⁿ”

That’s all.

QFT converts binary numbers into **rotational fractions**.

---

## No carries, no addition

Notice what’s missing:
- no carry bits
- no overflow logic
- no ripple effects

Phase handles addition naturally.

That’s the quiet power of QFT-based arithmetic.

---

## What QFT does NOT do

QFT does not:
- compute a value
- give you an answer directly
- replace classical arithmetic everywhere

It rearranges information so that
**interference can extract structure later**.

---

## Why inverse QFT matters

QFT by itself is rarely useful.

The usual pattern is:

1. Encode information into phase
2. Manipulate phase
3. Apply inverse QFT
4. Measure

The computation lives in steps 1–3.
Measurement just reveals it.

---

## What to remember

- QFT maps numbers → phases
- controlled rotations encode binary fractions
- inverse QFT turns phase back into values

If QFT feels passive,
that’s because it is.

It prepares the stage.

---

## Next

**`add-with-qft.md`**

Where we finally add numbers
without carrying a single bit.
