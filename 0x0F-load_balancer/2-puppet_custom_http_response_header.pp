# Ensure the package 'nginx' is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the service 'nginx' is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Manage the Nginx configuration file to add the custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Create a template file for the Nginx configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("EOF"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.nginx-debian.html;

    server_name _;

    location / {
        add_header X-Served-By <%= @hostname %>;
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        internal;
    }
}
    | EOF
}

# Create the custom index.html with "Hello World!"
file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => 'Hello World!',
}

# Create the custom 404 page with "Ceci n'est pas une page"
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}
