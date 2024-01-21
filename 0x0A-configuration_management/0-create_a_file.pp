# A simple resource in puppet
file {'':
  ensure: file
  owner: www-data
  group: www-data
  mode: 0744
  content => "I love Puppet"
}
