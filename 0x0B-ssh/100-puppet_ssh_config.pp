# set up clint cofig
include stdlib

file { '/home/doctware/.ssh':
  ensure => directory,
  owner  => 'doctware',
  group  => 'doctware',
  mode   => '0700',
}

file { '/home/doctware/.ssh/config':
  ensure => file,
  owner  => 'doctware',
  group  => 'doctware',
  mode   => '0600',
}

file_line { 'Turn off passwd auth':
  path    => '/home/doctware/.ssh/config',
  line    => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path    => '/home/doctware/.ssh/config',
  line    => '    IdentityFile ~/.ssh/school',
}
