# Client ssh config file
augeas { 'ssh_config':
  incl    => '/etc/ssh/ssh_config',
  lens    => 'Ssh',
  changes => [
      "touch /etc/ssh/ssh_config/PasswordAuthentication",
      "set /etc/ssh/ssh_config/PasswordAuthentication no",
      "touch /etc/ssh/ssh_config/IdentityFile",
      "set /etc/ssh/ssh_config/IdentityFile ~/.ssh/school",
    ],
}
