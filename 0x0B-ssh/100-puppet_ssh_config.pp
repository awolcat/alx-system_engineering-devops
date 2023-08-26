# Client ssh config file
file { 'usr ssh config':
  path               => '/etc/ssh/ssh_config',
  ensure             => file,
  mode               => '0600',
  source             => '2-ssh_config',
  source_permissions => ignore
}
