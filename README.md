An Ambari Service for Impala
====

## Support Version
- Impala 2.6 +
- Hadoop 2.6 +

## Create MPACK gzip file

The files and directories structure of the Management Pack for the Impala service is as follows.

```
/ -+--- mpack.json
   |
   +--- /addon-services 
   |    +--- /IMPALA 
   |         +--- /2.12.0 
   |              +--- metainfo.xml
   |
   +--- /common-services
        +--- /IMPALA
             +--- /2.12.0
                  +--- metainfo.xml
                  +--- alerts.json
                  +--- kerberos.json
                  +--- /configuration
                  |    +--- impala-env.xml
                  +--- /package
                       +--- /files
                       |    +--- hadoop-azure-datalake-2.6.0-cdh5.12.0.jar
                       +--- /scripts
                       |    +--- impala_base.py
                       |    +--- impala-catalog.py
                       |    +--- impala-daemon.py
                       |    +--- impala-state-store.py
                       |    +--- params.py
                       +--- /templates 
                            +--- impala.j2
                            +--- init_lib.sh.j2

```
Refer to the above structure and create ambari-impala-mpack-2.12.0-1012.tar.gz file using gzip.

## Install Impala two ways:

### 1. To download the Impala service folder, run below    

```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
sudo git clone https://github.com/cas-bigdatalab/ambari-impala-service.git /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/IMPALA        
```

### 2. MPACK 
```
ambari-server install-mpack --mpack=ambari-impala-mpack-2.12.0-1012.tar.gz -v
```

## local repository
Make your local repository.Download software from https://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/5/

software list as below:
```
bigtop-jsvc-0.6.0+cdh5.15.1+927-1.cdh5.15.1.p0.4.el6.x86_64.rpm
bigtop-jsvc-debuginfo-0.6.0+cdh5.15.1+927-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-0.20-conf-pseudo-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-0.20-mapreduce-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-0.20-mapreduce-jobtracker-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-0.20-mapreduce-jobtrackerha-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-0.20-mapreduce-tasktracker-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-0.20-mapreduce-zkfc-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-client-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-conf-pseudo-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-debuginfo-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-doc-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-datanode-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-fuse-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-journalnode-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-namenode-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-nfs3-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-secondarynamenode-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-hdfs-zkfc-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-httpfs-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-kms-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-kms-server-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-libhdfs-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-libhdfs-devel-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-mapreduce-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-mapreduce-historyserver-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-yarn-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-yarn-nodemanager-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-yarn-proxyserver-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hadoop-yarn-resourcemanager-2.6.0+cdh5.15.1+2822-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hbase-1.2.0+cdh5.15.1+470-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hbase-doc-1.2.0+cdh5.15.1+470-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hbase-master-1.2.0+cdh5.15.1+470-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hbase-regionserver-1.2.0+cdh5.15.1+470-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hbase-rest-1.2.0+cdh5.15.1+470-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hbase-thrift-1.2.0+cdh5.15.1+470-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-beeswax-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-common-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-doc-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-hbase-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-impala-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-pig-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-plugins-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-rdbms-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-search-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-security-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-server-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-spark-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-sqoop-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
hue-zookeeper-3.9.0+cdh5.15.1+8420-1.cdh5.15.1.p0.4.el6.x86_64.rpm
impala-2.12.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
impala-catalog-2.12.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
impala-debuginfo-2.12.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
impala-server-2.12.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
impala-shell-2.12.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
impala-state-store-2.12.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
impala-udf-devel-2.12.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
kudu-1.7.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
kudu-client-devel-1.7.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
kudu-client0-1.7.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
kudu-debuginfo-1.7.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
kudu-master-1.7.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
kudu-tserver-1.7.0+cdh5.15.1+0-1.cdh5.15.1.p0.4.el6.x86_64.rpm
zookeeper-3.4.5+cdh5.15.1+149-1.cdh5.15.1.p0.4.el6.x86_64.rpm
zookeeper-debuginfo-3.4.5+cdh5.15.1+149-1.cdh5.15.1.p0.4.el6.x86_64.rpm
zookeeper-native-3.4.5+cdh5.15.1+149-1.cdh5.15.1.p0.4.el6.x86_64.rpm
zookeeper-server-3.4.5+cdh5.15.1+149-1.cdh5.15.1.p0.4.el6.x86_64.rpm
```

## Restart Ambari  
sudo service ambari-server restart


## HDFS config
we need add below config to /etc/hadoop/conf/core-site.xml
```
<property>
    <name>dfs.client.read.shortcircuit</name> 
   <value>true</value>
</property>

<property>
    <name>dfs.client.read.shortcircuit.skip.checksum</name>
        <value>false</value>
</property>

<property> 
    <name>dfs.datanode.hdfs-blocks-metadata.enabled</name> 
    <value>true</value>
</property>
```
we need add below config to /etc/hadoop/conf/hdfs-site.xml
```
<property>
    <name>dfs.datanode.hdfs-blocks-metadata.enabled</name> 
    <value>true</value>
</property>
<property> 
    <name>dfs.block.local-path-access.user</name> 
    <value>impala</value>
</property>
<property>
    <name>dfs.client.file-block-storage-locations.timeout.millis</name>
    <value>60000</value>
</property>
```
add config info through webui

![Image](../master/screenshots/core-site.png?raw=true)
![Image](../master/screenshots/hdfs-site.png?raw=true)

restart hadoop and restart impala

## SUMMARY
![Image](../master/screenshots/summary.png?raw=true)

## NOTICE
- make sure your hive server normally
- hdfs and hive conf file is sync to /etc/impala/conf

## Some error note:
- NoSuchMethodError:setCaching
![Image](../master/screenshots/impala-error.jpg?raw=true)
Impala rely on Cloudrea Hbase Jar ,please use relevant jar.
