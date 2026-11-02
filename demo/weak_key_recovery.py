
from cryptography.hazmat.primitives.asymmetric import ec

CURVE = ec.SECP384R1()

# Reported weak scalar values (for educational simulation only)
weak_keys = [4, 56, 66, 115, 155, 156, 230, 237]

print("=" * 55)
print("       eMudhra CA Weak Key Recovery Simulation")
print("=" * 55)

for target_private in weak_keys:

    # Generate a synthetic public key
    target_key = ec.derive_private_key(target_private, CURVE)
    target_public = target_key.public_key().public_numbers()

    print(f"\nTarget public key generated for test case.")

    # Search the deliberately small candidate range
    for candidate in range(1, 256):

        candidate_key = ec.derive_private_key(candidate, CURVE)
        candidate_public = candidate_key.public_key().public_numbers()

        if candidate_public == target_public:
            print(f"[+] Private scalar recovered: {candidate}")
            break

print("\n" + "=" * 55)
print("Simulation completed successfully.")
print("=" * 55)
