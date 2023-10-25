#Kegiatan 1
def convert_to_minutes(data):
    output_data = []
    for item in data:
        parts = item.split()
        weeks = int(parts[0])
        days = int(parts[2])
        hours = int(parts[4])
        minutes = int(parts[6])
        total_minutes = weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
        output_data.append(total_minutes)
    return output_data

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output_data = convert_to_minutes(data)
print(output_data)
