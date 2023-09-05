exec { 'sudo apt-get install -y nginx':
  creates => '/var/www/html',
}

file_line { 'custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

exec { 'sudo service nginx restart' : }
