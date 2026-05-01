
## Linear Temporal Logic
This task is probably the most challenging out of all. It is designed to create a simple python API that allows the definition and verification of LTL formulae on simple infinite paths that are in the form $x_0 x_1... x_n (x_{n+1}...x_m)^\omega$. In other words the infinite path should be a prefix path concatenated to an infinitely repeated path. The exact implementation and design of most of LTL is let to the programmer, except for the `PropositionLTLFormula` class and `InfinitePath` class definition. However, the API should guarantee the following operations:
```python
# A, B, C are objects of the class LTLFormula
negated_A = ~A
next_A = +A
A_or_B = A | B
A_until_B = A >> B
A_and_B = A & B
generally_A = G(A)
eventually_A = F(A)
true_formula = TRUE
some_random_combination = (A | +F(B >> (~C))) & G(B | (+B))
``` 
You don't have to worry about the operations' priorities as you can assume that brackets will be used everywhere to avoid confusion.
After defining the API, you need to check if an inifite path satisfies a given LTL formula.