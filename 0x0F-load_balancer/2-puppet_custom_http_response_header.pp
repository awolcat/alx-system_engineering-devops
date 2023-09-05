# Configure new server with nginx
# Install nginx
exec { 'sudo apt-get install -y nginx':
  creates => '/var/www/html',
}

# Modify site config
file_line { 'custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}
# Restart nginx
exec { 'sudo service nginx restart' : }
