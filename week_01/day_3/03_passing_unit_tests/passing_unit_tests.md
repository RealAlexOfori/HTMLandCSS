# Passing Unit Tests

**Lesson Duration: 60 minutes**

### Learning Objectives

- Be able to read a test file
- Be able to write the code required to pass a test

## Introduction

When we write code, how do we know that it works?

The only way that we can possibly know if our code works is to test it. Up until this point, we've been testing our code manually. We add a new piece of functionality, then we run the program and check that it works the way that we expected it to. If it does, great. If it doesn't, we make changes to the code until it does work the way that we wanted it to.

What if the new changes that we've made prevent some of our old code from working properly? Unfortunately, this is quite common in software development. It's called regression. Every time we add new functionality, we should check that all of our old functionality still works the way that it's supposed to too. This sounds like it might become quite time consuming as our programs continue to grow in scope. Before long, we'll be spending more time testing our program than we will writing code, and that doesn't sound like fun.

Luckily, we can write code to automatically test that our code works as we expect it to. Every time we add new functionality, we can add some new tests to go along with it. We can then run our new tests to make sure that the new code works and our old tests to make sure that there haven't been any regressions.

In this lesson we will learn how to read and run a test file, so that we can write the code required to pass the tests within it.

## How Does Testing Work?

Most functions recieve some kind of data as input, act on the data in some way, and return a result based on the data that they were given. Consider the following function:

```py
def add_five(number):
    return number + 5
```

This function takes in any number and adds five to it. How could we test that it works? If we give the number 1 to this function, we would expect to get the number 6 back.

We can group the things that we need to think about into three categories:

- Data
- Test
- Code

The data that we're working with in this case is very simple. It's the number 1. We would feed the number 1 to our function and test the result that it gives us back. In this case, our test would expect to receive the number 6. It would "pass" if it received the number 6 and "fail" if it receives any other value.

The code that we are testing here is the simple `add_five()` function above.

> Open the start_code and take a few minutes to read record_store_test.py

## Reading a Test File

There will be a few things in this file that you aren't familiar with. For one, it's written using a class. We won't worry about this too much as we won't be expecting you to create a test file of your own for the time being. For now, the focus will be on reading and understanding a test file so that you can write the code required to pass the tests and run the tests to make sure that your code works.

In this file you'll see a number of functions (defined by the `def` keyword) which are our tests. Each one is currently marked with the `@unittest.skip` decorator, meaning that they wouldn't run if we were to run our tests. This will allow us to unskip and work on a single test at a time.

We will write the code to pass these tests in a separate file, `src/functions.py`.

How do we run our tests?

We would import all of our test files into `run_tests.py` and then run `run_tests.py` to run our tests. Let's give it a go and see what happens.

```sh
python3 run_tests.py

# sssss
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK (skipped=5)
```

Great. Our test file is running and we can see that all 5 tests are being skipped. Let's unskip the first one and get to work on making it pass!

Comment out or delete the `@unittest.skip` decorator for `test_greet_catalan` and run the tests again.

```py
# @unittest.skip("comment out this line to run the test")
  def test_greet_catalan(self):
      result = greet_catalan("Mar")
      self.assertEqual("Hola, Mar", result)
```

This time we get a very different result:

```sh
python3 run_tests.py

# sssEs
# ======================================================================
# ERROR: test_greet_catalan (tests.functions_test.TestFunctions)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/.../tests/functions_test.py", line 8, in test_greet_catalan
#     result = greet_catalan("Mar")
# NameError: name 'greet_catalan' is not defined

# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# FAILED (errors=1, skipped=4)
```

We can see now that we have four skipping tests and one that is causing an error. Errors can often be annoying to deal with, but they're actually very helpful when testing. If we follow the trail of errors, we can let them guide us into writing working code. Also, it's worth noting that we should _always_ run our tests before we write the code to pass the test. If you've never seen a test fail then how do you know that it _can_ fail? Maybe it's broken and passes all the time even if it should fail!

We're getting a `NameError` because "name `greet_catalan` is not defined". Let's look at the test and see if we can figure out what's going on here.

```py
# @unittest.skip("comment out this line to run the test")
  def test_greet_catalan(self):
      result = greet_catalan("Mar")
      self.assertEqual("Hola, Mar", result)
```

First, let's look at the game of the test. It's called `test_greet_catalan`. We can infer from this that we're to write some kind of greeting (in Catalan) functionality.

Next, we'll look at the body of the test. The test tries to call a function `greet_catalan`, which currently doesn't exist. This is the function that it's trying to test and the function that we will have to create. The test is already telling us how the function should be used, so we have quite a lot of information to work with.

We can see that the `greet_catalan` function is passed an argument `"Mar"` and it returns some kind of value, which is being stored in the variable `result`.

On the next line, we can see that the function `assertEqual` is being called. It takes two arguments. If the arguments are the same, the test passes. If they're different, the test fails.

This test expects the value of the `result` variable to be `"Hola, Mar"`, so we know that our `greet_catalan` function takes in a **string** like `"Mar"` and returns `"Hola, Mar"`.

Now that we know what we need to do, let's go ahead and do it!

## Passing a Test

We were getting a `NameError` because the function `greet_catalan` doesn't exist. The first thing that we have to do is define the function. We also know that the test was passing a **string** representing a **name** to the function when it tried to call it, so we should add that as a parameter too.

