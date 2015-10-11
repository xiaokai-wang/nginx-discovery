Introduction
=============

Based on nginx-1.8.0, native supporting all nginx function. Add four modules, extending nginx function. Naming nginx-discovery.
nginx update upstream-backendlist, not need reloading nginx.

Feature
============

* ngx_http_upstream_server_module + ngx_http_upstream_check_module

    you can push backend servers to nginx, dynamic add/del servers to upstream-host. supporting health-checking.

* nginx-upsync-module + ngx_http_upstream_check_module

    nginx + consul, nginx pull upstream_conf from consul at regular time, supporting health-checking.

* ngx_http_upstream_dynamic_module

    upstream-host based on domain, nginx will resolve domain at regular time.

Specific information, please take a look at ./modules/$module_name/README.md.

Install
============

```push
./configure --add-module=/path/to/ngx_http_upstream_check_module --add-module=/path/to/ngx_http_upstream_server_module
make
make install
```

```pull
./configure --add-module=/path/to/ngx_http_upstream_check_module --add-module=/path/to/nginx-upsync-module
make
make install
```

```dns
./configure --add-module=/path/to/ngx_http_upsteam_dynamic_module
make
make install
```
