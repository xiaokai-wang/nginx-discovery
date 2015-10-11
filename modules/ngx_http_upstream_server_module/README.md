语法说明
========

```
http {
    upstream place{
        server 127.0.0.1:8080 max_fails=0 fail_timeout=30s;
    }

    upstream testurl{
        server 127.0.0.1:9090 max_fails=0 fail_timeout=30s;

#       check interval=1000 rise=3 fall=2 timeout=3000 type=http default_down=false;
#       check_http_send "GET / HTTP/1.0\r\n\r\n";
#       check_http_expect_alive http_2xx http_3xx http_4xx;
    }

    server{
        listen 8888;
        server_name localhost;

        location =/server-status{
            return 200;
        }

        location =/upstream_add_server{
            upstream_add_server on;
        }

        location ~ "^(/2/|/)short_url/"{
            proxy_connect_timeout 3s;
            proxy_send_timeout 5s;
            proxy_read_timeout 5s;

            proxy_pass http://testurl;
        }

        location ~ "^(/2/|/)place/pois/tips"{
            proxy_connect_timeout 3s;
            proxy_send_timeout 5s;
            proxy_read_timeout 5s;

           proxy_pass http://place;
        }

        location ~ "^(/2/|/)proxy/darwin"{
            proxy_connect_timeout 3s;
            proxy_send_timeout 5s;
            proxy_read_timeout 5s;

            proxy_pass http://place;
        }

    }
}
```


配置项说明
==========

* upstream_add_server off or on;

    当是upstream_add_server off; 时，则关闭动态加减后端server接口；
    当是upstream_add_server on; 时，则开启动态加减后端server接口，可以动态扩容、缩容后端服务数；


设计说明
=========

    本模块设计时，天然支持健康监测模块，任何加减的后端节点server 都立即生效，并且立即开始进行健康监测.


接口说明
=========

* 动态加减后端server 格式基于json;

    加节点：
```
    curl "http://localhost:8888/upstream_add_server" -d "{\"upstream\":\"test\",\"server\":[\"10.77.108.242:8086\",\"10.77.108.242:8087\",\"10.77.108.242:8088\",\"10.77.108.242:8089\"],\"weight\":1,\"max_fails\":2,\"fail_timeout\":10,\"down\":0,\"backup\":0,\"method\":\"add\"}"
```
    减节点：
```
    curl "http://localhost:8888/upstream_add_server" -d "{\"upstream\":\"test\",\"server\":[\"10.77.108.242:8086\",\"10.77.108.242:8087\",\"10.77.108.242:8088\",\"10.77.108.242:8089\"],\"method\":\"del\"}"
```

    upstream:     后面跟具体服务的的host；

    server:       后面跟具体添加的节点ip:port;

    weight:       权重；

    max_fails:    失败次数；

    fail_timeout: 在此时间内连接失败max_fails 次后，在此时间内标记为不可用；

    method:       add or del;


    default value: weight=1 max_fails=2 fail_timeout=10 down=0 backup=0;


安装说明
=========

```
./configure -add-module=/path/to/ngx_http_upstream_server_module
make
make install
```


适用场景
=========

    此模块可以实现随时加减后端节点，并且立即生效，但是多nginx集群下可能存在潜在的不一致性，所以适用于规模较小的业务；

    或者结合其它存储服务，把所有的节点存储于服务中，结合其它脚本，实现动态的添加减节点.
