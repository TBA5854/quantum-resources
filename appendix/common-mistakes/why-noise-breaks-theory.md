# Why Noise Breaks Theory

On paper, quantum algorithms are clean.
On simulators, they look perfect.
On real hardware, they often fall apart.

This is not because the theory is wrong.

It’s because **quantum information is fragile**.

---

## The ideal world vs the real one

Most explanations assume:
- perfect gates
- infinite coherence time
- exact rotations
- no environment

Real devices have:
- noisy gates
- decoherence
- crosstalk
- calibration drift

The gap matters.

---

## What noise actually does

Noise does not just:
- flip bits
- add randomness

Noise:
- destroys phase
- weakens interference
- turns quantum states into classical mixtures

This directly attacks the core of quantum advantage.

---

## Decoherence: the silent killer

Decoherence is:
- loss of phase coherence
- caused by interaction with the environment
- irreversible

You don’t see decoherence directly.
You see its consequences:
- washed-out interference
- flat probability distributions
- algorithms that “almost work”

---

## Why depth matters more than width (sometimes)

Every gate:
- takes time
- introduces error
- risks decoherence

Long circuits:
- accumulate phase errors
- lose entanglement
- drift toward classical behavior

A theoretically correct circuit
can be practically useless if it’s too deep.

---

## Why QFT suffers the most

QFT:
- relies on many small-angle rotations
- depends on precise phase relationships
- amplifies tiny errors

This makes it:
- powerful in theory
- fragile in practice

Approximate QFT exists for this reason.

---

## Error is not evenly distributed

Not all errors are equal:
- phase errors often hurt more than bit flips
- correlated errors are worse than random ones
- entangling gates are noisier than single-qubit gates

Understanding error types matters.

---

## Why simulators lie (a little)

Simulators often:
- assume perfect gates
- ignore noise
- preserve phase exactly

They are great for learning.
They are optimistic about reality.

Always remember:
> “Working in simulation is necessary, not sufficient.”

---

## The role of error correction

Quantum error correction:
- spreads information across many qubits
- detects and corrects errors
- is extremely expensive

Most near-term devices:
- cannot run full error correction
- rely on short, careful circuits

This defines what’s practical today.

---

## A practical mindset

When designing circuits, ask:
- can I reduce depth?
- can I remove small-angle gates?
- can I simplify interference?
- can I trade precision for robustness?

Elegant theory must bow to physics.

---

## What to remember

- noise attacks phase first
- decoherence kills interference
- depth accumulates error
- theory assumes perfection

Quantum algorithms are real.
Quantum hardware is unforgiving.

Bridging that gap is the field.

---

## Next

**`approximate-qft-why-it-works.md`**

Where we explain why throwing gates away
can actually make algorithms better.
