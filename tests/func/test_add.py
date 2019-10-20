import pytest

import tasks

from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield

    tasks.stop_tasks_db()


def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    new_task = Task('do something')
    task_id = tasks.add(new_task)

    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)
    task_from_db = tasks.get(task_id)

    assert task_from_db.id == task_id


@pytest.mark.skipif(tasks.__version__ < '0.2.0', reason='misunderstood the API')
def test_unique_id():
    """Calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()

    assert id_1 != id_2


def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    uid = tasks.unique_id()

    assert uid not in ids
