# 2019/08/28: Tensorflow basic


### Question 1:
What are the main benefits of creating a computation graph rather than directly
executing the computations? What are the main drawbacks?

### Question 2:
Is the statement `a_val = a.eval(session=sess)` equivalent to `a_val =
sess.run(a)`?

### Question 3:
Is the statement `a_val, b_val = a.eval(session=sess), b.eval(ses
sion=sess)` equivalent to `a_val, b_val = sess.run([a, b])`?

### Question 4:
Can you run two graphs in the same session?

### Question 5:
 When is a variable initialized? When is it destroyed?

### Question 6:
What happens when you run the graph to evaluate an operation that depends on
a placeholder but you don’t feed its value? What happens if the operation does
not depend on the placeholder?



