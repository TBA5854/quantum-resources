# Quantum Algorithms (WIP)

Up to now, we’ve been preparing tools.

Qubits.
Phase.
Interference.
QFT.

This is where they finally get used.

Quantum algorithms are not faster because they “try everything”.
They are faster because they **shape interference**.

---

## A common myth

The myth:
> “Quantum computers do all possibilities in parallel.”

If that were true:
- measurement would give all answers
- brute force would be easy
- NP-complete problems would vanish

None of this happens.

Quantum algorithms succeed by:
- amplifying correct paths
- canceling incorrect ones

That’s interference, not parallelism.

---

## The recurring pattern

Most quantum algorithms follow the same structure:

1. Create superposition  
2. Encode structure using phase  
3. Interfere amplitudes  
4. Measure once  

The trick is step 2.

Everything else is setup or cleanup.

---

## What this section focuses on

We will not:
- chase speedups blindly
- dump full circuits immediately
- hide ideas behind diagrams

Instead, we will:
- understand *why* an algorithm works
- identify where quantum advantage enters
- connect circuits back to geometry

---

## Algorithms we will cover

Each algorithm is chosen for a reason:

- **Deutsch–Jozsa**  
  Shows how interference detects global structure

- **Grover’s Search**  
  Demonstrates amplitude amplification geometrically

- **Shor’s Algorithm**  
  Combines periodicity, phase estimation, and QFT

The goal is understanding, not implementation speed.

---

## A warning about expectations

Quantum algorithms:
- do not replace classical algorithms
- do not help every problem
- often require very specific structure

When they work, they work *spectacularly*.

When they don’t, they don’t help at all.

---

## How to read this section

For each algorithm:
- start with the classical problem
- identify what makes it hard
- see how phase encodes structure
- watch interference extract it

If you skip intuition, circuits will look magical.
We will not do that.

---

## What to remember

Quantum advantage comes from:
- geometry
- phase
- interference

Not from speed.
Not from parallel universes.

If you can point to where interference helps,
you understand the algorithm.

---

## Next

**`deutsch-jozsa.md`**

Where a problem with a useless practical purpose
teaches an extremely important lesson.
