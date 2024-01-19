# 2-execute_a_command.pp

# Define an exec resource to kill the "killmenow" process
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
