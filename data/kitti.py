import util

def dump_dir(root_dir, split):
    dir_name = util.io.get_filename(root_dir)
    output_path = "datasets/%s.csv"%(dir_name)
    print(output_path)
    
    left_image_dir = util.io.join_path(root_dir, split, "left")
    left_image_paths = util.io.search("*.png", left_image_dir, file_only = True)
    right_image_paths = [util.str.replace_all(left_path, "left", "right") for left_path in left_image_paths]
    disp_paths = [util.str.replace_all(left_path, "left", "disp") for left_path in left_image_paths]

    lines = []
    for left_path, right_path, disp_path in zip(left_image_paths, right_image_paths, disp_paths):
        assert util.io.exists(right_path)
        assert util.io.exists(disp_path)
        line = util.str.join([left_path, right_path, disp_path], ",")
        lines.append(line)
        
    util.io.write_lines(output_path, lines, append_break = True)
    print("%d lines written to %s"%(len(lines), output_path))

if __name__ == "__main__":
    root_dirs = util.argv[1:]
    for root_dir in root_dirs:
        for split in ["training"]:
            dump_dir(root_dir, split)
