from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connectivity import get_db
from controller.syllabustopic_controller import (
    create_syllabus_topic_controller,
    get_all_syllabus_topics_controller,
    get_syllabus_topic_by_id_controller,
    update_syllabus_topic_controller,
    delete_syllabus_topic_controller,
)
from schemes.SyllabusTopic import (
    SyllabusTopicCreate,
    SyllabusTopicUpdate,
    SyllabusTopicResponse,
)

topic_router = APIRouter(
    prefix="/syllabus-topics",
    tags=["Syllabus Topics"],
)


@topic_router.post("/", response_model=SyllabusTopicResponse)
def create_topic(
    topic: SyllabusTopicCreate,
    db: Session = Depends(get_db),
):
    return create_syllabus_topic_controller(topic, db)


@topic_router.get("/", response_model=list[SyllabusTopicResponse])
def get_all_topics(
    db: Session = Depends(get_db),
):
    return get_all_syllabus_topics_controller(db)


@topic_router.get("/{topic_id}", response_model=SyllabusTopicResponse)
def get_topic(
    topic_id: int,
    db: Session = Depends(get_db),
):
    return get_syllabus_topic_by_id_controller(topic_id, db)


@topic_router.put("/{topic_id}", response_model=SyllabusTopicResponse)
def update_topic(
    topic_id: int,
    topic: SyllabusTopicUpdate,
    db: Session = Depends(get_db),
):
    return update_syllabus_topic_controller(topic_id, topic, db)


@topic_router.delete("/{topic_id}")
def delete_topic(
    topic_id: int,
    db: Session = Depends(get_db),
):
    return delete_syllabus_topic_controller(topic_id, db)