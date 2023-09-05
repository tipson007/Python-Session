#

Install the SSH server package openssh by using the dnf command:
# dnf install openssh-server
Start the sshd daemon and set to start after reboot:
# systemctl start sshd
# systemctl enable sshd
Confirm that the sshd daemon is up and running:
# systemctl status sshd
Open the SSH port 22 to allow incoming traffic:
# firewall-cmd --zone=public --permanent --add-service=ssh
# firewall-cmd --reload
Optionally, locate the SSH server man config file /etc/ssh/sshd_config and perform custom configuration.

Every time you make any change to the /etc/ssh/sshd_config configuration file reload the sshd service to apply changes:
# systemctl reload sshd