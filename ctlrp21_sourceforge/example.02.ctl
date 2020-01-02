begin_problem(test2).

list_of_descriptions.
name({*test 2*}).
author({*Lan Zhang*}).
status(unsatisfiable).
description({*Test a unsatisfiable CNF clauses set*}).
end_of_list.

list_of_ctlformulae(conjectures).
  %EG p <-> ~ AF ~p
  and(implies(EG(p), not(AF(not(p)))),
      implies(not(AF(not(p))), EG(p))).
end_of_list.

end_problem.
