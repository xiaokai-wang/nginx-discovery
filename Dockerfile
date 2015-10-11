#From registry.intra.test.com/test_rd_common/centos:6.6

RUN mkdir -p /src/nginx

COPY . /src/nginx

WORKDIR /src/nginx

RUN yum install -y gcc pcre-devel openssl openssl-devel

RUN ./configure --add-module=/src/nginx/modules/ngx_http_upstream_check_module \
                --add-module=/src/nginx/modules/nginx-upsync-module

RUN make && make install

WORKDIR /usr/local/nginx

RUN mkdir -p /usr/local/nginx/conf/upstream

RUN mkdir -p /usr/local/nginx/conf/vhost

EXPOSE 80

CMD ["/usr/local/nginx/sbin/nginx", "-c", "/usr/local/nginx/conf/nginx.conf"]
