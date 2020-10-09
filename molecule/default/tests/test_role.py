import pytest


def test_name_set(host):
    name = host.check_output('sudo --set-home --user test_usr1 '
                             'git config user.name')
    assert name.strip() == 'Test User1'


def test_email_set(host):
    email = host.check_output('sudo --set-home --user test_usr1 '
                              'git config user.email')
    assert email.strip() == 'test1@example.com'


@pytest.mark.parametrize('username', [
    'test_usr2',
    'test_usr3',
])
def test_name_not_set(host, username):
    cmd = host.run('sudo --set-home --user %s '
                   'git config user.name',
                   username)
    assert cmd.rc != 0


@pytest.mark.parametrize('username', [
    'test_usr2',
    'test_usr3',
])
def test_email_not_set(host, username):
    cmd = host.run('sudo --set-home --user %s '
                   'git config user.email',
                   username)
    assert cmd.rc != 0


def test_name_not_overridden(host):
    name = host.check_output('sudo --set-home --user test_usr4 '
                             'git config user.name')
    assert name.strip() == 'Existing Name'


def test_email_not_overridden(host):
    email = host.check_output('sudo --set-home --user test_usr4 '
                              'git config user.email')
    assert email.strip() == 'existing@example.com'


def test_name_overridden(host):
    name = host.check_output('sudo --set-home --user test_usr5 '
                             'git config user.name')
    assert name.strip() == 'Test User5'


def test_email_overridden(host):
    email = host.check_output('sudo --set-home --user test_usr5 '
                              'git config user.email')
    assert email.strip() == 'test5@example.com'
