#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright 2017 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and 
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain 
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

from pyomo.environ import *

model = ConcreteModel()
model.x1 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)
model.x3 = Var(within=NonNegativeReals)

model.c1 = Constraint(expr=4*model.x1 + 2*model.x2 + model.x3 >= 5)
model.c2 = Constraint(expr=model.x1 + model.x2 >= 3)
model.c3 = Constraint(expr=model.x2 + model.x3 >= 4)

