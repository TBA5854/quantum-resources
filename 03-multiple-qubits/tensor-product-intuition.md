# Tensor Products (Intuition First)

The moment we move from one qubit to two,
everything quietly becomes more dangerous.

Not because it’s harder math,
but because our intuition tries to cheat.

---

## One qubit vs two qubits

A single qubit state lives in a space with:
- 2 basis states: |0⟩, |1⟩

Two qubits do **not** live in:
- two separate spaces side by side

They live in a **new space** with:
- 4 basis states: |00⟩, |01⟩, |10⟩, |11⟩

This jump is the whole story.

---

## The tensor product in plain words

The tensor product means:

> “Every possibility of the first system combined  
> with every possibility of the second system.”

Not addition.
Not pairing.
Full combination.

That’s why size multiplies.

---

## Basis states are combinations

For two qubits, the basis is:

- |0⟩ ⊗ |0⟩ = |00⟩  
- |0⟩ ⊗ |1⟩ = |01⟩  
- |1⟩ ⊗ |0⟩ = |10⟩  
- |1⟩ ⊗ |1⟩ = |11⟩  

Nothing mystical happened.
We just listed all combinations.

---

## States grow exponentially

- 1 qubit → 2 amplitudes
- 2 qubits → 4 amplitudes
- 3 qubits → 8 amplitudes
- n qubits → 2ⁿ amplitudes

This is why classical simulation struggles.

The state itself explodes.

---

## Product states (the easy case)

If two qubits are independent, their state looks like:

(|ψ⟩ ⊗ |φ⟩)

Example:

(|0⟩ + |1⟩)/√2 ⊗ |0⟩  
= (|00⟩ + |10⟩)/√2

You can still talk about “each qubit”.

This comfort will not last.

---

## Why this is already dangerous

Even before entanglement:
- states are vectors in a 4D space
- rotations act on the whole space
- measurement affects joint outcomes

Thinking “per qubit” starts to break.

---

## A critical warning

Do not think:
> “each qubit has its own Bloch sphere”

That is false for multi-qubit systems.

There is **one state**, not many little ones.

---

## What to remember

Tensor products mean:
- spaces multiply
- possibilities combine
- intuition must scale carefully

If this feels abstract, that’s expected.
We are laying the floor, not decorating yet.

---

Next up:

[**`03-multiple-qubits/entanglement-is-not-magic.md`**](./entanglement-is-not-magic.md)

Where the phrase “cannot be written as a tensor product”
finally becomes meaningful.
