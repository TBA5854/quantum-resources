# Measurement

Measurement is where quantum computing stops being gentle.

Everything before measurement is:
- reversible
- smooth
- information-preserving

Measurement breaks all three.

---

## What measurement is NOT

Measurement is not:
- “reading the value”
- “peeking at the qubit”
- “finding out what it really was”

There is no hidden classical value waiting inside.

---

## What measurement actually does

Measurement does two things at once:
1. chooses a basis
2. projects the state onto that basis

All other information is destroyed.

Not hidden.
Not stored.
Destroyed.

---

## A geometric picture

Before measurement:
- the qubit is a point on the Bloch sphere

After measurement:
- the qubit snaps to |0⟩ or |1⟩
- longitude (phase) is erased
- only north or south remains

This is not reversible.

---

## Why probabilities appear

Probabilities are not added by hand.

They come from:
- how aligned the state is with the measurement axis

Closer alignment → higher probability.

This is geometry pretending to be randomness.

---

## Measurement creates classical data

Once measured:
- the result is a classical bit
- it can be copied
- it can be logged
- it can be reused

The qubit itself is gone.

You cannot “measure and continue”.

---

## Why measurement ruins algorithms

Quantum algorithms work by:
- shaping amplitudes
- arranging interference
- canceling wrong paths

Measurement:
- freezes the system too early
- prevents interference
- collapses structure

Measure too soon, and the algorithm becomes classical.

---

## Deferred measurement principle

Many circuits measure at the end.

This is not tradition.
It’s survival.

As long as possible:
- don’t measure
- don’t observe
- don’t collapse

Let the geometry work.

---

## Measuring in other bases

Measurement doesn’t have to be in |0⟩ / |1⟩.

To measure in another basis:
- rotate the qubit
- measure normally

This is why H before measurement matters.

Measurement never changes.
The basis does.

---

## Important rule of thumb

If your circuit:
- “works” when you remove measurements
- breaks when you add them

That’s not a bug.
That’s quantum mechanics doing its job.

---

## What to remember

Measurement is:
- destructive
- final
- classical

Treat it like fire.
Useful.
Dangerous.
Never casual.

---

Next up:

**`03-multiple-qubits/tensor-product-intuition.md`**

Where one qubit becomes many,
and intuition starts to wobble.
