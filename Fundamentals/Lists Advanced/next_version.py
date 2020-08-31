input_sw_version = input().split(".")

next_version = str(int("".join(input_sw_version)) + 1)

print(".".join(next_version))
