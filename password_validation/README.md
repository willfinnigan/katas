# Password Validation
https://www.codurance.com/katalyst/password-validation      
https://www.meetup.com/software-crafters-north/  

## TTD notes
Initially I found wanted to write tests against the validate method, 
but this was tricky to do incrementally because the first test would become 
invalid against the next rule on, unless the test cases already passed all conditions.  

So instead started testing each condition individually ([test_rules.py](tests/test_rules.py)).  
This worked well - but ultimately these seem a bit redundant once started testing 
the validate method ([test_password_validation.py](tests/test_password_validation.py)).  

## Design
In the first implementation, the rules were all hard coded into the validate method.   

The second implementation wanted two new validators with different rule combinations.  
This led to the strategy pattern - rules are added to the validator and evaulated in the validate method.  

I've ended up with a functional version of the strategy pattern.  
Each rule is a function where the first argument must be the password. 

Rules are added to the validator with the add.rule(rule) method. 

I like the functional version because it seems simpler.  However there is no interface abstract base class defined, 
which is maybe not ideal?

### Handling additional arguments - n_characters rule
Initially I allowed rules to have optional arguments by using *args.  
However this isn't the ideal solution, and isn't very 'functional'.  
Instead can use 'closures', where a function creates another function.  

```python
# use a closure to handle additional argument
def create_has_more_than_n_chars_rule(n):
    def has_more_than_or_equal_n_chars(password):
        return len(password) >= n
    return has_more_than_or_equal_n_chars
```

### Define Callable 
Bonus points for defining rules using Callable.  











