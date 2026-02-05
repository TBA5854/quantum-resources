# The Single Qubit World

This is where quantum computing starts to feel different.

A qubit is not:
- a bit that hasn't made up its mind
- a probability distribution
- two states happening at once

A qubit is a **point on a sphere**.

Understanding that changes everything.

---

## Why this section matters

Most beginner tutorials:
- show you circuits
- tell you to "just run them"
- measure everything immediately

Then you see outputs like `{'0': 512, '1': 512}`  
and think: "That's it?"

You missed the entire computation.

This section exists to show you what happens **before** measurement destroys it.

---

## The Bloch sphere is not a metaphor

When we say:
> "A qubit is a point on a sphere"

We do not mean:
- approximately
- sort of
- for visualization purposes

We mean exactly that.

Every valid single-qubit state (ignoring global phase)  
corresponds to exactly one point on the surface of a unit sphere.

This is geometry, not hand-waving.

---

## What you'll learn

### 1. **`bloch-sphere-intuition.md`**

You'll understand:
- why the north pole is |0⟩ and the south pole is |1⟩
- why latitude controls probability
- why longitude controls phase
- why phase feels invisible until it suddenly isn't

If measurement makes sense after this,  
you're ready to continue.

If it still feels mysterious,  
read it again — slowly.

### 2. **`gates-h-x-z-s-t.md`**

You'll understand:
- why gates are rotations, not operations
- why X flips probabilities but Z does not
- why H creates superposition (and what that actually means)
- why S and T gates look useless until interference happens

Gates do not compute values.  
They **move the arrow**.

That shift in thinking is critical.

### 3. **`measurement.md`**

You'll understand:
- why measurement is violent, not gentle
- why you cannot "peek" without destroying
- why measuring early ruins quantum algorithms
- why deferred measurement is not optional

Measurement is the most destructive operation in quantum computing.

Treat it accordingly.

---

## The key insight

Classical bits have two possible values: 0 or 1.

Qubits have two basis states: |0⟩ and |1⟩.

But a qubit state can point **anywhere on the sphere**.

That continuous space is where quantum power lives.

---

## Common confusion (addressed now)

**Q: "If a qubit is in superposition, doesn't that mean it's both 0 and 1?"**

No.

It means the qubit is pointing in a direction  
that is not aligned with the measurement axis.

When you measure, you project the state onto that axis.  
The closer the arrow was to |0⟩, the more likely you see 0.

This is geometry, not parallel universes.

---

## What to remember

- qubits are arrows on a sphere
- gates rotate the arrow
- measurement snaps it to a pole
- phase lives in the angle around the sphere

If you can visualize this,  
single-qubit circuits stop being mysterious.

---

## Next up

After this section, you'll move to **multiple qubits**,  
where the sphere metaphor breaks  
and entanglement becomes unavoidable.

But first, master the single qubit.

It's worth it.
