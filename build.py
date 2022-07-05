import glob
import os
import shutil


def main() -> None:
    src_dir_paths = glob.glob("src/*")
    for src_dir_path in src_dir_paths:
        dest_dir_path = f'./dest/{src_dir_path.split("/")[-1]}'
        if not os.path.exists(dest_dir_path):
            os.mkdir(dest_dir_path)
        src_problem_dir_paths = glob.glob(f"{src_dir_path}/*")
        for src_problem_dir_path in src_problem_dir_paths:
            dest_problem_dir_path = f'./dest/{"/".join(src_problem_dir_path.split("/")[-2:])}'
            shutil.make_archive(dest_problem_dir_path,
                                format="zip", root_dir=src_problem_dir_path)


if __name__ == "__main__":
    main()
