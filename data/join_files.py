import util
files = util.argv[1:]
lines = []
output_name = []

for path in files:
    name = util.io.get_filename(path).split(".")[0]
    output_name.append(name)
    file_lines = util.io.read_lines(path)
    lines.extend(file_lines)
    
output_name = util.str.join(output_name, "_")
output_path = util.io.join_path("datasets", output_name + ".csv")
util.io.write_lines(output_path, lines, append_break=False)
print(len(lines), "lines written to", output_path)