import re


UNIT_PATTERN = re.compile(
    r"^(?:#+\s*)?(.*?)(PART|UNIT|MODULE|SECTION|THEME|VOLUME|BOOK|भाग|इकाई)\s*([A-Za-z0-9IVX]+)$",
    re.IGNORECASE,
)

CHAPTER_PATTERN = re.compile(
    r"^(?:#+\s*)?(Chapter|Ch|Lesson|Topic|अध्याय|पाठ)\s*([A-Za-z0-9IVX]*)[:.\-\s]*(.*)$",
    re.IGNORECASE,
)

TOPIC_PATTERN = re.compile(
    r"^(?:•|-|\*|▪|◦|○|G|\d+\.\s|\d+\)\s|[a-zA-Z]\)\s)(.+)"
)


def parse_syllabus(text: str):
    topics = []

    current_unit_no = None
    current_unit_name = None

    current_chapter_no = None
    current_chapter_name = None

    current_topic = None

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    for line in lines:

        # ---------------- UNIT ----------------
        unit_match = UNIT_PATTERN.match(line)

        if unit_match:
            current_unit_no = unit_match.group(3)
            current_unit_name = line.strip()
            current_chapter_no = None
            current_chapter_name = None
            current_topic = None
            continue

        # ---------------- CHAPTER ----------------
        chapter_match = CHAPTER_PATTERN.match(line)

        if chapter_match:
            current_chapter_no = chapter_match.group(2)
            current_chapter_name = chapter_match.group(3).strip() or line
            current_topic = None
            continue

        # ---------------- TOPIC ----------------
        topic_match = TOPIC_PATTERN.match(line)

        if topic_match:

            current_topic = {
                "unit_no": current_unit_no,
                "unit_name": current_unit_name,
                "chapter_no": current_chapter_no,
                "chapter_name": current_chapter_name,
                "topic_name": topic_match.group(1).strip(),
                "content": topic_match.group(1).strip(),
            }

            topics.append(current_topic)
            continue

        # ---------------- CONTENT ----------------
        if current_topic:
            current_topic["content"] += "\n" + line

    return topics