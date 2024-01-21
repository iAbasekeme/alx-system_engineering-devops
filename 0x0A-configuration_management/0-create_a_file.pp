# A simple resource in puppet
file { '/tmp/school':
  ensure: file
  owner: www-data
  group: www-data
  mode: 0744
  content => "I love Puppet"
}
