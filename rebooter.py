try:
    import pexpect
    from pexpect.popen_spawn import PopenSpawn
except ModuleNotFoundError:
    print("Module pexpect is not installed")
    exit
import time
import shutil

if shutil.which("plink") != None:
    print("plink is installed")
else:
    print("plink is not installed")
    print("run winget putty.putty to install it from terminal")
    exit
    
ssh_tunnel = pexpect.popen_spawn.PopenSpawn('plink username@IPADDRESS -pw password -batch', encoding='utf-8')
time.sleep(5)
ssh_tunnel.sendline('reboot')
time.sleep(5)
ssh_tunnel.sendline('y')
time.sleep (5)
ssh_tunnel.expect(pexpect.EOF)
exit
