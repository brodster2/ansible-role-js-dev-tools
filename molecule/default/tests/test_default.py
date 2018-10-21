import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def check_node_is_installed(host):
    nodejs = host.package("nodejs")
    assert nodejs.is_installed
    assert nodejs.version.startswith("8.12")


def check_yarn_is_installed(host):
    yarn = host.package("yarn")
    assert yarn.is_installed
    assert yarn.version.startswith("1.10")


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
