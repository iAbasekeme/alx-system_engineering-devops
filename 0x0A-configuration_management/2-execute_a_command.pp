# A manifest that kills a process named killmenow.
exec {'pKill -f killmenow':
  provider  => 'shell'
}
