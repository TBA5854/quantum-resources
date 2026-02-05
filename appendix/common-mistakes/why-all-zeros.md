# Why Is My Output All Zeros?

At some point, every quantum beginner sees this:

```
Counts: {'0000': 1024}
```

And thinks:
> “My circuit is broken.”

Most of the time, it isn’t.

This file exists to save you hours.

---

## The most important truth

“All zeros” is not an error.

It is a **symptom**.

The circuit is telling you something very specific —
you’re just looking in the wrong place.

---

## Cause 1: You measured too early

This is the most common reason.

If you measure:
- before interference
- before inverse QFT
- before amplitude amplification

Then all structure collapses.

### Symptom
- clean circuit
- sensible gates
- useless classical output

### Fix
- remove measurements
- inspect the statevector
- add measurement only at the very end

---

## Cause 2: You are looking at counts instead of state

Counts show:
- probabilities
- after collapse
- with phase destroyed

Many quantum states:
- differ only by phase
- look identical when measured

### Symptom
- changing gates changes nothing
- counts stay uniform or trivial

### Fix
Use:

```
Statevector.from_instruction(circuit)
```

If amplitudes differ, your circuit is working.

---

## Cause 3: You forgot the inverse QFT

QFT-based arithmetic requires:

1. QFT  
2. Phase manipulation  
3. **Inverse QFT**  
4. Measurement  

Skipping step 3 guarantees garbage output.

### Symptom
- arithmetic “does nothing”
- phase rotations appear pointless

### Fix
Always ask:
> “Did I bring phase back into the computational basis?”

---

## Cause 4: You reset or overwrite qubits

Operations like:
- `reset`
- reusing registers
- reinitializing inputs

can silently erase information.

### Symptom
- circuit looks correct
- output ignores earlier computation

### Fix
- avoid `reset` unless you fully understand it
- prefer uncomputation
- trace qubit lifetimes carefully

---

## Cause 5: Control logic never triggered

Controlled gates do nothing if:
- control qubit is always |0⟩
- control condition is wrong

### Symptom
- gates appear in circuit
- statevector shows no effect

### Fix
Inspect:
- control qubit initialization
- control basis
- classical vs quantum control confusion

---

## Cause 6: You assumed classical intuition

Examples:
- expecting intermediate results
- expecting visible change after phase gates
- expecting addition without inverse QFT

Quantum circuits often look useless
until the **very last step**.

This is not a flaw.
It is the design.

---

## A debugging checklist

When you see all zeros:

1. Remove all measurements  
2. Inspect the statevector  
3. Look for phase-only changes  
4. Check inverse operations  
5. Verify control qubits  
6. Add measurement last  

Do not skip step 2.

---

## The quiet truth

If your circuit outputs all zeros,
it usually means:

> “You destroyed the computation before looking at it.”

Quantum computing is fragile,
not broken.

---

## What to remember

- zeros are a diagnostic, not a failure  
- phase is invisible but powerful  
- measurement is destructive  
- statevectors are your friend  

If you stop fearing this output,
you start learning fast.

---

## Next

**`why-my-circuit-disappeared.md`**

Where we explain how a perfectly good circuit  
vanishes the moment you call `.inverse()`.