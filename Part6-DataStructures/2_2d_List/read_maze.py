"""
Python Data Structures - A Game-Based Approach
Reading a maze from a text file
"""
import os

def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


def get_text_files(folder_path):
    # get a list of all files and folders in the folder
    files_and_folders = os.listdir(folder_path)

    # Use a list comprehension to filter only the text files (ending with .txt)
    return [file for file in files_and_folders if file.endswith(".txt")]


if __name__ == "__main__":
    maze_files = get_text_files("mazes")

    for file_name in maze_files:
        maze = read_maze(f"mazes/{file_name}")
        print(f"----------Showing of the file: {file_name}")
        for row in maze:
            print(row)

    print(f"--------------------------------------\nTOTAL MAZES: {len(maze_files)}")
