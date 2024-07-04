# Ensure the nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the nginx service is running
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

# Configure the default nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create the index.html file with "Hello World!"
file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Ensure the nginx site is enabled
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}
