# Deutsch–Jozsa Algorithm

The Deutsch–Jozsa algorithm solves a problem
that almost never appears in real life.

That’s exactly why it’s useful.

Its job is not practicality.
Its job is to **teach interference**.

---

## The problem statement

You are given a function:

\[
f : \{0,1\}^n \rightarrow \{0,1\}
\]

You are promised that the function is either:

- **constant**  
  (same output for all inputs)

or

- **balanced**  
  (outputs 0 for half the inputs, 1 for the other half)

Your task:
determine which one it is.

---

## The classical cost

Classically:
- in the worst case
- you must check **more than half** the inputs

For \(n\) bits:
- inputs = \(2^n\)
- required checks ≈ \(2^{n-1} + 1\)

This is exponential.

---

## Why the promise matters

Without the promise:
- the problem is impossible to solve exactly

With the promise:
- structure exists
- interference can exploit it

Quantum speedups almost always rely on promises.

---

## The quantum idea (high level)

The algorithm works by:

1. Putting all inputs into superposition  
2. Querying the function **once**  
3. Letting phase interference happen  
4. Measuring a global property  

No input is examined individually.

---

## The oracle (important concept)

The function is accessed via an **oracle**.

The oracle:
- does not reveal values directly
- encodes output into **phase**

Specifically:
- inputs where \(f(x)=1\) get a phase flip

This is called **phase kickback**.

---

## Why phase, not bits?

If the oracle wrote results into bits:
- interference would not happen
- information would remain local

Phase affects **global behavior**.

That’s why it works.

---

## Interference does the test

After the oracle:
- constant functions produce uniform phase
- balanced functions produce mixed phase

A final set of Hadamard gates:
- causes constructive interference for constants
- causes destructive interference for balanced cases

The difference becomes visible.

---

## The measurement result

After measurement:

- all zeros → function is **constant**
- anything else → function is **balanced**

No probabilities.
No guessing.
Exact result.

---

## What actually gave the speedup

Not:
- superposition alone
- querying all inputs
- parallel evaluation

The speedup came from:
- encoding structure into phase
- interference collapsing a global property

That’s the pattern to remember.

---

## Why this algorithm matters

Deutsch–Jozsa teaches that:

- quantum algorithms don’t read answers
- they detect **structure**
- they use interference as a filter

Later algorithms reuse this idea
with real-world relevance.

---

## What to remember

- the oracle encodes information into phase
- interference extracts global properties
- measurement reads structure, not values

If you understand Deutsch–Jozsa,
Grover will feel natural.

---

## Next

**`grover.md`**

Where interference is no longer subtle,
and amplitudes are pushed around on purpose.
