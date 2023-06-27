# configure a new web server

exec { 'apt-get -y update && apt-get -y install nginx':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}

file_line { 'redirect_me':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => '    rewrite ^/redirect_me/?.*$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    after  => 'server_name _;'
}

file_line { '404_not_found':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => '    error_page 404 =404 /404.html;',
    after  => 'rewrite'
}

file { '/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!'
}

file { '/var/www/html/404.html':
    ensure  => present,
    content => 'Ceci n\'est pas une page'
}

exec { 'service nginx restart':
    path => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    user => 'root'
}
