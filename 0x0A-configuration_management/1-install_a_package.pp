# Install flask using pip3 must be version 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
