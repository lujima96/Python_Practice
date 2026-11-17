item_name = input("Item name: ").strip()
package_count = int(input("Number of packages: "))
weight_per_package = float(input("Weight of each package: "))

total_weight = package_count * weight_per_package

print()
print(f"Item: {item_name}")
print(f"Packages: {package_count}")
print(f"Total weight: {total_weight}")