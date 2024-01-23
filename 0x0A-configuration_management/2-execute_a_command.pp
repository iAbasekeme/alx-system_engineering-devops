# A manifest that kills a process named killmenow.
exec { 'pkill killmenow':
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
  path        => '/usr/bin/',
}

