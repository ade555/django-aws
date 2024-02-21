import pytest
import logging

logger = logging.getLogger(__name__)


payload = {  
    "task_name": "Wash Clothes",  
    "task_description": "Wash clothes in the washing machine",  
}
  
@pytest.mark.django_db  
def test_create_task(api_client) -> None:  
    """  
    Test the create task API  
    :param api_client:  
    :return: None  
    """  
    # Create a task  
    response_create = api_client.post("/api/tasks/", data=payload, format="json")  
    task_id = response_create.data["data"]["id"]  
    logger.info(f"Created task with id: {task_id}")  
    logger.info(f"Response: {response_create.data}")  
    assert response_create.status_code == 201  
    assert response_create.data["data"]["task_name"] == payload["task_name"]  

    # Read the task  
    response_read = api_client.get(f"/api/tasks/modify/{task_id}/", format="json")  
    logger.info(f"Read task with id: {task_id}")  
    logger.info(f"Response: {response_read.data}")
    assert response_read.status_code == 200  
    assert response_read.data["data"]["task_name"] == payload["task_name"]


@pytest.mark.django_db
def test_update_task(api_client) -> None:

    # Create a task  
    response_create = api_client.post("/api/tasks/", data=payload, format="json")  
    task_id = response_create.data["data"]["id"]  
    logger.info(f"Created task with id: {task_id}")  
    logger.info(f"Response: {response_create.data}")  
    assert response_create.status_code == 201  
    assert response_create.data["data"]["task_name"] == payload["task_name"]

    # Update the task
    payload["task_name"]="Buy books"
    response_update = api_client.patch(f"/api/tasks/modify/{task_id}/", data=payload, format="json")
    logger.info(f"Updated task with id: {task_id}")
    logger.info(f"Response: {response_update.data}")
    assert response_update.status_code == 201 
    assert response_update.data["data"]["task_name"] == payload["task_name"]

    # task not found
    response_update = api_client.patch(f"/api/tasks/modify/{task_id + 0.2}/", data=payload, format="json")
    logger.info(f"updated task with id {task_id + 0.2}")
    assert response_update.status_code == 404

@pytest.mark.django_db
def test_delete_task(api_client):

    # Create a task  
    response_create = api_client.post("/api/tasks/", data=payload, format="json")  
    task_id = response_create.data["data"]["id"]  
    logger.info(f"Created task with id: {task_id}")  
    logger.info(f"Response: {response_create.data}")  
    assert response_create.status_code == 201  
    assert response_create.data["data"]["task_name"] == payload["task_name"]

    # Delete the created task
    response_delete = api_client.delete(f"/api/tasks/modify/{task_id}/", data=payload, format="json")
    logger.info(f"Deleted task with ID {task_id}")
    assert response_delete.status_code == 204

    # Read the task to ensure it was deleted
    response_read = api_client.get(f"/api/tasks/modify/{task_id}/", format="json")
    assert response_read.status_code == 404

    # Check if task does not exist
    response_update = api_client.patch(f"/api/tasks/modify/{task_id + 0.2}/", data=payload, format="json")
    logger.info(f"updated task with id {task_id + 0.2}")
    assert response_update.status_code == 404
