# midi note of most upper left key
root_value = 24

colors = [
    "332211",  # C
    "332211",  # Db
    "332211",  # D
    "111111",  # Eb
    "111111",  # E
    "111111",  # F
    "190f0f",  # Gb
    "190f0f",  # G
    "190f0f",  # Ab
    "031612",  # A
    "031612",  # Bb
    "031612",  # B
]

print("-" * 80)
print("Please specify semitone steps along two axes (number may be negative):")
delta_x = int(input("1) Semitone steps to the right (and slightly upwards): "))
delta_y = int(input("2) Semitone steps downwards (and slightly left): "))

# set to true if CC signal of sustain pedal needs to be inverted
invert_sustain = False


def update_map(key_to_coord, row_x, row_y, row_len):
    root_key = len(key_to_coord)
    row = {root_key + i: (row_x + i, row_y) for i in range(row_len)}
    key_to_coord.update(row)
    return key_to_coord


deltas_row_x = [0, 1] * 4 + [0, 2, 3]
deltas_row_y = [0] + [1] * 10
row_lens = [2, 5] + [6] * 7 + [5, 2]

ltn_string = ""
for n in range(5):
    key_to_coord = dict()
    row_x = 7 * n
    row_y = 2 * n
    for row_len, delta_row_x, delta_row_y in zip(row_lens, deltas_row_x, deltas_row_y):
        row_x += delta_row_x
        row_y += delta_row_y
        key_to_coord = update_map(key_to_coord, row_x, row_y, row_len)

    key_to_value = {
        key: root_value + delta_x * coord[0] + delta_y * coord[1]
        for key, coord in key_to_coord.items()
    }
    key_to_color = {key: colors[value % 12] for key, value in key_to_value.items()}

    ltn_string += f"[Board{n}]\n"
    for key in range(len(key_to_coord)):
        value = key_to_value[key]
        color = key_to_color[key]
        ltn_string += f"Key_{key}={value}\n"
        ltn_string += f"Chan_{key}=1\n"
        ltn_string += f"Col_{key}={color}\n"
        if invert_sustain:
            ltn_string += f"CCInvert_{key}\n"

# uncomment for custom velocity curve, etc.
# ltn_string += "VelocityIntrvlTbl=1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 60 61 62 63 64 66 67 68 70 71 72 73 74 76 77 79 81 82 84 86 88 90 92 94 96 98 101 104 107 111 115 119 124 129 134 140 146 152 159 170 171 175 180 185 190 195 200 205 210 215 220 225 230 235 240 245 250 255 260 265 270 275 280 285 290 295 300 305 310 \n"
# ltn_string += "NoteOnOffVelocityCrvTbl=1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 63 64 65 66 68 69 70 72 73 74 76 77 79 80 82 84 85 87 88 90 92 94 96 97 99 101 103 105 108 110 112 114 117 119 121 124 127 \n"
# ltn_string += "FaderConfig=1 2 2 2 3 3 3 4 4 4 5 5 6 6 6 7 7 7 8 8 9 9 9 10 10 10 11 11 12 12 12 13 13 14 14 14 15 15 16 16 17 17 17 18 18 19 19 20 20 20 21 21 22 22 23 23 24 24 25 25 26 26 27 27 28 28 29 29 30 31 31 32 32 33 33 34 35 35 36 37 37 38 39 39 40 41 41 42 43 44 45 45 46 47 48 49 50 51 52 53 55 56 57 59 62 65 68 71 74 77 79 82 85 88 91 94 97 99 102 105 108 111 114 117 119 122 125 127 \n"
# ltn_string += "afterTouchConfig=0 2 3 5 6 8 9 10 12 13 14 16 17 18 20 21 22 24 25 26 27 28 30 31 32 33 34 36 37 38 39 40 41 43 44 45 46 47 48 49 50 51 52 53 54 55 57 58 59 60 61 62 63 64 65 66 67 68 69 70 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 85 86 87 88 89 90 91 92 92 93 94 95 96 97 98 99 99 100 101 102 103 104 104 105 106 107 108 108 109 110 111 112 112 113 114 115 116 116 117 118 119 120 120 121 122 123 123 124 125 126 126 127 \n"
# ltn_string += "LumaTouchConfig=0 1 2 2 3 3 3 4 4 4 5 5 5 6 6 7 7 7 8 8 8 9 9 10 10 10 11 11 11 12 12 13 13 13 14 14 15 15 15 16 16 17 17 18 18 18 19 19 20 20 21 21 22 22 22 23 23 24 24 25 25 26 26 27 27 28 28 29 29 30 30 31 32 32 33 33 34 34 35 36 36 37 37 38 39 39 40 41 41 42 43 43 44 45 46 47 47 48 49 50 51 52 53 53 54 56 57 58 60 61 63 65 68 70 73 75 78 81 84 87 90 94 98 102 107 113 121 127 "

file_name = f"mapping_{root_value}_{delta_x}_{delta_y}.ltn"
with open(file_name, "w") as f:
    f.write(ltn_string)
    print(f"ltn file saved to {file_name}")
print("-" * 80)
