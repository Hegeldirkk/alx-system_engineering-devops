#fix stack so as to get 0 failed requests

service { 'nginx stop':
  ensure => stopped;
}

exec { 'fix nginx':
  command => "sed -i 's/15/2000/g' /etc/default/nginx",
  path    => ['/bin'],
}

service { 'nginx':
  ensure => running,
}
