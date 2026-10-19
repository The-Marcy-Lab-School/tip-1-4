# Conditionals 2: Check All, or First Match

**Time:** 77 minutes

**Files in this repo**

| File                     | Used in           |
| ------------------------ | ----------------- |
| `review.py`              | Review            |
| `what_to_wear.py`        | Parts 1–3         |
| `movie_night.py` (empty) | Part 4            |
| `snow_day.py`            | Independent check |

## How this activity works

You'll predict what code does, run it, figure out why, change it, and then build something of your own. Wrong predictions are expected. They show you exactly which idea to look at next.

### When you're stuck

Raise your hand when either of these is true:

- You've been stuck on one step for **5 minutes**, or
- You've tried **two different things** and neither worked.

Look for the 🙋 symbol in this guide. It marks the places where fellows most often get stuck, and asking for help there is the right move.

**When you ask for help, come with:**

1. The line of code you're stuck on
2. What you predicted
3. What actually happened
4. What you've tried so far

The ✅ symbol marks a checkpoint where you show an instructor your work before moving on.

---

## The big ideas (come back to these tables)

### Review: you've seen these before

| #   | Idea                                                                                                                                                                              |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| R1  | A block runs only if its condition is true at the moment Python reaches it.                                                                                                       |
| R2  | In one chain (`if` / `elif` / `else`), Python checks top to bottom and runs only the first block whose condition is true. The rest of the chain is skipped without being checked. |
| R3  | When conditions overlap, order decides the result. Start with the narrowest condition and move to broader ones.                                                                   |
| R4  | `else` runs when none of the conditions before it in its chain were true.                                                                                                         |

### Core: today's focus

| #   | Idea                                                                                                                                                                             | Try it                                                                 |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1   | Separate `if`s are each checked on their own, so any number of them can run: none, one, or all.                                                                                  | Part 1                                                                 |
| 2   | Separate `if`s are "check all that apply." A chain is "first true condition wins." Python doesn't know what you want, so you have to be explicit about what "the best match" is. | Part 1                                                                 |
| 3   | `return` ends the function immediately, so `if`s that each `return` act like a chain.                                                                                            | Part 3, exercise 3                                                     |
| 4   | Python counts zero, empty values, and `None` as false and everything else as true, in a condition or with `bool()`.                                                              | In the REPL: `bool(0)`, `bool("")`, `bool("no")`, `bool(None)`         |
| 5   | Each side of `and` / `or` is judged on its own. A bare value on one side is judged by whether it's truthy or falsy.                                                              | In the REPL: `if False or "no": print("runs")`                         |
| 6   | Comparisons come first, then `not`, then `and`, then `or`. Parentheses override this order.                                                                                      | In the REPL: `True or True and False`, then `(True or True) and False` |

### Extension: explore if you have time

| #   | Idea                                                                                                                      |
| --- | ------------------------------------------------------------------------------------------------------------------------- |
| E1  | Conditions that read like English aren't run like English. `drink == "tea" or "coffee"` doesn't mean what it sounds like. |

## Habits for today

**Coding habit:** Before you write conditions that overlap, decide what the task is. If the task is "check all that apply," use separate `if`s. If the task needs one answer, use a chain, or `if`s that each `return`, and put the narrowest condition first. Compare explicitly (`rain_chance >= 50`) unless you really mean "anything that isn't zero or empty."

**Working habit: Test the edges.**

- Every condition has a boundary: the value where it switches from true to false. For `temp > 75`, the boundary is between 75 and 76.
- Test one value just inside the boundary and one value just outside it.
- Most condition bugs live at the boundary, so a test far from the boundary (like `temp = 20`) can pass while the program is still wrong.

---

## Review (12 minutes)

Open `review.py`, which has the `is_it_hot` code. Answer each question as a comment in the space provided. When a question asks you to run something, predict first.

```python
def is_it_hot(temp):
    if temp > 100:
        print("So Hot!")
    elif temp > 90:
        print("Yes!")
    elif temp > 75:
        print("Eh")
    else:
        print("Nah")

is_it_hot(95)
is_it_hot(60)
```

