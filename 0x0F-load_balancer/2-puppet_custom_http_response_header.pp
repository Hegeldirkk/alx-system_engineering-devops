# install nginx on server
package { 'nginx':
  ensure  => installed,
}
# return a page that contains the string hello world
file { '/var/www/html/index.html':
  content => 'Hello World!',
}
# /redirect_me is redirecting to another page
file_line { 'writes redirection site':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen [::]:80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
# custom 404 page that contains the string Ceci n'est pas une page.
file_line { 'writes custom 404 site':
  ensure => 'present',
  path   => '/var/www/html/error404.html',
  after  => '/server_name _;',
  line   => 'error_page 404 /error404.html;\nlocation = /error404.html {\nroot /var/www/html;\ninternal;\n}',
}
# custom Nginx response header
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;',
}
# start service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
