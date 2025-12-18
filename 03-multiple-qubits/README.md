# Multiple Qubits

One qubit is geometry.

Two qubits are exponential explosion.

This is where classical simulation starts quietly dying.

---

## The uncomfortable jump

With one qubit:
- 2 basis states: |0⟩, |1⟩
- the Bloch sphere visualizes everything
- intuition mostly works

With two qubits:
- 4 basis states: |00⟩, |01⟩, |10⟩, |11⟩
- no simple visualization exists
- classical intuition starts lying

With three qubits:
- 8 basis states
- your laptop can still simulate this comfortably

With fifty qubits:
- 2⁵⁰ ≈ 10¹⁵ amplitudes
- more numbers than atoms in your body
- classical simulation becomes impossible

This jump is not gradual.  
It is exponential.

---

## The wrong mental model

Do **not** think:
> "Qubit A is in some state, qubit B is in some state."

For separable states, that works.

For entangled states, that model **breaks completely**.

There is no "state of qubit A" by itself.  
Only the joint state exists.

This is not philosophy.  
It is math refusing to factor.

---

## What you'll learn

### 1. **`tensor-product-intuition.md`**

You'll understand:
- why spaces multiply, not add
- why 2 qubits ≠ 2 separate Bloch spheres
- why "every possibility of A combined with every possibility of B" matters
- why exponential growth is unavoidable

The tensor product is not complicated math.  
It is just **full combination of possibilities**.

But that innocent idea has brutal consequences.

### 2. **`entanglement-is-not-magic.md`**

You'll understand:
- what "cannot be written as a product" actually means
- why entanglement is not faster-than-light communication
- why measurement outcomes are correlated
- why "spooky action" is just geometry

Entanglement sounds mystical.

It is not.

It is the failure of a specific algebraic factorization.

---

## The critical realization

When states are separable:
- you can describe each qubit independently
- classical intuition survives

When states are entangled:
- the system must be described as a whole
- no assignment of individual states reproduces the joint behavior
- quantum advantage becomes possible

Entanglement is not optional decoration.

It is **the** resource.

---

## Why this is hard

Your brain wants to think:
> "What is qubit 0 doing? What is qubit 1 doing?"

Quantum mechanics says:
> "Wrong question. The system has one state."

This shift feels unnatural.

It is.

But it is also correct.

---

## A warning about the Bloch sphere

The Bloch sphere works beautifully for:
- one qubit
- pure states
- no entanglement

The moment you have two qubits:
- the sphere picture breaks
- you need a 4D space
- visualization becomes useless

Do not try to force the Bloch sphere onto multi-qubit systems.

It will lie to you.

---

## What to remember

- tensor products mean full combination
- entanglement means factorization fails
- no Bloch sphere for multiple qubits
- the state is joint, not individual

If you accept that the system is one unified object,  
entanglement stops feeling mystical.

---

## Next up

After this section, you'll move to **Qiskit**,  
where you'll finally write actual circuits.

But the geometry you learned here  
will be what makes those circuits make sense.
