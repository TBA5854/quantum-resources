# Measurement Order Matters

In classical programs, you can print values whenever you want.

In quantum programs, **when** you measure is part of the algorithm.

Measure at the wrong time,
and the computation never happens.

---

## The quiet mistake

The mistake is not:
- measuring the wrong qubit

The mistake is:
- measuring the right qubit
- at the wrong time

Quantum algorithms are fragile about order.

---

## Measurement is not observation

Measurement is not:
- logging
- debugging
- checking progress

Measurement is:
- collapse
- information destruction
- irreversible change

Treat it like a commit you can’t undo.

---

## A common failure pattern

You want to:
1. compute something
2. inspect intermediate results
3. continue computation

So you add measurement in the middle.

The algorithm stops working.

This is expected.

---

## Why this breaks things

Before measurement:
- amplitudes interfere
- phase accumulates
- entanglement exists

After measurement:
- phase is gone
- entanglement collapses
- interference is impossible

The “rest of the circuit” is now classical.

---

## Mid-circuit measurement is special

Mid-circuit measurement:
- changes the computation model
- introduces classical control
- splits the timeline

Unless you *explicitly* want this,
it will break algorithms.

---

## Deferred measurement principle (final time)

If a measurement can be delayed,
it **must** be delayed.

Most quantum algorithms:
- do all quantum work first
- measure once
- extract a classical answer

This is not stylistic.
It is structural.

---

## Measuring ancillas too early

Ancilla qubits often:
- carry temporary phase
- are entangled
- influence interference

Measuring them early:
- leaks information
- destroys correlations
- ruins results elsewhere

Even if you “don’t care” about their value.

---

## A debugging trap

Beginners often add measurement to:
- see if something changed
- check if a gate worked

This always backfires.

Use:
- statevectors
- partial traces
- simulator inspection

Never measurement-as-debugging.

---

## When early measurement is intentional

Some algorithms **do** measure early:
- teleportation
- error correction
- adaptive circuits

In these cases:
- measurement outcome controls later gates
- classical feedback is essential

If you don’t see explicit classical control,
you probably shouldn’t be measuring.

---

## A safe mental model

Ask yourself:
> “Does the rest of my circuit still rely on phase or interference?”

If yes:
- measurement must wait

If no:
- measurement is safe

---

## What to remember

- measurement is destructive
- order is part of the algorithm
- early measurement kills interference
- debugging ≠ measuring

If your algorithm stopped working,
check *when* you measured — not just *what*.

---

## Next

**`classical-control-vs-quantum-control.md`**

Where we untangle the confusion between
“if this bit is 1”
and
“if this qubit is |1⟩”.
