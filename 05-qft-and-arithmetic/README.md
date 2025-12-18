# QFT and Arithmetic

This is where quantum computing stops looking like rotations
and starts doing something that resembles computation.

The Quantum Fourier Transform (QFT) is not magic.
It is **phase organization**.

Arithmetic happens when phase is treated as information.

---

## Why QFT matters

Classical computers store numbers as:
- bit patterns
- explicit values

Quantum computers store numbers as:
- **relative phases**
- distributed across amplitudes

QFT is the bridge between:
- values ↔ phase
- counting ↔ interference

Without QFT, most famous quantum algorithms do not exist.

---

## A warning before we start

QFT is often taught as:
- a circuit to memorize
- a matrix to fear
- a black box to trust

We will do none of that.

If you don’t understand *why* QFT works,
you will never understand:
- Shor’s algorithm
- phase estimation
- quantum arithmetic

So we go slow.

---

## What QFT actually does (intuition first)

QFT takes:
- information encoded in amplitudes
- and moves it into **phase relationships**

Think of it as:
- spreading value information across rotations
- so interference can later extract structure

Nothing is calculated directly.
Everything is **arranged**.

---

## Phase as a number

After QFT:
- each qubit’s phase encodes a fraction
- higher qubits hold finer resolution
- lower qubits hold coarse structure

This is why:
- small phase errors matter
- controlled rotations appear everywhere

Arithmetic emerges from geometry.

---

## What this section will cover

In this section, we will:
- build QFT step by step
- see how addition works using phase
- understand why carry bits disappear
- see why inverse QFT recovers numbers

No shortcuts.
No “just accept this”.

---

## What we will avoid (on purpose)

We will not:
- dump the full QFT circuit immediately
- start with Shor’s algorithm
- hide phase behind diagrams only

Every gate must earn its place.

---

## A mindset shift you will need

Stop thinking:
> “Where is the number stored?”

Start thinking:
> “Where is the phase rotating?”

This shift is the hardest part.
Once it clicks, everything else simplifies.

---

## A recurring theme

In this section, you will notice:
- many gates that do nothing visibly
- measurements that look boring
- states that differ only by phase

That is expected.

QFT works **before** you look.

---

## What to remember going forward

- QFT rearranges information, it doesn’t compute directly
- phase is the real data
- interference is the extraction mechanism

If QFT feels useless at first,
you’re looking at the right time.

---

## Next

**`what-qft-actually-does.md`**

Where we build QFT from one qubit up
and watch phase turn into structure.
