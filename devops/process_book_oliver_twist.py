import os
import re

def split_book_by_chapter(input_path: str, output_dir: str):
    # Read an entire book
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all chapters (assuming they start with ' CHAPTER' on a new line)
    chapters = re.split(r'(?:^ CHAPTER\s+)', content, flags=re.MULTILINE)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, chapter in enumerate(chapters):
        filename = f"oliver-twist/chapter-{i}.txt"
        filepath = os.path.join(output_dir, filename)
        final_text = 'CHAPTER ' + chapter.strip()
        # Replace hart to type characters
        final_text = final_text.replace('—', '-')
        final_text = final_text.replace('“', '"')
        final_text = final_text.replace('”', '"')
        final_text = final_text.replace('’', "'")
        with open(filepath, 'w', encoding='utf-8') as out:
            out.write(final_text)
        print(f"Wrote {filename}")

if __name__ == "__main__":
    input_file = "pg730.txt"
    output_folder = "../public"
    split_book_by_chapter(input_file, output_folder)
