# Bloch Sphere Intuition

Up to now, we’ve talked about qubits as arrows in an abstract space.

The Bloch sphere is what happens when we give that arrow a **geometric home**.

Not a metaphor.
An actual, precise picture.

---

## Why we need the Bloch sphere

A single qubit state has:
- two complex numbers
- one normalization rule
- one irrelevant global phase

That sounds messy.

The Bloch sphere compresses all of that into:
- one point
- on the surface of a sphere

Same information. Much better intuition.

---

## The sphere itself

Picture a unit sphere.

- north pole → |0⟩
- south pole → |1⟩

Every valid single-qubit state (ignoring global phase)
is a point on the **surface** of this sphere.

Not inside.
Not outside.
Exactly on the surface.

---

## Latitude = probability

If a state is closer to:
- north → higher chance of measuring 0
- south → higher chance of measuring 1

States on the equator give:
- 50% chance of 0
- 50% chance of 1

Probability is encoded as **latitude**.

---

## Longitude = phase

Now the important part people skip.

Points around the equator:
- all give the same measurement probabilities
- but behave differently under gates

That difference is **phase**.

Phase lives in the angle *around* the sphere.

This is why phase feels invisible until it suddenly isn’t.

---

## One qubit, two angles

Any single-qubit state can be written as:

|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ) sin(θ/2)|1⟩

You don’t need to memorize this.

Just remember:
- θ controls up vs down
- φ controls around-the-sphere rotation

That’s the entire Bloch sphere.

---

## What gates do on the sphere

Single-qubit gates are:
- rotations of the Bloch sphere

Examples:
- X gate → flips north ↔ south
- Z gate → spins around the vertical axis
- H gate → rotates between poles and equator

No mystery. Just rotations.

---

## Measurement revisited

Measurement does one brutal thing:
- it ignores longitude
- it keeps only north vs south

All phase information is destroyed.

That’s why measurement feels violent.

It is.

---

## Important limitation

The Bloch sphere works only for:
- one qubit
- pure states

The moment you add:
- entanglement
- noise
- mixed states

the picture breaks.

That’s not a bug.
That’s a warning.

---

## What to carry forward

When thinking about a single qubit:
- imagine a point on a sphere
- imagine gates as rotations
- imagine measurement as snapping to a pole

If a circuit confuses you,
try to picture the rotations.

---

Next up:

**`02-single-qubit-world/gates-h-x-z-s-t.md`**

Where we take the most common gates
and watch exactly how they move the arrow.
