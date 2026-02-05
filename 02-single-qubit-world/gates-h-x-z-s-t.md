# Single-Qubit Gates: H, X, Z, S, T

Single-qubit gates are the alphabet of quantum circuits.

They do not compute.
They **rotate**.

If you remember that, everything else falls into place.

---

## Gates are rotations

Every single-qubit gate:
- preserves vector length
- changes direction
- is reversible

This is why quantum gates are unitary.

No information is lost — until measurement.

---

## X gate (bit flip)

The X gate flips |0⟩ and |1⟩.

On the Bloch sphere:
- rotates 180° around the X-axis
- north ↔ south

This is the closest thing to a classical NOT.

But even here, phase matters.

---

## Z gate (phase flip)

The Z gate:
- leaves |0⟩ unchanged
- multiplies |1⟩ by −1

Measurement can’t see this.

But future gates can.

On the Bloch sphere:
- rotates around the Z-axis
- changes longitude, not latitude

This is your first real encounter with hidden phase.

---

## H gate (Hadamard)

The H gate creates and destroys balance.

- |0⟩ → equal superposition
- |1⟩ → equal superposition with opposite phase

On the Bloch sphere:
- rotates between poles and equator

H is not “making things quantum”.
It’s **changing the measurement basis**.

---

## S gate (√Z)

The S gate:
- applies a 90° phase rotation
- multiplies |1⟩ by i

You will not see its effect immediately.

You will see it when interference happens.

Think of S as a **quarter turn** around the Z-axis.

---

## T gate (√S)

The T gate:
- applies a 45° phase rotation
- multiplies |1⟩ by e^(iπ/4)

This gate looks innocent.
It is not.

T is what makes quantum computing hard to simulate classically.

This is where true quantum complexity starts.

---

## Why phase gates matter

X changes outcomes directly.
Z, S, T change **future possibilities**.

Most quantum algorithms are:
- long sequences of invisible phase changes
- followed by one dramatic interference step

If you ignore phase, algorithms look like nonsense.

---

## A quick comparison

- X → flips probabilities
- Z → flips phase
- H → mixes axes
- S/T → fine control of phase

Different tools. Same geometry.

---

## What to remember

When reading circuits:
- don’t ask “what value is this qubit?”
- ask “where is it pointing now?”

That question never lies.

---

Next up:

[**`02-single-qubit-world/measurement.md`**](./measurement.md)

Where we confront the most destructive operation in quantum computing.
