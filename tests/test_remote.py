import paramiko
def test_ssh_server02():
    s=paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect("192.168.85.128",username="root",key_filename="/root/.ssh/id_ed25519",look_for_keys=False,timeout=10)
    _,o,_=s.exec_command("hostname")
    assert o.read().decode().strip()=="rootops-server-02"
    s.close()
