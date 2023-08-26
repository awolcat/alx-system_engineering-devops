# Kill killmenow
exec {'kill killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif => '/usr/bin/pgrep -f killmenow'
}
