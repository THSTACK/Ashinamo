#!/usr/bin/env python
# -*- coding:utf-8 -*-
""" ��ȡ�ڴ�����, �� /proc/meminfo �ļ� """
""" @Author: baoyiluo@gmail.com
    @Site: www.pythonpie.com
    @Date: 2013-05-23
    @Version: v1.2
    @Note:
        /proc/meminfo ���������ݵĽ��ͣ�
[root@ashinamo ~]# head -n 4 /proc/meminfo
MemTotal:        1017812 kB
MemFree:           67768 kB
Buffers:           10280 kB
Cached:           283708 kB
MemTotal:���ڴ��С
MemFree:�����ڴ��С
Buffers��Cached�����̻���Ĵ�С
Buffers��Cached������
buffers��ָ���������豸���Ļ����С����ֻ��¼�ļ�ϵͳ��metadata�Լ�
tracking in-flight pages.
cached���������ļ������塣

"""


def get_ProcMeminfo():
    """ ��ȡ�ڴ�����
    @Return: (status, msgs, results)
            status = INT, Fuction execution status, 0 is normal,
                     other is failure.
            msgs = STRING, If status equal to 0, msgs is '',
                   otherwise will be filled with error message.
            results = DICT {
                    'memtotal': 1017812, #��λ���� KB
                    'memused': 283708
            }
    """

    now_data = {}
    status = 0
    msgs = ""
    results = ""
    try:
        fp_o = file('/proc/meminfo')
        raw_data = fp_o.read()
        fp_o.close()
        temps = raw_data.strip().split('\n')
        for temp in temps:
            tmp = temp.split()
            now_data[tmp[0]] = tmp[1]
        results = {}
        results['memtotal'] = int(now_data['MemTotal:'])
        # results['memused']=int(now_data['MemTotal:'])-int(now_data['MemFree:'])-int(now_data['Buffers:'])-int(now_data['Cached:'])
        results['memused'] = int(now_data['MemTotal:']) -\
            int(now_data['MemFree:'])
        results['buffers'] = int(now_data['Buffers:'])
        results['cached'] = int(now_data['Cached:'])
        return (status, msgs, results)
    except Exception, e:
        return (-1, 'data error!' + e, '')

if __name__ == "__main__":
    print get_ProcMeminfo()
