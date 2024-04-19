from sqlmodel import Session, select

from src.apis.tasks.models import Task
from src.configs.database import engine
from src.utils.logger import logger_config

logger = logger_config(__name__)


def seed_tasks():
    with Session(engine) as session:
        query = select(Task)
        results = session.exec(query)
        for result in results:
            session.delete(result)
        session.commit()


        task_1 = Task(
            task="Build base source code",
            status="doing"
        )
        task_2 = Task(
            task="Learning AWS SAA-C03",
            status="todo"
        )
        task_3 = Task(
            task="Reading email",
            status="done"
        )

        session.add(task_1)
        session.add(task_2)
        session.add(task_3)
        session.commit()

        session.refresh(task_1)
        session.refresh(task_2)
        session.refresh(task_3)

        logger.info("=========== MOCK DATA CREATED ===========")
        logger.info("Task 1 %s", task_1)
        logger.info("Task 2 %s", task_2)
        logger.info("Task 3 %s", task_3)
        logger.info("===========================================")