```py
# functions.py

def greet_catalan(name): # NEW
    pass                 # NEW
```

That should be everything that we need to do in order to fix the error that we had, so let's run the tests again and see what happens now.

```sh
python3 run_tests.py

# sssFs
# ======================================================================
# FAIL: test_greet_catalan (tests.functions_test.TestFunctions)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/user/e63_classnotes/week_01/day_3/03_passing_unit_tests/passing_unit_tests_start_code/tests/functions_test.py", line 9, in test_greet_catalan
#     self.assertEqual("Hola, Mar", result)
# AssertionError: 'Hola, Mar' != None

# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s

# FAILED (failures=1, skipped=4)
```

The first thing that we should notice here is that we aren't getting a `NameError` any more! We've moved on from this error to one for a failing test: `AssertionError`. This is great news. Our code runs, but the test doesn't get the result that it wanted.

We can see that the test expected to get `"Hola, Mar"` but it actually got `None` because we haven't told our function to return anything. Let's update our function, so that it actually returns the string that the test is looking for, and then run the test again.

```py
# functions.py

def greet_catalan(name):
    return f"Hola, {name}"  # UPDATED
```

> Note: We are NOT returning the hard-coded value `"Hola, Mar"`, even though this would pass our test. We have to work with the data (some **string** name) that we were given by the test.

```sh
python3 run_tests.py

# sss.s
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK (skipped=4)
```

Great news! We have a passing test. 

### Task

Have a go repeating these steps for the second test, `test_greet_mandarin`.

<details>
<summary>Solution</summary>

```py
# functions_test.py

# @unittest.skip("comment out this line to run the test")
def test_greet_mandarin(self):
    result = greet_mandarin("Sky")
    self.assertEqual("Ni hao, Sky", result)
```

```py
# functions.py

def greet_mandarin(name):
    return f"Ni hao, {name}"
```
</details>

### More tests

Let's pass another test!

Again, we'll start by removing the `@unittest.skip` decorator that tells `unittest` to skip the test.

```py
# @unittest.skip("comment out this line to run the test")
def test_count_eggs(self):
    chickens = [
        { "name": "Margaret", "age": 2, "eggs": 0 },
        { "name": "Hetty", "age": 1, "eggs": 2 },
        { "name": "Henrietta", "age": 3, "eggs": 1 },
        { "name": "Audrey", "age": 2, "eggs": 0 },
        { "name": "Mabel", "age": 5, "eggs": 1 },
    ]
    result = count_eggs(chickens)
    self.assertEqual(4, result)
```

Now, let's think about what this test wants from us.

The test is called `test_count_eggs`, so we can assume that we're supposed to count some eggs... Hint: We have done this before!

We can see that the test sets up a list of dictionaries representing our `chickens`, and calls `count_eggs` passing in the list of `chickens`.

A value is returned from the function and stored in `result`, and this **actual** value is compared against the **expected** `4`, which is total number of eggs in our list of chickens.

```py
self.assertEqual(4, result)
```

We can summise from this that our function will have to take in a list of dictionaries and then total up the number of eggs, returning the total.

Let's run the test, see it fail and figure out what we have to do.

```sh
python run_tests.py

# Ess.s
# ======================================================================
# ERROR: test_count_eggs (tests.functions_test.TestFunctions)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/.../tests/functions_test.py", line 27, in test_count_eggs
#     result = count_eggs(chickens)
# NameError: name 'count_eggs' is not defined

# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# FAILED (errors=1, skipped=3)
```

That's right! We don't have a function named `count_eggs`, so we'll have to create one. We know that in the test, `count_eggs` is passed one parameter (a list), so we can add the parameter for this.

```py
# record_store.py

def count_eggs(chickens):
    pass
```

Let's run the test again and see what it wants us to do next.

```sh
# Fss.s
# ======================================================================
# FAIL: test_count_eggs (tests.functions_test.TestFunctions)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/.../tests/functions_test.py", line 28, in test_count_eggs
#     self.assertEqual(4, result)
# AssertionError: 4 != None

# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# FAILED (failures=1, skipped=3)
```

Great, we've moved on from the `NameError` that we saw before and now we have an `AssertionError` for a failing test. We can see that the test is expecting `4`, but in actuality is getting `None`. We'll have to add the functionality to calculate and return the correct total.

```py
# functions.py

def count_eggs(chickens):
    total_eggs = 0

    for chicken in chickens:
        total_eggs += chicken["eggs"]

    return total_eggs
```

Looks good to me. Let's run the tests again and see what happens now.

```sh
python3 run_tests.py

# .ss..
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK (skipped=2)
```

Great, looks like we have three passing tests now!

## Task (5-10 minutes)

Pass the final two tests!

Try to answer the following questions before you start

- What should your function be called?
- What arguments are going to be passed to your function?
- What is the test expecting you to return from your function?

<details>
<summary>Solution</summary>

```py
# functions.py

def find_chicken_by_name(chickens, name):
    found_chicken = None

    for chicken in chickens:
        if chicken["name"] == name:
            found_chicken = chicken

    return found_chicken
```
</details>

The final two tests actually test the same function `find_chicken_by_name` but looks at two possible conditions: one where the chicken is found and returned; one where there is no chicken with the name, so `None` is returned.

## Conclusion

Now that we are able to test our code, we can be sure that it works without spending ages testing it manually. We can also rest assured that we haven't broken our old code every time that we make changes now, because we can simply run our old tests again to check.

