# kills a process naed killemenow

exec { 'pkill -f killmenow':
    path => '/usr/bin:/bin'
}
