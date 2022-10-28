# configure new Server

package { 'nginx':
  ensure => 'installed',
}
$host=$hostname
$conf = "server {
	listen   80 default_server;
	listen   [::]:80 default_server;
	root     /var/www/html;
	index    index.html index.htm;
	location /redirect_me {
		return 301 https://www.youtube.com;
	}
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html;
	}
	error_page 404 /custom_404.html;
	location = /custom_404.html {
		root /var/www/errors/;
		internal;
	}
	location / {
                add_header X-Served-By ${host};
        }
		
}
"
file {'/data/':
  ensure => 'directory',
  group  => 'ubuntu',
  owner  => 'ubuntu'
}
file {'/data/web_static/':
  ensure => 'directory',
  group  => 'ubuntu',
  owner  => 'ubuntu'
}
file {'/data/web_static/releases/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file {'/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}
file {'/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}

file {'/data/web_static/current':
  ensure => 'link',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  target => '/data/web_static/releases/test/'
}
file {'/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $conf
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => 'Holberton School',
  owner   => 'ubuntu',
  group   => 'ubuntu'
}
file { '/var/www/errors/custom_404.html':
  ensure  => 'present',
  content => 'Ceci n\'est pas une page'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
