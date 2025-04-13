# Function to estimate insurance cost based on various factors
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    # Calculate the estimated insurance cost using the given formula
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    
    # Print the estimated insurance cost with the person's name
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
