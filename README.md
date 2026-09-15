# Python Functions – Odd Numbers and Odd-Length Words

## 📌 Overview

This practice program demonstrates how to use **Python `for` loops, functions, conditional statements, and the modulus operator (`%`)** to:

* Display odd numbers from a list
* Create a function to find odd numbers
* Create a function to find words with an odd number of characters

This program is designed for beginners who are learning **Python functions and loops**.

---

## 🛠️ Technologies Used

* **Python 3**
* `for` loop
* Functions
* `if` condition
* Lists
* `len()`
* Modulus operator `%`

---

# 1. Display Odd Numbers from a List

### Code

```python
d = [1, 2, 3, 4, 5, 6]

for i in d:
    if i % 2 == 1:
        print(i)
```

### Output

```text
1
3
5
```

### How It Works

The program checks every number in the list.

```python
i % 2 == 1
```

If the remainder after dividing the number by `2` is `1`, the number is odd.

For example:

```text
1 % 2 = 1  → Odd
2 % 2 = 0  → Even
3 % 2 = 1  → Odd
4 % 2 = 0  → Even
5 % 2 = 1  → Odd
```

---

# 2. Find Odd Numbers Using a Function

### Code

```python
def odd(d):
    for i in d:
        if i % 2 == 1:
            print(i)

odd([1, 2, 3, 4, 5, 6])
```

### Output

```text
1
3
5
```

### Explanation

The logic is placed inside a reusable function called `odd()`.

```python
def odd(d):
```

Here:

* `odd` → function name
* `d` → parameter that receives a list

The function is called using:

```python
odd([1, 2, 3, 4, 5, 6])
```

This makes the program reusable with different lists.

### Example

```python
odd([10, 11, 12, 13, 14, 15])
```

Output:

```text
11
13
15
```

---

# 3. Find Words with Odd Length

### Code

```python
def odd_word(s):
    for i in s:
        if len(i) % 2 == 1:
            print(i)

odd_word(["Back", "Welcome", "Hi", "Prana", "Jadhao", "Raj"])
```

### Output

```text
Back
Welcome
Prana
Jadhao
Raj
```

### Explanation

The function checks the length of each word.

```python
len(i) % 2 == 1
```

If the length of the word is odd, it prints the word.

For example:

```text
Back     → 4 characters → Even
Welcome  → 7 characters → Odd
Hi       → 2 characters → Even
Prana    → 5 characters → Odd
Jadhao   → 6 characters → Even
Raj      → 3 characters → Odd
```

Therefore, the expected output is:

```text
Welcome
Prana
Raj
```

> **Note:** The original code's expected output should exclude `"Back"` and `"Jadhao"` because their lengths are even.

---

## 🔄 Program Flow

```text
Start
  ↓
Take a list
  ↓
Iterate through each element
  ↓
Check condition
  ↓
Is number odd?
  ├── Yes → Print number
  └── No  → Skip
  ↓
For words:
Check word length
  ↓
Is length odd?
  ├── Yes → Print word
  └── No  → Skip
  ↓
End
```

---

## 📚 Concepts Practiced

| Concept            | Usage                         |
| ------------------ | ----------------------------- |
| `for` loop         | Iterate through list elements |
| Function           | Create reusable logic         |
| `if` statement     | Check conditions              |
| `%` operator       | Check odd/even values         |
| `len()`            | Find string length            |
| List               | Store numbers and words       |
| Function parameter | Pass data to functions        |
| Function call      | Execute a function            |

---

## 🎯 Learning Objectives

After completing these programs, you should understand:

* How to iterate through a list using a `for` loop
* How to identify odd numbers
* How to create and call functions
* How to pass a list as a function argument
* How to calculate string length using `len()`
* How to identify strings with odd lengths
* How to reuse the same logic with different input data

---

## 🚀 Possible Improvements

Instead of printing values directly, the functions can return a list.

For example:

```python
def odd(d):
    result = []

    for i in d:
        if i % 2 == 1:
            result.append(i)

    return result

print(odd([1, 2, 3, 4, 5, 6]))
```

Output:

```text
[1, 3, 5]
```

This approach is more reusable because the returned result can be stored, processed, or used elsewhere in a program.

---

## 👨‍💻 Author

**Pranay Vishwanath Jadhao**

B.E. Electronics & Telecommunication Engineering
Python & Data Analytics Learner

---

## 📄 License

This project is created for **educational and practice purposes**.
