import re


def parse_syllabus(text: str):
    topics = []

    current_unit_no = None
    current_unit_name = None
    current_chapter_no = None
    current_chapter_name = None

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines:

        # PART 1 / PART 2
        if "GANITA PRAKASH" in line.upper():
            current_unit_no = current_unit_no + 1 if current_unit_no else 1
            current_unit_name = line
            continue

        # Chapter
        chapter_match = re.match(r"Chapter\s+(\d+)\.\s+(.*)", line)

        if chapter_match:
            current_chapter_no = int(chapter_match.group(1))
            current_chapter_name = chapter_match.group(2).strip()
            continue

        # Topics (PyMuPDF is extracting bullets as G)
        if line.startswith("G") or line.startswith("•") or line.startswith("-"):
            topic = line[1:].strip()

            topics.append(
                {
                    "unit_no": current_unit_no,
                    "unit_name": current_unit_name,
                    "chapter_no": current_chapter_no,
                    "chapter_name": current_chapter_name,
                    "topic_name": topic,
                    "content": topic,
                }
            )

    return topics