# changing OS cofig to give no error when loggiing in as a ggiven user

exec { 'change soft limit':
  command  => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf',
  provider => shell,
  unless   => 'grep -q "holberton\ssoft\tnofile\t10000" /etc/security/limits.conf',
}

exec { 'change hard limit':
  command  => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t100000/" /etc/security/limits.conf',
  provider => shell,
  unless   => 'grep -q "holberton\shard\tnofile\t100000" /etc/security/limits.conf',
}
