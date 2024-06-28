# Install a pacckage with puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
