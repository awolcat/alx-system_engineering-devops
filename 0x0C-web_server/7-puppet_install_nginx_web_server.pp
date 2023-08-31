# Install nginx and configure reirect

package { 'install_nginx':
  ensure => installed,
  name   => 'nginx'
}

file { 'edit default site':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}

file_line { 'page redirect':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => '\n\nlocation /redirect_me {\n\t\treturn 301 https://albertmathenge.tech;\n\t}\n\n',
}

exec { 'restart nginx':
  command     => 'service nginx start',
  refreshonly => true,
}
