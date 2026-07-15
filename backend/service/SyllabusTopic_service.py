from sqlalchemy.orm import Session

from models.syllabus_topics import SyllabusTopic
from schemes.SyllabusTopic import (
    SyllabusTopicCreate,
    SyllabusTopicUpdate,
)
from exceptions.httpexception import not_found


def create_syllabus_topic(db: Session, topic: SyllabusTopicCreate):
    new_topic = SyllabusTopic(**topic.model_dump())

    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return new_topic


def get_all_syllabus_topics(db: Session):
    return (
        db.query(SyllabusTopic)
        .filter(SyllabusTopic.is_active == True)
        .all()
    )


def get_syllabus_topic_by_id(db: Session, topic_id: int):
    topic = (
        db.query(SyllabusTopic)
        .filter(
            SyllabusTopic.id == topic_id,
            SyllabusTopic.is_active == True,
        )
        .first()
    )

    if not topic:
       not_found("Syllabus Topic not found")

    return topic


def update_syllabus_topic(
    db: Session,
    topic_id: int,
    topic_data: SyllabusTopicUpdate,
):
    topic = (
        db.query(SyllabusTopic)
        .filter(
            SyllabusTopic.id == topic_id,
            SyllabusTopic.is_active == True,
        )
        .first()
    )

    if not topic:
        not_found("Syllabus Topic not found")

    update_data = topic_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(topic, key, value)

    db.commit()
    db.refresh(topic)

    return topic


def delete_syllabus_topic(db: Session, topic_id: int):
    topic = (
        db.query(SyllabusTopic)
        .filter(
            SyllabusTopic.id == topic_id,
            SyllabusTopic.is_active == True,
        )
        .first()
    )

    if not topic:
        not_found("Syllabus Topic not found")

    topic.is_active = False

    db.commit()

    return {"message": "Syllabus Topic deleted successfully"}