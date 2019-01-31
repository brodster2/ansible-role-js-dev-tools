import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def check_node_is_installed(host):
    nodejs = host.package("nodejs")
    assert nodejs.is_installed
    assert nodejs.version.startswith("8.12")


# def check_yarn_is_not_installed(host):
#     yarn = host.package("yarn")
#     assert not(yarn.is_installed)
