from sqlalchemy.orm import Session
from fastapi import Depends

from database.connectivity import get_db
from service.SyllabusTopic_service import (
    create_syllabus_topic,
    get_all_syllabus_topics,
    get_syllabus_topic_by_id,
    update_syllabus_topic,
    delete_syllabus_topic,
)
from schemes.SyllabusTopic import (
    SyllabusTopicCreate,
    SyllabusTopicUpdate,
)


def create_syllabus_topic_controller(
    topic: SyllabusTopicCreate,
    db: Session,
):
    return create_syllabus_topic(db, topic)


def get_all_syllabus_topics_controller(
    db: Session,
):
    return get_all_syllabus_topics(db)


def get_syllabus_topic_by_id_controller(
    topic_id: int,
    db: Session,
):
    return get_syllabus_topic_by_id(db, topic_id)


def update_syllabus_topic_controller(
    topic_id: int,
    topic: SyllabusTopicUpdate,
    db: Session,
):
    return update_syllabus_topic(db, topic_id, topic)


def delete_syllabus_topic_controller(
    topic_id: int,
    db: Session,
):
    return delete_syllabus_topic(db, topic_id)