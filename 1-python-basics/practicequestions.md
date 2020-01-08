# Practice Questions

1. Which of the following are operators, and which are values?

  `*`  operator

  `'hello'`  value

  `-88.8` value

  `-` operator

  `/` operator

  `+` operator

  `5` value

2. Which of the following is a variable, and which is a string?

  `spam` variable

  `'spam'` string

3. Name three data types

  Integer.  Float.  String.

4. What is an expression made up of?  What do all expressions do?

  An expression is made up of values and operators.  All expressions evaluate down
to a single value.

5.  What is the difference between an expression and a statement?

  A statement, such as an assignment statement (`spam = 10`) doesn't evaluate down
to a single value (has a different purpose than to evaluate).

6. What does the variable `bacon` contain after the following code runs?

  ```python
  bacon = 20
  bacon +1
  ```
  20

7. What should the following two expressions evaluate to?

  ```python
  'spam' + 'spamspam'
  'spam' * 3
  ```

  Both expressions should evaluate to `spamspamspam`

8. Why is `eggs` a valid variable name while 100 is invalid?

  In Python, variables can't begin with a number.

9. What three functions can be used to get the integer, floating-point number,
   or string version of a value?

  `int()`, `float()`, `str()`


10. Why does this expression cause an error?  How can you fix it?

  ```python
  'I have eaten ' + 99 + 'burritos.'
  ```

  We can't concatenate or add a string value to a integer value.

  ```python
  'I have eaten ' + str(99) + ' burritos.'
  ```
