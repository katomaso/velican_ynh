# Velican - a pelican blog engine

Velican installs pelican, basic theme and configuration for a blog for given `$domain`,
and a WebDAV endpoint on the URL `$domain/content`.

It uses default username admin with user provided by the user during installation.

Velican also provides a systemd service that watches for file `.publish` not to be
empty or existing. If the file cease to exist or is truncated then blog regeneration
is executed and the log is written into the `.publish` file.

## Logic

Installation creates three directories with diefferent purpose

- `/var/www/{APP_ID}` is `www-data` readable, has sticky g-bit and initially empty
- `/home/yunohost.app/{APP_ID}` contains pelican's theme and config files, owner is `APP_ID` user
- `/home/yunohost.app/{APP_ID}/content` is `www-data` writable and WebDAV points there

Once `/home/yunohost.app/{APP_ID}/content/.publish` is removed or emptied then regenerate
the blog and point output to `/var/www/{APP_ID}`.