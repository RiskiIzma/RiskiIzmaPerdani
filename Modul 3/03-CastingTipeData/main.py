# casting adalah cara mengubah tipe data variabel

# INTEGER
print("===INTEGER===")
data_int = 9
print("data = ", data_int, "Tipe data = ", type(data_int))

# Casting
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data = ", data_float, "Tipe data = ", type(data_float))
print("data = ", data_str, "Tipe data = ", type(data_str))
print("data = ", data_bool, "Tipe data = ", type(data_bool))

# FLOAT
print("===FLOAT===")
data_float = 3.14
data_int_from_float = int(data_float)  # Mengubah float ke integer
data_str_from_float = str(data_float)  # Mengubah float ke string
data_bool_from_float = bool(data_float)  # Mengubah float ke boolean

print("data = ", data_int_from_float, "Tipe data = ", type(data_int_from_float))
print("data = ", data_str_from_float, "Tipe data = ", type(data_str_from_float))
print("data = ", data_bool_from_float, "Tipe data = ", type(data_bool_from_float))