# Adding Numbers with QFT

This is where things get unintuitive in a productive way.

We are going to add numbers:
- without carry bits
- without full adders
- without touching most qubits directly

The addition will happen **in phase**.

---

## The classical expectation

Classically, addition means:
- bit-by-bit sums
- carry propagation
- logic depth grows with bit-width

Quantum addition using QFT ignores all of this.

That’s not because it’s smarter.
It’s because phase behaves differently than bits.

---

## The setup

We will use:
- one register to hold a number |x⟩
- QFT applied to that register
- controlled phase rotations to add |y⟩
- inverse QFT to recover |x + y⟩

No carries will appear anywhere.

---

## Step 1: Encode x using QFT

Start with a register holding:

\[
|x⟩ = |x_{n-1} \dots x_1 x_0⟩
\]

Apply QFT.

After QFT:
- each qubit is in superposition
- each qubit’s phase represents a fraction of x
- lower bits influence higher bits via smaller rotations

The number is now stored **geometrically**.

---

## Step 2: Add y using phase shifts

To add a number y:
- we apply controlled phase rotations
- conditioned on bits of y
- to the QFT-transformed register

Each bit of y contributes:
- a rotation of size π, π/2, π/4, ...

This is binary addition in disguise.

---

## Why no carry is needed

In classical addition:
- bits overflow
- carries propagate

In phase addition:
- rotations simply add
- angles accumulate smoothly
- no overflow exists on a circle

Phase does what carry logic tries to approximate.

---

## A concrete intuition

Think of a clock:
- adding 1 hour rotates the hand
- adding another hour rotates it again
- no “carry” is required

QFT arithmetic treats numbers like angles.

---

## Step 3: Inverse QFT

After all phase shifts:
- the register encodes x + y in phase form

Apply inverse QFT.

This:
- converts phase back into basis states
- reconstructs the binary representation
- makes the sum measurable

Only now do we look.

---

## What actually did the work

Not the inverse QFT.
Not the measurement.

The real work happened when:
- phase rotations accumulated
- interference aligned amplitudes
- geometry replaced logic

---

## Limitations and reality check

QFT-based addition:
- is elegant
- is shallow in depth
- is sensitive to phase errors

This makes it:
- powerful in theory
- tricky on noisy hardware

That tradeoff matters.

---

## What to remember

- QFT stores numbers as rotations
- addition becomes phase accumulation
- inverse QFT reveals the result

No carries.
No branching.
Just geometry.

---

## Next

**`06-algorithms/README.md`**

Where we finally use all of this
to understand real quantum algorithms.
