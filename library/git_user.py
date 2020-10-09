#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type


from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str'),
            email=dict(type='str'),
            force=dict(type='bool')
        ),
        supports_check_mode=True,
    )
    git_path = module.get_bin_path('git', True)

    params = module.params
    # We check error message for a pattern, so we need to make sure the
    # messages appear in the form we're expecting.
    # Set the locale to C to ensure consistent messages.
    module.run_command_environ_update = dict(
        LANG='C', LC_ALL='C', LC_MESSAGES='C', LC_CTYPE='C')

    if params['name']:
        name = params['name']
    else:
        name = None

    if params['email']:
        email = params['email']
    else:
        email = None

    if params['force']:
        force = params['force']
    else:
        force = None

    changed = False

    # Get current name
    args = [git_path, 'config', '--global', 'user.name']
    (rc, out, err) = module.run_command(args)
    if rc == 0:
        current_name = out.strip()
    elif rc == 1:
        # Value not set
        current_name = None
    else:
        module.fail_json(msg='Error quering user.name',
                         rc=rc,
                         stdout=out,
                         stderr=err,
                         cmd=' '.join(args))

    # Set new name
    set_username = (
        force or current_name is None) and name not in (
        '', None, current_name)
    if set_username:
        changed = True
        new_name = name
        if not module.check_mode:
            args = [git_path, 'config', '--global', 'user.name', new_name]
            (rc, out, err) = module.run_command(args)
            if rc != 0:
                module.fail_json(msg='Error setting user.name',
                                 rc=rc,
                                 stdout=out,
                                 stderr=err,
                                 cmd=' '.join(args))
    else:
        new_name = current_name

    # Get current email
    args = [git_path, 'config', '--global', 'user.email']
    (rc, out, err) = module.run_command(args)
    if rc == 0:
        current_email = out.strip()
    elif rc == 1:
        # Value not set
        current_email = None
    else:
        module.fail_json(msg='Error querying user.email',
                         rc=rc,
                         stdout=out,
                         stderr=err,
                         cmd=' '.join(args))

    # Set new email
    set_email = (
        force or current_email is None) and email not in (
        '', None, current_email)
    if set_email:
        changed = True
        new_email = email
        if not module.check_mode:
            args = [git_path, 'config', '--global', 'user.email', new_email]
            (rc, out, err) = module.run_command(args)
            if rc != 0:
                module.fail_json(msg='Error setting user.email',
                                 rc=rc,
                                 stdout=out,
                                 stderr=err,
                                 cmd=' '.join(args))
    else:
        new_email = current_email

    module.exit_json(
        changed=changed,
        result=dict(
            changed=changed,
            new_name=new_name,
            previous_name=current_name,
            playbook_name=module.params['name'],
            new_email=new_email,
            previous_email=current_email,
            playbook_email=module.params['email']
        )
    )


if __name__ == '__main__':
    main()
