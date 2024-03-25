# Puppet Manifest for installing puppet-lint version 2.5.0

exec { 'install_puppet_lint':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0\n',
}

file { '/etc/puppetlabs/puppet/puppet.conf':
  ensure  => file,
  content => "[main]\nlogdir=/var/log/puppet\nvardir=/var/lib/puppet\nssldir=/var/lib/puppet/ssl\ncodedir=/etc/puppetlabs/code\n\n[agent]\nserver=puppet\npluginsync=true\nreport=true\nenvironment=production\n",
}

