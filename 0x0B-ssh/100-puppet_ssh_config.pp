file { '/home/doctware/.ssh/config':
  ensure  => file,
  owner   => 'doctware',
  group   => 'doctware',
  mode    => '0600',
  content => @(EOF)
Host 52.91.157.23
    User ubuntu
    IdentityFile ~/.ssh/config
    PasswordAuthentication no
| EOF
}
