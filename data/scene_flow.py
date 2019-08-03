import util

def dump_dir(root_dir):
    image_dir = util.io.join_path(root_dir, "frames_cleanpass")
    dir_name = util.io.get_filename(root_dir)
    output_path = "datasets/%s.csv"%(dir_name)
    print(output_path)
    
    left_image_paths = util.io.search("left/*.png", image_dir, file_only = True, recursive = True)
    right_image_paths = [util.str.replace_all(p, "left", "right") for p in left_image_paths]
    disp_paths = []
    for left_path in left_image_paths:
        disp_path = util.str.replace_all(left_path, "frames_cleanpass", "disparity")
        disp_path = util.str.replace_all(disp_path, ".png", ".pfm")
        disp_paths.append(disp_path)
    
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
        dump_dir(root_dir)
