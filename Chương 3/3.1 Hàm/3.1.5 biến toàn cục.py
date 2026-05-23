# Bien toan cuc va bien cuc bo trong Python

global_var = 30  # bien toan cuc

def show_values():
    local_var = 10  # bien cuc bo
    print("Gia tri bien cuc bo:", local_var)
    print("Gia tri bien toan cuc:", global_var)

# Goi ham
show_values()

# In bien toan cuc ben ngoai ham
print(global_var)
