# Fix Nginx errors

exec { 'increase_nofile':
  command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx; sudo service nginx restart",
}
