# Constants
TRAILER_VOLUME_CUBIC_FEET = 52.58 * 8.33 * 9.25  # cubic feet
TRAILER_WEIGHT_LIMIT_LBS = 45000  # lbs
PALLET_VOLUME_CUBIC_FEET = 48 * 48 * 5.5 / 1728  # cubic feet (convert from cubic inches)
PALLET_WEIGHT_LIMIT_LBS = 3000  # lbs

# A 12-pack of 12 fl oz cans weighs approximately 10 lbs
SODA_PACK_WEIGHT_LBS = 10

# Function to estimate the number of soda packs that can fit in a trailer
def estimate_soda_packs_per_truck():
    # Calculate the number of pallets that fit by volume
    num_pallets_by_volume = TRAILER_VOLUME_CUBIC_FEET // PALLET_VOLUME_CUBIC_FEET
    
    # Calculate the number of pallets that fit by weight
    num_pallets_by_weight = TRAILER_WEIGHT_LIMIT_LBS // PALLET_WEIGHT_LIMIT_LBS
    
    # The actual number of pallets that can be shipped is limited by the smaller of the two numbers
    num_pallets = min(num_pallets_by_volume, num_pallets_by_weight)
    
    # Calculate the total number of soda packs per truck
    soda_packs_per_pallet = PALLET_WEIGHT_LIMIT_LBS // SODA_PACK_WEIGHT_LBS
    total_soda_packs_per_truck = num_pallets * soda_packs_per_pallet
    
    return total_soda_packs_per_truck

# Function to calculate the number of trucks needed for a given soda demand
def calculate_trucks_needed(soda_demand_packs):
    soda_packs_per_truck = estimate_soda_packs_per_truck()
    num_trucks_needed = -(-soda_demand_packs // soda_packs_per_truck)  # Ceiling division
    
    return num_trucks_needed

# Example usage
soda_demand_packs = 100000  # Example demand in soda packs
num_trucks_needed = calculate_trucks_needed(soda_demand_packs)
print(f"Number of trucks needed to meet the soda demand of {soda_demand_packs} packs: {num_trucks_needed}")

