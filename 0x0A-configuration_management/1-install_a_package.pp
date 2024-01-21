#!/usr/bin/pup
# This file installs flask python framework using pip3
package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
}
