import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ntp_service(host):

    os = host.system_info.distribution
    if os in ("ubuntu", "debian"):
        ntp_daemon = "ntp"
    if os in ("centos", "redhat"):
        ntp_daemon = "ntpd"

    assert host.service(ntp_daemon).is_running
    assert host.service(ntp_daemon).is_enabled
