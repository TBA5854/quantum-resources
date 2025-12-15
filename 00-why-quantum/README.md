# Why Quantum?

Before we talk about qubits, gates, or circuits, we need to answer a harder question:

**Why does quantum computing exist at all?**

Not “why is it cool”,  
not “why is it faster”,  
but **what actually breaks in classical computing**.

---

## The classical world works… until it doesn’t

Classical computers are unbelievably good at:
- counting
- following rules
- doing deterministic steps very fast

Everything a classical computer does can be reduced to:
- bits (0 or 1)
- logic gates
- sequences of steps

For most problems, this is enough.

For some problems, it is *provably not*.

---

## The problem is not speed — it’s scaling

When people say:
> “quantum is faster”

they usually mean:
> “quantum scales differently”

Some problems grow **exponentially** with input size:
- factoring large numbers
- simulating quantum systems
- searching unstructured spaces

Classical computers don’t fail suddenly.  
They fail *quietly*, by becoming uselessly slow.

---

## A concrete example (no quantum yet)

Imagine trying all possibilities:

- 10 bits → 1,024 possibilities  
- 50 bits → 1 quadrillion possibilities  
- 300 bits → more than atoms in the observable universe  

No clever CPU optimization fixes this.

This isn’t an engineering problem.  
It’s a **physics and mathematics problem**.

---

## Nature doesn’t compute classically

Here’s the key insight:

The universe itself does not simulate physics using bits.

Atoms don’t check “if / else”.  
Electrons don’t store booleans.

They evolve according to **linear algebra over complex numbers**.

So when we try to simulate nature with classical machines,
we’re forcing a quantum world to speak a classical language.

It works — but badly.

---

## The quantum idea (in one sentence)

Instead of forcing nature into bits,  
**let the computer behave like nature does**.

That’s it.  
No mysticism. No magic.

Quantum computing is not about being clever.  
It’s about **matching the problem’s physics**.

---

## What changes when we go quantum

When we stop pretending everything is a bit:
- states become vectors
- operations become rotations
- probabilities come from geometry, not counting

This gives us:
- interference (paths cancel or reinforce)
- superposition (not parallel worlds — geometry)
- entanglement (correlation beyond classical description)

We’ll unpack each of these slowly.

---

## What this section will cover

In this section, we will:
- see where classical intuition breaks
- build the mental model needed for qubits
- avoid equations until they become unavoidable

You don’t need to *believe* quantum computing works.

You just need to see **why classical thinking hits a wall**.

---

## One warning before continuing

If you’re looking for:
- instant speedups
- magical parallelism
- “quantum does everything at once”

This repo will disappoint you — on purpose.

What you’ll get instead is understanding.

And that turns out to be rarer.
