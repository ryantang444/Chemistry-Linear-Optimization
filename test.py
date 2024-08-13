import pulp
pulp.pulpTestAll()


import pulp
print(pulp.listSolvers(onlyAvailable=True))