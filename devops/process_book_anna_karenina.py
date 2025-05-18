import os
import re
import textwrap

def split_book_by_chapter(input_path: str, output_dir: str):
    # Read an entire book
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all chapters (assuming they start with a bunch of multilines)
    chapters_with_junk = re.split(r'(?:^\n{4,}\s+)', content, flags=re.MULTILINE)
    chapters = [s for s in chapters_with_junk if len(s) > 100]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, chapter in enumerate(chapters):
        filename = f"anna-karenina-part-1/chapter-{i}.txt"
        filepath = os.path.join(output_dir, filename)
        final_text = chapter.strip()
        # Wrap each line separately
        wrapped_lines = []
        for line in final_text.splitlines():
            wrapped_lines.append(textwrap.fill(line, width=70))

        # Join wrapped lines back together
        final_text = "\n".join(wrapped_lines)

        # Replace hart to type characters
        # final_text = final_text.replace('—', '-')
        # final_text = final_text.replace('“', '"')
        # final_text = final_text.replace('”', '"')
        # final_text = final_text.replace('’', "'")
        with open(filepath, 'w', encoding='utf-8') as out:
            out.write(final_text)
        print(f"Wrote {filename}")

if __name__ == "__main__":
    input_file = "tolstoj_lew_nikolaewich-text_0080-part1.txt"
    output_folder = "../public"
    split_book_by_chapter(input_file, output_folder)
