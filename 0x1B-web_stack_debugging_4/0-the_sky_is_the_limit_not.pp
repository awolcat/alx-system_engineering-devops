# Increase nginx capacity

# Stop nginx

# exec {'stop-nginx':
#   command => 'sudo service nginx stop',
#   path    => '/usr/bin/'
# }

# Reconfigure nginx

augeas { 'nginx.conf':
  incl    => '/etc/nginx/nginx.conf',
  lens    => 'Nginx.lns',
  changes => [
                'ins worker_rlimit_nofile after worker_processes',
                'set worker_rlimit_nofile 16384',
                'set worker_processes 8',
                'rm events/#',
                'ins multi_accept after events/worker_connections',
                'set events/multi_accept on',
                'set events/worker_connections 8192',
        ],
}

# Restart nginx

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
