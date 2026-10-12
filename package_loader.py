total_items = int(input("How many items do you want to send? "))

package_count = 1
current_package_weight = 0
total_weight = 0
total_empty_kg = 0

max_empty_in_package = 0
max_empty_package_num = 1

for i in range(total_items):
    weight = int(input(f"Enter the weight of item {i + 1} (from 1 to 10 kg): "))
    
    if weight < 1 or weight > 10:
        print("Error: Weight out of allowed range (1-10 kg). Ending process.")
        break

    if current_package_weight + weight > 20:
        empty_in_current = 20 - current_package_weight
        total_empty_kg += empty_in_current
        
        if empty_in_current > max_empty_in_package:
            max_empty_in_package = empty_in_current
            max_empty_package_num = package_count

        package_count += 1
        current_package_weight = weight  
        total_weight += weight
    else:
        current_package_weight += weight
        total_weight += weight

if current_package_weight > 0:
    empty_in_current = 20 - current_package_weight
    total_empty_kg += empty_in_current
    if empty_in_current > max_empty_in_package:
        max_empty_in_package = empty_in_current
        max_empty_package_num = package_count

if total_weight == 0:
    package_count = 0

print("\n" + "=" * 40)
print("SHIPPING SUMMARY:")
print(f"1. Sent packages: {package_count}")
print(f"2. Total weight sent: {total_weight} kg")
print(f"3. Total empty kilograms: {total_empty_kg} kg")
print(f"4. Package with the most empty kilograms: Package {max_empty_package_num} ({max_empty_in_package} kg)")
print("=" * 40)