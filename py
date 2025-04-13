# Function to estimate insurance cost based on various factors
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    # Calculate the estimated insurance cost using the given formula
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    
    # Print the estimated insurance cost with the person's name
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")

    # Return the estimated cost
    return estimated_cost

# Estimate Maria's insurance cost by calling the function with her details
maria_insurance_cost = estimate_insurance_cost(name="Maria", age=31, sex=0, bmi=23.1, num_of_children=1, smoker=0)

# Estimate Rohan's insurance cost by calling the function with his details
rohan_insurance_cost = estimate_insurance_cost(name="Rohan", age=25, sex=1, bmi=28.5, num_of_children=3, smoker=0)

# Estimate Valentina's insurance cost by calling the function with her details
valentina_insurance_cost = estimate_insurance_cost(name="Valentina", age=53, sex=0, bmi=31.4, num_of_children=0, smoker=1)

# Create a list of names for the individuals
names = ['Maria', 'Rohan', 'Valentina']

# Create a list of actual insurance costs for the individuals
insurance_cost = [4150.0, 5320, 35210.0]

# Combine names and actual insurance costs using zip and convert to a list
insurance_data = list
# Print the actual insurance cost data
print(f'Here is the actual insurance cost data: {insurance_data}')

# Create an empty list to store estimated insurance data
estimated_insurance_data = []

# Append estimated insurance costs for each individual to the list
estimated_insurance_data.append(('Maria', maria_insurance_cost))
estimated_insurance_data.append(('Rohan', rohan_insurance_cost))
estimated_insurance_data.append(('Valentina', valentina_insurance_cost))
# Print the estimated insurance cost data
print(f'Here is the estimated insurance cost data: {estimated_insurance_data}')

# Calculate the difference between actual and estimated insurance costs
insurance_cost_difference = [(actual[0], actual[1] - estimated[1]) for actual, estimated in zip(insurance_data, estimated_insurance_data)]

# Print the differences in insurance costs
print(f'Insurance cost difference: {insurance_cost_difference}')



