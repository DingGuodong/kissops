from django.test import TestCase

# Create your tests here.
dd = {'hosts_user_is_privilege': 0, 'hosts_type': 0, 'hosts_ip_private': u'10.6.28.28', 'hosts_ip_public': u'None',
      'hosts_user_is_sudo': 0, 'hosts_user': u'test', 'hosts_user_password': u'root123', 'hosts_hosts': u'10.6.28.28'}

for k, v in dd.items():
    print k, v
