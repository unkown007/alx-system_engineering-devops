# enable the server to not authenticate with password
file_line { 'Turn off passwd auth':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no'
}

# enable the client ssh use private key
file_line { 'Declare identity file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school'
}