```
Yes!
Nah
```

- **R1:** Pick a temperature that makes `temp > 100` true. Predict what `is_it_hot` prints for it, then add the call and run it. How many lines printed, and why?
- **R2:** 95 is greater than 90 and greater than 75. Why does `is_it_hot(95)` print only `Yes!` and not `Eh` too?
- **R3:** Explain in your own words how `is_it_hot` writes its conditions from narrowest to broadest. What would `is_it_hot(95)` print if `temp > 75` were the first condition?
- **R4:** The `else` has no condition. Which temperatures reach it? Write the exact rule ("any temperature that is ___"), then test the edge with `is_it_hot(75)` and `is_it_hot(76)`.

🙋 **Ask for help if:** your answer to R2 or R4 doesn't match what the code actually prints when you run it.

---

## Part 1: Predict & Run (10 minutes)

Open `what_to_wear.py`. It has two functions: `pack_bag` prints what to put in your bag, and `pick_coat` prints which coat to wear. **Don't run it yet.**

1. Fill in every `# Prediction:` line. Each `---` line is printed by the program, so it marks where each call's output starts.
2. Run `python3 what_to_wear.py`.
3. Fill in each `# Actual:` and `# Explanation:` line. Use the big ideas tables.

Answer these as comments at the bottom of `what_to_wear.py`:

1. How many lines did each call print? Which call printed nothing, and why isn't that an error?
2. `pack_bag(45, True)` printed two items. Is that right for packing a bag? Why?
3. `pick_coat(20)` printed three coats. Is that right for choosing a coat? What should it print?
4. The two functions are written the same way, with separate `if`s. Why is that right for one function and wrong for the other?

**Swap with a partner** and compare answers.

🙋 **Ask for help if:** you and your partner can't agree on which function is wrong, or why.

---

## Part 2: Investigate (15 minutes)

### Truthy, falsy, `and`, `or` (in the REPL)

Open the REPL (`python3`). Predict each result before you press Enter. For the `if` line, press Enter twice.

```
bool(0)
bool("")
bool("no")
bool(None)
if False or "no": print("runs")
True or True and False
(True or True) and False
```

Write down:

1. Which values counted as false? What do they have in common?
2. `"no"` means no in English. Why does Python count it as true?
3. Why did `runs` print, even though one side of the `or` is `False`?
4. The last two lines use the same three values. Why do they give different answers?

🙋 **Ask for help if:** you can't explain why the last two lines differ. Use idea 6 and work out which operator Python does first.

✅ **Checkpoint:** Tell an instructor, in one sentence, when separate `if`s are the right choice and when a chain is the right choice.

---

## Part 3: Modify (15 minutes)

Work in `what_to_wear.py`.

### 1. Fix the error

Change **two words** in `pick_coat` so that it prints exactly one coat: the warmest one the temperature needs.

Self-check: run it. `pick_coat(20)` should print only `winter coat`, and `pick_coat(40)` should print only `jacket`.

### 2. Variation

The weather app doesn't say "raining" or "not raining." It gives the chance of rain as a percentage, from 0 to 100.

**Without changing the logic of the `pack_bag` function**:

1. In `pack_bag`, rename the parameter `raining` to `rain_chance`. Change it in both places it appears.
2. Change the two `pack_bag` calls (and their `---` lines) to use the app's numbers: `pack_bag(45, 80)` and `pack_bag(70, 0)`. Predict, then run. The output should look the same as before. Why does it still work?
3. Add a third call at the bottom, with its own `---` line: `pack_bag(70, 10)`. Predict, then run.

Answer as comments:

1. Would you carry an umbrella for a 10% chance of rain? What did `pack_bag` decide, and which idea number explains why?
2. What does Python check in `if rain_chance:`? Write the rule in words.

Now change the umbrella condition so that the umbrella goes in the bag only when the chance of rain is 50 or higher.

