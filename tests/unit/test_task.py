from tasks import Task


def test_asdict():
    """_asdict() should return a dictionary."""

    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21
    }

    assert t_dict == expected


def test_replace():
    """replace() shoudl change passed in fields."""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)

    assert t_after == t_expected


def test_defaults():
    """Check .field functionality of namedtuple."""
    t1 = Task()
    t2 = Task(None, None, False, None)

    assert t1 == t2


def test_member_access():
    t = Task('buy milk', 'brian')

    actual = (t.summary, t.owner, t.done, t.id)
    expected = ('buy milk', 'brian', False, None)

    assert actual == expected
