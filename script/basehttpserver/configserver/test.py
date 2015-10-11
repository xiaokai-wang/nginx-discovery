#!/usr/bin/python
import BaseHTTPServer
import SimpleHTTPServer
import urlparse
import threading
import random
import getopt
import SocketServer
import socket
import time
import sys

class ThreadingSimpleServer(SocketServer.ThreadingMixIn,BaseHTTPServer.HTTPServer):
        pass

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        #protocol_version = "HTTP/1.1"

        def do_HEAD(s):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
        def do_POST(self):
                self.do_GET()
        def do_GET(self):
                """Respond to a GET request."""
                parsed_path = urlparse.urlparse(self.path)
		ctime=str(int(time.time()))
		message = '{"retcode":20000000,"msg":"","data":{"meta":{"etag":"a44ef0c19c52f559919e5e137c69f73f","expire":600,"ctime":'+ctime+'},"data":{"main":{"log":{"heartbeatlog":false,"heartbeatlog_on_update_config":false,"accesslog":false,"errorlog":true,"timelog":true,"facility":"local4","signedkey":"130103e2ebdce95e61dc8d148b777f59"},"sub":{"no_remote_validate_status":[20,30,50],"no_need_renew_status":[20,30,40,50]},"renew_sid":{"after_ctime":86400,"before_etime":0},"session":{"force_redirect_on_need_verify":null},"visitor":[],"time":{"sample":{"check_login_status":{"percent":0,"max":100}}},"authinfo_disable":[]},"counter":{"http_validate_error":{"period":300,"max":20,"duration":300},"http_destroy_error":{"period":300,"max":20,"duration":300},"memcache_error":{"period":300,"max":20,"duration":300},"dns_lookup_error":{"period":300,"max":20,"duration":300},"http_sus_validate_error":{"period":300,"max":20,"duration":300}},"res":{"cache":[{"host":"xd.wccs.mars.grid.sina.com.cn","port":"2888","attr":{"status":"ok"}}],"http":{"create":"http:\/\/i.session.sso.sina.com.cn\/api\/session\/create","destroybysid":"http:\/\/i.session.sso.sina.com.cn\/api\/session\/destroybysid","validate":"http:\/\/i.session.sso.sina.com.cn\/api\/session\/validate","querybysid":"http:\/\/i.session.sso.sina.com.cn\/api\/session\/querybysid","login":"http:\/\/login.sina.com.cn\/sso\/login.php","logout":"http:\/\/login.sina.com.cn\/sso\/logout.php","validate_ticket":"http:\/\/ilogin.sina.com.cn\/sso\/ticket\/st\/validate","getsso":"http:\/\/ilogin.sina.com.cn\/api\/getsso.php","checkgsid":"http:\/\/i.login.weibo.cn\/login\/check","destroygsid":"http:\/\/i.login.weibo.cn\/login\/destory","verify_sguide":"http:\/\/login.sina.com.cn\/sguide\/sguide.php","sus_validate":"http:\/\/i.sn.sina.com.cn\/validate","sus_destroy":"http:\/\/i.sn.sina.com.cn\/destroy","create_visitor":"http:\/\/passport.weibo.com\/visitor\/visitor"},"udp":{"info":[{"host":"10.13.24.23","port":"514","enable":true}],"error":[{"host":"10.13.24.23","port":"514","enable":true}]}},"key":{"suesup":{"v0":{"pub_key":"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDuRbH5Nj\/E+KcPO2cqDyb\/QiYy\nXCQh2bR31X\/K2EyaqtAveGwvQLIum5yG9PrCjfwaMLnI4pRIufAR0jfAyS+riGwx\nWHvQoB0mgt2dBwzf59jTJBriGrMgC5ZhTCAVLPnRmBQsZ\/\/ArMZOHeULn4x4pK8o\nV23eAA6wHPOLwkchHQIDAQAB\n-----END PUBLIC KEY-----\n"},"v1":{"pub_key":"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcU\/MAqgkaLQhirRlcEEBqP4IR\nLAdjO0MuarU6pzfKfzJRm5HF+QkAC0+7Ws17SEn7UpGyugKMULNhsxTPerMPAo2E\nTg0sbWmc4x94W7kMTUnkYXDqx\/HjR1IxhKl\/pEQqiNiRx0HCgTs+boc7VLm2eSSY\nAsz\/KJpJsRCnko3mBQIDAQAB\n-----END PUBLIC KEY-----"}},"suw":{"v0":{"pub_key":"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcwXyK0SP5y6OTk0y5yvWkNP0\/\nuGqnu5kIWuki+Ru1DtQ9FNzn1Itj4Y4JcLDVS9qaVg2gt6BkaMPUUAJa59dOcelN\naOv1O5iWtOADp+8zN9sGqm\/adcP4WruVdBVdV1fu2eb\/SKj3vOcNrWKMblkobxgE\nW33MeLFSQRioP1JEwwIDAQAB\n-----END PUBLIC KEY-----"}},"sub":{"v1":{"key":"ac94e2b8f9294bb911c3e424efc593e4","pub_key":"-----BEGIN PUBLIC KEY-----\nMFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAL6\/3mQv38O5i63P5IlK0HplFXpbAEpv\nrcpOhwSpmTGZgg70M2w+70M27Z+b\/mhn8\/KIso4wRI1pgFvSci4RofECAwEAAQ==\n-----END PUBLIC KEY-----"},"v2":{"key":"ac94e2b8f9294bb911c3e424efc593e4","pub_key":"-----BEGIN PUBLIC KEY-----\nMDAwDQYJKoZIhvcNAQEBBQADHwAwHAIVANMFNdju7jKXQX5qGqfRrdRBuZ2BAgMB\nAAE=\n-----END PUBLIC KEY-----"},"v3":{"key":"e974ebd51e0a9b47ad5391b5e6bfdb0b","pub_key":"-----BEGIN PUBLIC KEY-----\nMDAwDQYJKoZIhvcNAQEBBQADHwAwHAIVAKKhpe4HLgCcNxOKKNWNcSKzaVppAgMB\nAAE=\n-----END PUBLIC KEY-----"}},"subp":{"v2":"uAL715W8e3jJCcNU0lT_FSXVgxpbEDdQ4vKaIOH2GBPtfzqsmYZo-wRM9i6hynrk=","v3":"5WFh28sGziZTeS1lBxCK-HgPq9IdMUwknybo.LJrQD3uj_Va7pE0XfcNR4AOYvm6t"},"checkgsid":"xkmn&*@654rx"},"log":{"accesslog":{"_SERVER":["HTTP_USER_AGENT","REQUEST_URI","test"],"_REQUEST":["test"],"_COOKIE":["test"]},"errorlog":{"SERVER":["HTTP_USER_AGENT"],"REQUEST":[],"COOKIE":[]},"slowlog":{"mc":{"timeout":500},"http":{"timeout":500},"dns":{"timeout":500}},"heartbeatlog":{"min":"1.0.0","max":"n.0.1","in":[]},"rule":{"accesslog":{"byuid":{"model":{"mod":{"option":[{"max":"10","mod":[1,3,5]}],"enable":true},"ereg":{"option":{"six_num":"#^[1-9][0-9]{5}$#"},"enable":true}},"enable":false},"byip":{"model":{"in":{"option":{"ip":["10.73.56.0\/24","10.75.75.75\/32"]},"enable":true}},"enable":false}}}},"domain":{".sina.com.cn":1,".weibo.com":2,".sina.cn":3,".weibo.cn":4,".kanyouxi.cn":48,".kanyouxi.com":49,".kanyouxi.com.cn":50,".97973.com":51,".weicaifu.com":52},"idc":{"xd":1,"ja":2,"yf":3,"tc":4,"yhg":5,"ft":6,"yz":7,"bx":8,"cp":9,"tp":10,"yq":11,"lx":12,"zjm":13,"edu":14,"ws":15,"csk":16,"tj":48,"sd":49,"sh":50,"gz":80,"yt":81,"sb":82,"hk":96},"timeout":{"mc":{"connect_timeout":1000,"send_timeout":1000,"recv_timeout":1000},"http":{"timeout":2000}},"sid":{"data_type_map":{"uid":[],"username":[],"from":[],"etime":{"pack":"timestamp"},"domain":{"pack":"c2"},"savestate":{"pack":"c1"},"logintype":{"pack":"c1"},"idc":{"pack":"c1"},"rand":[],"clienttype":{"pack":"c1"}}},"session":{"storage_map":{"domain":{"index":1,"pack":"c2"},"ctime":{"index":2,"pack":"timestamp"},"idc":{"index":3,"pack":"c1"},"status":{"index":4,"pack":"c2","default":0},"ip":{"index":5,"pack":"ip"},"ua":{"index":6,"pack":"c4"},"etime":{"index":7,"pack":"timestamp"},"mid":{"index":8,"pack":"c*"},"appid":{"index":9,"pack":"c4"},"flag":{"index":10,"pack":"c2","default":0},"username":{"index":11},"from":{"index":12},"logintype":{"index":13},"savestate":{"index":14,"pack":"c1"},"clienttype":{"index":15,"pack":"c1"},"verify_flag":{"index":16,"pack":"c1"},"entry":{"index":17,"pack":"c2"},"ac":{"index":18,"pack":"c1"},"tid":{"index":19,"transform":"tid"},"appkey":{"index":20,"pack":"c*","transform":"appkey"},"psid":{"index":21,"pack":"c*"}}}}}}'
#                message = '{"retcode":20000000,"msg":"","data":{"meta":{"etag":"4cb5a3cd5141158defe3827d7a74479e","expire":1800,"ctime":1416897731},"data":{"code":304,"msg":"304 Not Modified"}}}'
                self.send_response(200)
                self.end_headers()
                try:
                        self.wfile.write(message)
                except Exception,e:
                        print "========wfile.write excepting======", str(e)
                interval=random.choice([0.1, 0.2, 0.0])
                aa=str(interval)
                inter=float(aa)
                time.sleep(inter)
                return


if __name__=='__main__':
	ip = "10.13.1.134"
	port = 10004
	httpd = ThreadingSimpleServer((ip, port), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (ip, port)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                print "Bye,bye"
        except Exception, e:
                print "=====connection exception===",str(e), "~~~~~connection exception"
        print time.asctime(), "Server Stops - %s:%s" % (ip, port)


