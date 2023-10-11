# Puppet script

$file = '/var/www/html/wp-settings.php'

# Replace string

exec { 'replace_string':
  command => "sed -i 's/phpp/php/g' ${file}",
  path    => ['/bin','/usr/bin']
}
