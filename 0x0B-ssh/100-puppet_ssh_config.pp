# Client ssh config file
augeas { 'ssh_config':
  incl    => '/etc/ssh/ssh_config',
  lens    => 'Ssh.lns',
  changes => [
      "touch Host/PasswordAuthentication",
      "set Host/PasswordAuthentication no",
      "touch Host/IdentityFile",
      "set Host/IdentityFile ~/.ssh/school",
    ],
}
