import paramiko

host = "localhost"
port = 22
username ="priyadarshee"
password = "Subham@2003"
#create an object and connect to remote machine
client = paramiko.SSHClient()
#set the rule to handle the unknown host keys, _ or the first time connecting host keys
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=host,
    port = port,
    username=username,
    password=password
)
stdin,stdout,stderr = client.exec_command("whoami")
print(stdout.read().decode())
client.close()


