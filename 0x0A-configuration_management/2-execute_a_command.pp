# A manifest that kills a process named killmenow.
exec { '/usr/bin/pkill killmenow':
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
}
