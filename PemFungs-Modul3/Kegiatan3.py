random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

def map_int_to_dict(value):
    def curry_mapping():
        def map_internal():
            ratusan = value // 100
            sisa = value % 100
            puluhan = sisa // 10
            satuan = sisa % 10
            return {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}
        return map_internal
    return curry_mapping

int_mapped = list (map(lambda x: x()(), map(map_int_to_dict, int_values)))

print("Data Float:", tuple(float_values))
print("Data Int:")
for data in int_mapped:
    print(data)
print("Data String:", string_values)