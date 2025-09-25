Challenge: Reverse "URSTUDENT" using stack.

Step 1: 
  stack = []
step 2: add elements in stack letter by letter
  stack.list("URSTUDENT")
  print(stack)
step 3: define other rev_stack valiable
    rev_stack
step 4: pop data into new stack
   rev_stack = [item.pop() for item in stack]
step 5: print reversed stack
   print(rev_stack)

Challenge: Queue vs stack for distributing books in library. Which fits?


Queue is the better fit for distributing books in a typical library setting - assuming you're distributing to people based on arrival/request order.