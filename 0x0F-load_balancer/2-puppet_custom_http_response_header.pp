# create a custom HTTP header response

exec { 'apt-get -y update && apt-get -y install nginx':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
-> file_line { 'X-Served-By':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => "\tadd_header X-Served-By ${hostname};",
    after  => 'server_name _;'
}
-> exec { 'service nginx restart':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
