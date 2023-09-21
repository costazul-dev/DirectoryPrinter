import os


def generate_tree(path, file_to_write, prefix=""):
    """Generate the directory tree recursively."""

    if os.path.isdir(path):
        # Get the list of files and directories directly under 'path'.
        entries = os.listdir(path)
        entries.sort()
        for i, entry in enumerate(entries):
            # Use '|__' for the last item, and '|--' for the rest.
            new_prefix = prefix + ('|__ ' if i == len(entries) - 1 else '|-- ')
            file_to_write.write(prefix + entry + '\n')
            # Recursive call for directories
            generate_tree(os.path.join(path, entry), file_to_write, new_prefix)


def main():
    input_path = input("Enter the path to generate a file tree: ")
    output_file = input("Enter the name of the output file (e.g., tree.txt): ")

    # Check if the provided path is valid
    if not os.path.exists(input_path):
        print(f"The path '{input_path}' does not exist.")
        return

    # Generate the file tree
    with open(output_file, 'w') as f:
        f.write(f"File tree for '{input_path}':\n\n")
        generate_tree(input_path, f)

    print(f"File tree generated in '{output_file}'.")


if __name__ == "__main__":
    main()
