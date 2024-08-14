#Use this to check if you have correctly installed puLP
import pulp
pulp.pulpTestAll()
print(pulp.listSolvers(onlyAvailable=True))


#Output from Ryan's Mac
#Should have at least one available solver
"""
Available solvers: ['PULP_CBC_CMD']
Unavailable solvers: {'GLPK_CMD', 'SCIP_PY', 'CPLEX_PY', 'CPLEX_CMD', 'COINMP_DLL', 'MIPCL_CMD', 'FSCIP_CMD', 'COPT_CMD', 'HiGHS_CMD', 'COPT_DLL', 'SCIP_CMD', 'COIN_CMD', 'HiGHS', 'XPRESS_PY', 'MOSEK', 'COPT', 'GUROBI', 'XPRESS', 'GUROBI_CMD', 'PYGLPK', 'CHOCO_CMD'}
ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss..............................................Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pulp/solverdir/cbc/osx/64/cbc /var/folders/xf/krvvwf3n09qgc08x7bzzjqbw0000gn/T/1d51f119e3e54d82a8433f49be9908ac-pulp.mps -timeMode elapsed -branch -printingOptions all -solution /var/folders/xf/krvvwf3n09qgc08x7bzzjqbw0000gn/T/1d51f119e3e54d82a8433f49be9908ac-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 9 COLUMNS
At line 20 RHS
At line 25 BOUNDS
At line 29 ENDATA
Problem MODEL has 4 rows, 4 columns and 7 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Presolve 1 (-3) rows, 2 (-2) columns and 2 (-5) elements
0  Obj 51.9 Primal inf 2.099999 (1)
1  Obj 54
Optimal - objective value 54
After Postsolve, objective 54, infeasibilities - dual 0 (0), primal 0 (0)
Optimal objective 54 - 1 iterations time 0.002, Presolve 0.00
Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00

...........ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
----------------------------------------------------------------------
Ran 1348 tests in 26.794s

OK (skipped=1284)
['PULP_CBC_CMD']
"""