# Common Mistakes

Quantum computing has a learning curve that looks smooth until you hit invisible walls.

This section catalogs those walls.

---

## Why this exists

Most quantum computing mistakes are not:
- typos
- syntax errors
- logic bugs you can print-debug

They are **conceptual traps**.

The code runs.  
The circuit compiles.  
The output looks reasonable.

But the computation never happened.

---

## How to read this

Each file addresses one specific failure mode:
- what the mistake looks like
- why it happens
- what actually breaks
- how to fix it

These are not theoretical exercises.  
They are patterns that appear in real code, repeatedly.

---

## The List

### Conceptual Traps

1. **`phase-is-not-visible.md`**  
   Why your circuit looks like it does nothing, until it suddenly does something.

2. **`why-quantum-is-not-just-linear-algebra.md`**  
   Why math alone is insufficient to understand quantum constraints.

### Destructive Operations

3. **`measurement-order-matters.md`**  
   Why you can't just peek at variables in the middle of a calculation.

4. **`reset-vs-uncompute.md`**  
   Why `reset` destroys your algorithm, and what to do instead.

5. **`classical-control-vs-quantum-control.md`**  
   The vital difference between `if` (after measure) and controlled gates (before measure).

### Resource Management

6. **`ancilla-qubits-are-not-free.md`**  
   Why you can't just keep adding qubits to solve problems.

7. **`approximate-qft-why-it-works.md`**  
   Why throwing away precision sometimes improves results.

### Debugging Mysteries

8. **`why-all-zeros.md`**  
   The most common "error" that isn't an error.

9. **`why-my-circuit-disappeared.md`**  
   Why the compiler deleted your code (it was right to do so).

### Reality Checks

10. **`why-noise-breaks-theory.md`**  
    Why testing on a simulator isn't enough.

---

## A pattern you'll notice

Almost every mistake follows the same structure:

1. Classical intuition suggests doing X
2. X compiles and runs
3. X silently destroys quantum behavior
4. Output looks wrong, but you can't see why

Quantum computing does not fail loudly.  
It fails silently.

These files exist to make those failures visible.

---

## When to read these

**Before writing code:**  
Skim the titles. Know what traps exist.

**When debugging:**  
If your circuit "should work" but doesn't, check here first.

**After you think you understand:**  
Read them anyway. You probably hit one without noticing.

---

## One more thing

If you finish this section and think:
> "I already knew all of this"

Then either:
- you are unusually careful
- or you haven't tested your code on real hardware yet

Most people discover these the hard way.

Consider this the shortcut.
