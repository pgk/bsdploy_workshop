from fabric import api as fab


def upload_website():
    fab.put('htdocs/*', '/usr/jails/webserver/usr/local/www/nginx/')
