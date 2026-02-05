# Why Did My Circuit Disappear?

You built a circuit.
It had gates.
It made sense.

Then you did one of these:

- `.inverse()`
- `.compose()`
- `.append(custom_gate)`
- transpiled it

And suddenly:
- the circuit looks empty
- gates vanished
- everything simplified away

This is not Qiskit being broken.

This is Qiskit being **too correct**.

---

## The uncomfortable truth

If a circuit disappears, it usually means:

> “You built something that mathematically does nothing.”

Quantum compilers are ruthless about removing identity operations.

---

## Cause 1: You inverted the entire computation

This is the most common cause.

Example pattern:

```python
qc.append(my_gate, qubits)
qc.append(my_gate.inverse(), qubits)
```

This is equivalent to:
- do something
- undo it perfectly

Net effect: **identity**

### Symptom
- circuit vanishes after optimization
- simulator shows no change
- statevector unchanged

### Fix
Ask yourself:
> “Did I actually want to uncompute everything?”

If yes → this is correct behavior.  
If no → you inverted too much.

---

## Cause 2: You inverted a gate with no side effects

Many gates:
- only change phase
- only act conditionally
- cancel when composed symmetrically

If phase is never converted back:
- the compiler removes it

### Symptom
- phase gates disappear
- arithmetic gates vanish
- QFT looks pointless

### Fix
Ensure:
- inverse QFT is applied later
- phase actually affects measurement

Phase without interference is invisible.

---

## Cause 3: You composed gates incorrectly

Common mistake:

```python
qc = QuantumCircuit(n)
qc.compose(subcircuit)
```

By default:
- `compose` returns a **new** circuit
- it does not modify in place

### Symptom
- circuit remains empty
- no errors thrown
- total confusion

### Fix

```python
qc = qc.compose(subcircuit)
```

or

```python
qc.compose(subcircuit, inplace=True)
```

---

## Cause 4: You appended a gate with no qubits

This happens when:
- register sizes mismatch
- wrong qubit list is passed
- slicing errors occur

### Symptom
- append succeeds
- nothing appears in the diagram

### Fix
Double-check:
- qubit indices
- register lengths
- ordering of arguments

Qiskit does not always scream when ignored.

---

## Cause 5: The transpiler optimized it away

Transpilers:
- remove redundant gates
- collapse inverse pairs
- simplify identities

This is their job.

### Symptom
- circuit looks fine before transpile
- becomes empty after transpile

### Fix
Temporarily disable optimization:

```python
transpile(qc, optimization_level=0)
```

If gates reappear, nothing was “wrong”.

---

## Cause 6: You expected visual confirmation of phase

Phase-only circuits:
- may look empty
- may collapse to identity visually
- still matter internally

### Symptom
- diagram empty
- statevector differs only by phase

### Fix
Inspect amplitudes, not diagrams.

Visualization hides phase.

---

## A sanity test

When confused, do this:

```python
sv_before = Statevector.from_instruction(qc)
sv_after  = Statevector.from_instruction(qc.inverse())
```

If:
- `sv_before == sv_after.conjugate()`  
then everything is working.

---

## The compiler is not your enemy

Qiskit assumes:
- math is sacred
- identities are useless
- silence means correctness

If something disappears,
it usually means it never mattered physically.

---

## What to remember

- inverses cancel perfectly
- phase without interference is invisible
- transpilers remove identities aggressively
- empty circuits are often correct

The compiler is not deleting your work.

It’s telling you the truth.