# Python Object-Oriented Programming Notes

Based on Andy Bek's Udemy course: *Python Object Oriented Programming (OOP): Beginner to Pro*.

## Section II - Basic Classes

- **A class** is a blueprint that represents a type of object.
- Calling a class creates instances (or objects) of that class.
- Even the simplest class has **state** and **behavior**.

### Class State

- **Defined in the class body** and shared by all instances.
- Stored in a `mappingproxy` object and accessed via `__dict__`.
- Can be modified or extended outside of the class body.

### Methods and Behavior

- Adding behavior: Define functions within the class (called **methods**).
- These methods always have at least one parameter, conventionally named `self`.
- Functions defined in the class body become bound to instances.

### Instance Attributes

- **Attributes** are variables associated with objects.
- Best practice: Set them in the `__init__` method.
- Can be set before or after the instance is created.

### Class and Static Methods

- **Class methods:** The class is passed as the first argument (implicitly).
- **Static methods:** Do not take the instance or class as an argument.
- Static methods are conceptually related to the class and grouped in its namespace.

### Revisiting `self`

- `self` is the first argument passed to instance methods and refers to the instance object.
- Not a reserved keyword; a convention only.

### Dunder `__dict__`

- **Instance attributes** are stored in a plain Python dictionary accessed via `instance.__dict__`.
- **Class attributes:** Use a `mappingproxy`, a restricted read-only dictionary.

### Class vs. Instance `__dict__`

- Classes have their own attribute namespace, accessible with `class.__dict__`.
- Contains all instance, class, and static methods, class variables, and descriptors.

### Access Control

- Python attributes are public by default, with no classical access control.
- Aligns with Python's **Uniform Access Principle**.
- Use properties for custom logic for getting, setting, or deleting attributes.

### Docstrings

- **Docstrings** are strings written as the first statement of a class, function, or module.
- Bound to the `__doc__` attribute and visible in `help()`.
- Different from comments and follow various styles.

---

### Skill Challenge 1: Define a `Student` Class

#### Requirements:

1. **Instance Attributes:** `name` and `age`.
   - Default `age` to a number; allow instances to be created by specifying only `name`.
2. **Class Attribute:** `educational_platform` (default: `udemy`).
3. Define a `greet()` method to randomly select and interpolate greetings like:
   - "Hi, I'm..."
   - "Hey there, my name is..."
   - "Hi. Oh, my name is..."
4. From a list of student names, create instances and let each student introduce themselves.

---

### Skill Challenge 2: Define a `Password` Class

#### Requirements:

1. **Instance Attributes:** `strength` and `length`.
2. Generate a random password based on `strength`:
   - **Low:** 8 characters (lowercase/uppercase).
   - **Mid:** 12 characters (lowercase/uppercase/numbers).
   - **High:** 16 characters (lowercase/uppercase/numbers/punctuation).
3. If `length` is specified, it overrides the defaults.
4. Default strength is `"mid"` if not specified.
5. Implement `show_input_universe()`:
   - Return a dictionary of character pools: `{"letters": [...], "numbers": [...], "punctuation": [...]}`.


## Section III - Dunders

### `__repr__`

- Customize object representation by implementing `__repr__` in the class definition.

---

### `__repr__` vs `__str__`

- Both `__repr__` and `__str__` define custom string representations for an object.
- **Tip:** Define `__repr__` if you have to choose, as Python falls back to `__repr__` if `__str__` is not defined.
- **Best Practice:** `__repr__` should ideally return valid Python code that can recreate the instance.

---

### `__format__`

- Customize string formatting for objects by defining `__format__`.
- Called by `f-strings`, the `format()` built-in, and `str.format()`.
- Optional: Python will delegate to `__str__` or fall back to `__repr__` if not defined.

---

### Object Equality

- By default, instances of the same class are **not equal**.
- Customize object equality by defining `__eq__`.

---

### Hashing and Mutability

- A hash is a fixed-length integer identifying an object.
- Immutable types like `int`, `float`, `str`, and `tuple` are hashable.
- **Hashable objects:**
  - Hash value does not change during the object’s lifetime.
  - Must implement `__hash__` (returning an integer) and `__eq__`.
  - Hashes facilitate fast dictionary lookups and set membership checks.

---

### Other Rich Comparisons

- Define `__lt__`, `__gt__`, `__le__`, and `__ge__` to support comparison operators.
- Use `functools.total_ordering` to simplify implementation if `__eq__` and one of {`__lt__`, `__gt__`, etc.} are defined.

---

### Truthiness

- By default, all objects are truthy.
- Customize truthiness by defining `__bool__`.

---

### Container Classes

- Classes can act as container abstractions for other classes.
- A container class can be capacity- and type-aware, storing instances of another class.

---

### Operator Overloading

- Support custom operators by implementing methods like `__add__`, `__radd__`, `__sub__`, `__mul__`, etc.
- To ensure commutativity (e.g., `a + b == b + a`), implement both `__add__` and `__radd__`.

---

### The `__getitem__` Magic

- Add support for square-bracket key lookups by implementing `__getitem__`.
- Makes the class iterable.
- Customizable to handle integers, slices, or other logic.

---

### Defining Custom Dunders

- Avoid defining custom dunder methods—it’s considered an antipattern.
- Risks clashing with future Python updates.

---

### Skill Challenge 3: Define a `Contact` Class

#### Requirements:

1. **Instance Attributes:** `name`, `last_name`, `phone`, `email`, and `display_mode` (default: `"masked"`).
2. Create instances using `name` and `last_name` only (phone/email optional).
3. Customize string representation:
   - `str()` returns initials (e.g., "J.D." for John Doe).
   - Masked mode obfuscates `name` and `last_name`.
   - Regular mode shows all attributes.
4. Equality: Two instances are equal if any of the following match:
   - `phone` or `email`
   - `name` and `last_name`
5. A masked instance's string can reveal all attributes via formatting.

---

### Skill Challenge 4: Define a `Vector` Class

#### Requirements:

1. **Instance Attributes:** `x`, `y`, `z` (no default values).
2. Add functionality:
   - Reconstruct instances via `__repr__`.
   - Calculate magnitude using `abs()` (√(x² + y² + z²)).
   - Overload operators:
     - Add two vectors (e.g., `Vector(1, 2, 3) + Vector(4, 5, 6) -> Vector(5, 7, 9)`).
     - Scalar multiplication, supporting both orders (e.g., `Vector(1, 2, 3) * 2 == 2 * Vector(1, 2, 3)`).
   - Comparisons (e.g., `<`, `>`, `==`, etc.).
3. **Hashable:** Implement `__hash__` and `__eq__`.
4. Truthiness: False only if magnitude is 0.
5. Support square-bracket access (e.g., `v['y']` or `v['Y']` for `2`).