Self-check: use the working habit. Add calls for `pack_bag(70, 49)` and `pack_bag(70, 50)`. Only the second one should print `umbrella`.

🙋 **Ask for help if:** `pack_bag(70, 0)` and `pack_bag(70, 10)` print the same thing after your change and you can't tell whether that's right.

### 3. Trace

Add this function and these two calls at the bottom of `what_to_wear.py`:

```python
def coat_for(temp):
    if temp < 32:
        return "winter coat"
    if temp < 50:
        return "jacket"
    if temp < 65:
        return "hoodie"
    return "no coat"

print("Wear:", coat_for(20))
print("Wear:", coat_for(70))
```

**Before running**, trace `coat_for(20)` as comments, one step per line: which condition Python checks, whether it is true or false, and what happens next. Then trace `coat_for(70)` the same way. Run it and compare.

Answer as comments:

1. `coat_for` uses separate `if`s, like the broken `pick_coat` did. Why does `coat_for(20)` give back only one coat?
2. `temp < 50` is true when `temp` is 20. Did Python ever check it? How do you know?
3. Why doesn't `return "no coat"` need an `else`?

Now swap the first two `if` blocks so that `temp < 50` comes first. Predict what `coat_for(20)` gives back, then run it. Which review idea explains the result? Swap them back when you're done.

🙋 **Ask for help if:** you're not sure which lines of `coat_for` ran. Add a `print` above each `if`, run it again, and look at which ones appear.

---

## Part 4: Make (15 minutes)

**Task: Movie night.** In `movie_night.py`, write two functions for a movie theater: one that works out the price of a ticket, and one that shows every perk a group gets.

**Requirements**

1. `ticket_price(age, is_matinee)` **returns** the price of one ticket:
   - Children under 3 get in free (`0`).
   - Children under 13 and seniors 65 or older pay `9`.
   - Anyone else at a matinee pays `11`.
   - Everyone else pays `15`.
2. If more than one price fits a person, they pay the **cheapest** one. For example, an 8-year-old at a matinee pays `9`, not `11`.
3. `ticket_price` uses only `if` and `return`: no `elif` and no `else`. It uses `or` exactly once.
4. `show_perks(tickets, is_member)` **prints** every perk the group gets:
   - Members get `Free popcorn`.
   - Groups of 4 or more tickets get `Group discount`.
   - Members with 2 or more tickets get `Free parking`.
5. Test the edges: call `ticket_price` with ages 2 and 3, 12 and 13, and 64 and 65, and check each answer against the rules.
6. The program must run without crashing.

**Check your output.**

```
Age 2, evening: 0
Age 8, matinee: 9
Age 70, evening: 9
Age 16, matinee: 11
Age 40, evening: 15
Perks for 4 tickets, member:
Free popcorn
Group discount
Free parking
Perks for 1 ticket, not a member:
```

The last line has nothing under it, because that group gets no perks.

Tip: before you write `ticket_price`, decide which kind of task it is ("one answer" or "check all that apply"). Then do the same for `show_perks`. The two answers should be different.

🙋 **Ask for help if:** the 8-year-old at a matinee pays `11`, and you can't find which condition is in the wrong place.

✅ **Checkpoint:** Show an instructor your code. Point to the function that checks all that apply and the function that gives one answer, and explain how the code shows the difference.

---

## Part 5: Independent check (10 minutes)

Your instructor will hand this out. Work alone, with no AI and no notes, and write your prediction on paper before you run anything.

---

## Going further (optional)

Try E1 in the REPL. Predict first, then press Enter twice after the `if` line.

```
drink = "water"
if drink == "tea" or "coffee": print("hot drink")
```

1. Water isn't a hot drink. Why did `hot drink` print? Use ideas 5 and 6 to split the condition into its two sides, and say what Python decides about each side.
2. Fix the condition so it prints `hot drink` only when `drink` is `"tea"` or `"coffee"`. Test it with `"water"`, `"tea"`, and `"coffee"`.
