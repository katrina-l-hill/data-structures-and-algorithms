# Blog Notes: Merge Sort

## This blog will discuss how merge sorts work and provide a visual output to help you understand.

### Visual

![Visual](./)

### Trace/Step-through

[8, 4, 23, 42]

- 1st pass

Start on the left side of the array and check the value at index position 1 (i), which is 4. 4 is temporarily removed from the array and assigned to the "temp" variable.
The value of 4 is compared to the value to the left of it, which is 8 (j). Since 4 is less than 8, we shift 8 to the right into the vacant position 4 was in since it was temporarily removed.
4 is now placed in the vacant position 8 was in so that it is now on the far left of the array.
[]

- 2nd pass
Start at the second index position, which is 23 (j + 1), and temporarily removed from the array and assigned to the "temp" variable.
The value of 23 is compared to the value to the left of it, which is 8 (j). Since 8 is less than 23, it is not shifted to the right in the vacant position 23 was in.
23 is placed back into it's vacant position, and the algorithm goes on to the next pass.
[]

- 3rd pass

- 4th pass

- 5th pass

- 6th pass

### Big O Efficiency
