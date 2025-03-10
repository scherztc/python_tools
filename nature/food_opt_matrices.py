import numpy as np
from scipy.optimize import linprog

# Supply matrix (food available in each region)
supply = np.array([100, 150, 200])  # supply in 3 regions

# Demand matrix (food required in each consumption zone)
demand = np.array([80, 120, 150, 100])  # demand in 4 zones

# Cost matrix (cost to transport 1 unit of food from source to destination)
cost_matrix = np.array([
    [2, 3, 1, 4],  # costs from Region 1 to each of the 4 zones
    [5, 4, 2, 3],  # costs from Region 2 to each of the 4 zones
    [3, 2, 4, 1]   # costs from Region 3 to each of the 4 zones
])

# Flatten the cost matrix for linprog optimization
cost_vector = cost_matrix.flatten()

# Supply and demand constraints for optimization
# Row constraints (supply): Total food provided by each source region should not exceed supply
lhs_ineq = np.zeros((len(supply), len(cost_vector)))
for i in range(len(supply)):
    lhs_ineq[i, i * len(demand):(i + 1) * len(demand)] = 1  # each region's supply constraint

rhs_ineq = supply  # right-hand side (supply limits)

# Column constraints (demand): Total food received by each consumption zone should meet demand
lhs_eq = np.zeros((len(demand), len(cost_vector)))
for i in range(len(demand)):
    lhs_eq[i, i::len(demand)] = 1  # each demand constraint

rhs_eq = demand  # right-hand side (demand)

# Solve the linear programming problem to minimize transportation cost
result = linprog(c=cost_vector, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, method='highs')

# Output the results
if result.success:
    # Reshape the result into the original 3x4 transportation matrix
    transportation_plan = result.x.reshape(len(supply), len(demand))
    print("Optimized Food Distribution Plan (Food transported from each region to each zone):")
    print(transportation_plan)
    print("\nTotal transportation cost:", result.fun)
else:
    print("Optimization failed:", result.message)

