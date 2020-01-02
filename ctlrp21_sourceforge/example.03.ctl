begin_problem(test2).

list_of_descriptions.
name({*test 2*}).
author({*Lan Zhang*}).
status(unsatisfiable).
description({*Test a unsatisfiable CNF clauses set*}).
end_of_list.


list_of_ctlformulae(conjectures).
  % EX(p v q) <-> EX p v EX q
  and(implies(EX(or(p, q)), or(EX(p), EX(q))),
      implies(or(EX(p), EX(q)), EX(or(p, q)))).
end_of_list.

end_problem.
