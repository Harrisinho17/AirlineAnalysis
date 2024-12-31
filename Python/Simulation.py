import numpy as np

def pricing_function(days_until_flight, seats_left, demand_level):
   
    # Average demand level for future days (uniform distribution [100, 200])
    avg_demand = 1250  # Expected value of the uniform distribution
    
    # Estimate the average number of tickets that can be sold per day
    avg_quantity_per_day = seats_left / days_until_flight
    
    # Price to match expected quantity sold with average quantity needed
    optimal_price = avg_demand - avg_quantity_per_day
    
    # Adjust price to current demand_level
    adjusted_price = max(1, min(optimal_price, demand_level))  # Ensure price is within bounds
    
    return adjusted_price

# Simulate the pricing environment
np.random.seed(42)  # For reproducibility

# Parameters
days_until_flight = 1
seats_left = 100
total_revenue = 0

# Simulate each day's pricing and demand
for day in range(days_until_flight):
    demand_level = np.random.uniform(1200, 1300)  # Simulate daily demand level
    price = pricing_function(days_until_flight - day, seats_left, demand_level)
    quantity_sold = min(int(demand_level - price), seats_left)  # Tickets sold capped by seats available
    quantity_sold = max(0, quantity_sold)  # Ensure non-negative tickets sold
    
    # Update revenue and seats left
    total_revenue += price * quantity_sold
    seats_left -= quantity_sold
    
    print(f"Day {day + 1}: Price = {price:.2f}, Demand Level = {demand_level:.2f}, "
          f"Quantity Sold = {quantity_sold:.0f}, Seats Left = {seats_left}, Revenue = {total_revenue:.2f}")

print(f"Total Revenue: {total_revenue:.2f}")