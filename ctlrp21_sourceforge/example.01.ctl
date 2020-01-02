begin_problem(test2).

list_of_descriptions.
name({*test 2*}).
author({*Lan Zhang*}).
status(unsatisfiable).
description({*Test a unsatisfiable CNF clauses set*}).
end_of_list.

list_of_ctlformulae(conjectures).
  %AG p <-> ~ EF ~p
  and(implies(AG(p), not(EF(not(p)))),
      implies(not(EF(not(p))), AG(p))).
end_of_list.

end_problem.
