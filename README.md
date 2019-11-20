Ansible Role: Git User
======================

[![Build Status](https://travis-ci.com/gantsign/ansible_role_git_user.svg?branch=master)](https://travis-ci.com/gantsign/ansible_role_git_user)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.git__user-blue.svg)](https://galaxy.ansible.com/gantsign/git_user)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_git_user/master/LICENSE)

Role to configure the username and email address for users of Git.

Requirements
------------

* Ansible >= 2.6

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

        * Fedora

            * 31

    * SUSE Family

        * openSUSE

            * 15.1

    * Note: other versions are likely to work but have not been tested.

* Docker (already installed)

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# Users to configure the Git user name and email address for
users: []
```

Users are configured as follows:

```yaml
users:
  - username: # Unix user name
    git_user_name: # Optional. User name to use for Git
    git_user_email: # Optional. Email address to use for Git
    git_user_force: # Optional. (yes/no) wether to overwrite the current values
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.git_user
      users:
        - username: joe
          git_user_name: Joe Bloggs
          git_user_email: joe@example.com
          git_user_force: no
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
