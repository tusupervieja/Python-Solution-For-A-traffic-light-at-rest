import math

angle_degrees_1 = float(input("Enter the value of angle 1 in degrees: "))
angle_degrees_2 = float(input("Enter the value of angle 2 in degrees: "))
weight = float(input("Enter the weight of the object in N: "))

angle_radians_1 = math.radians(angle_degrees_1)
angle_radians_2 = math.radians(angle_degrees_2)

cosine_1 = math.cos(angle_radians_1)
cosine_2 = math.cos(angle_radians_2)

T2_T1 = cosine_2 / cosine_1

sin_1 = math.sin(angle_radians_1)
sin_2 = math.sin(angle_radians_2)

Tension_1 = weight / (sin_1 * (T2_T1) + sin_2)
Tension_2 = T2_T1 * Tension_1

print(f"Tension 1: {Tension_1:.4f} N")
print(f"Tension 2: {Tension_2:.4f} N")

