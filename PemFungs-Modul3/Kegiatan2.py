#Kegiatan 2
def extract_integers(data):
    integer_lists = []
    for item in data:
        parts = item.split()
        integers = [part for part in parts if part.isdigit()]
        integer_lists.append(integers)
    return integer_lists

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

integer_data = extract_integers(data)
for integers in integer_data:
    print(integers)
