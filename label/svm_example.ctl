begin_problem(test2).

list_of_descriptions.
name({*01*}).
author({*Lan Zhang*}).
status(unknown).
description({*Test a  CNF propositional logic clauses set*}).
end_of_list.

list_of_ctlformulae(axioms).
and(
%Header

p,
or(not(r),not(p)),
r

%Tail
).
end_of_list.

end_problem.
