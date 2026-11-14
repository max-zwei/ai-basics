
## Test Problem 2

_Test Problem 2 is more complex than the others. It's a good case study to get an impression of the time complexity of your algorithm compared to model checking. Your algorithm should be a lot faster than model checking on this test case. Do you understand why?_

- The problem uses the symbols for A, G, H, I, J, K, L, M, N, O
- Yet only symbols A,B,C,D,E,F are used for the query and implications
- Meaning the model_check functions runs through a lot more "unuseful" symbols while forward_search can focus on the query-relevant symbols

## Test Problem 5

_Your algorithm will likely not be able to solve Test Problem 5 (meaning it will return None rather than the correct result). Can you find out why?_

- The algorithm is trying to find the result for C, which the exhaustive test of model_check can find. 
- The function get_inferrable_knowledge isn't able to untangle A implies (B or C) with the additional logic of Not B. Therefore, C is never proven as True or False and the function returns None.
