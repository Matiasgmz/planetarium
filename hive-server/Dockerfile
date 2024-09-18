# FROM bde2020/hadoop-base:2.0.0-hadoop3.2.1-java8
 
# # Installer Hive
# ENV HIVE_VERSION=3.1.3
# ENV HIVE_HOME=/opt/hive
# ENV HADOOP_HOME=/opt/hadoop

# RUN apt-get update
# RUN apt-get install -y wget

# # RUN wget https://downloads.apache.org/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz \
# # && tar -xzf apache-hive-${HIVE_VERSION}-bin.tar.gz -C /opt/ \
# # && mv /opt/apache-hive-${HIVE_VERSION}-bin ${HIVE_HOME} \
# # && rm apache-hive-${HIVE_VERSION}-bin.tar.gz
 
# # Configurer Hive
# RUN mkdir -p /opt/hive/logs /opt/hive/tmp /opt/hive/warehouse \
# && chmod 777 /opt/hive/logs /opt/hive/tmp /opt/hive/warehouse
 
# ENV PATH=$HIVE_HOME/bin:$PATH
 
# # Configurer les propriétés de Hive pour utiliser HBase
# COPY hive-site.xml ${HIVE_HOME}/conf/
# COPY hbase-site.xml ${HADOOP_HOME}/etc/hadoop/
 
# # Installer le client HBase
# RUN wget https://archive.apache.org/dist/hbase/2.2.7/hbase-2.2.7-bin.tar.gz \
# && tar -xzf hbase-2.2.7-bin.tar.gz -C /opt/ \
# && rm hbase-2.2.7-bin.tar.gz \
# && ln -s /opt/hbase-2.2.7 /opt/hbase
 
# ENV HBASE_HOME=/opt/hbase
# ENV PATH=$HBASE_HOME/bin:$PATH
 
# # Exposer les ports pour Hive
# EXPOSE 10000 10002
 
# # Démarrer Hive avec HBase
# CMD ["hive", "--service", "metastore"]

# Use the latest stable Debian image
FROM debian:latest
 
# Environment variables for Hadoop, HBase, and Hive versions
ENV HADOOP_VERSION=3.4.0
ENV HBASE_VERSION=2.6.0
ENV HIVE_VERSION=4.0.0
ENV HADOOP_HOME=/opt/hadoop
ENV HBASE_HOME=/opt/hbase
ENV HIVE_HOME=/opt/hive
ENV PATH=$PATH:$HADOOP_HOME/bin:$HBASE_HOME/bin:$HIVE_HOME/bin
# RUN echo "deb http://archive.debian.org/debian stretch main" >> /etc/apt/sources.list

# RUN echo "deb-src http://archive.debian.org/debian stretch main" >> /etc/apt/sources.list 
# RUN echo "deb http://archive.debian.org/debian stretch-backports main" >> /etc/apt/sources.list 
# RUN echo "deb http://archive.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list RUN echo  "deb-src http://archive.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list
 
# Install necessary packages
RUN apt-get update && apt-get install -y \
wget
 
# Download and install Hadoop
RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xvzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} /opt/hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz
 
# Download and install HBase
RUN wget https://downloads.apache.org/hbase/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz && \
    tar -xvzf hbase-${HBASE_VERSION}-bin.tar.gz && \
    mv hbase-${HBASE_VERSION} /opt/hbase && \
    rm hbase-${HBASE_VERSION}-bin.tar.gz
 
# Download and install Hive
RUN wget https://downloads.apache.org/hive/hive-${HIVE_VERSION}/apache-hive-${HIVE_VERSION}-bin.tar.gz && \
    tar -xvzf apache-hive-${HIVE_VERSION}-bin.tar.gz && \
    mv apache-hive-${HIVE_VERSION}-bin /opt/hive && \
    rm apache-hive-${HIVE_VERSION}-bin.tar.gz
 
# Set Hadoop configuration
COPY core-site.xml $HADOOP_HOME/etc/hadoop/
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/
COPY yarn-site.xml $HADOOP_HOME/etc/hadoop/
COPY mapred-site.xml $HADOOP_HOME/etc/hadoop/
 
# Set HBase configuration
COPY hbase-site.xml $HBASE_HOME/conf/
 
# Set Hive configuration
COPY hive-site.xml $HIVE_HOME/conf/
 
# Expose ports for HDFS, YARN, HBase, and Hive
EXPOSE 50070 8088 16010 10000
 
# Start Hadoop services (Namenode, Datanode, ResourceManager, and NodeManager)
CMD service ssh start && \
    $HADOOP_HOME/bin/hdfs namenode -format && \
    $HADOOP_HOME/sbin/start-dfs.sh && \
    $HADOOP_HOME/sbin/start-yarn.sh && \
    $HBASE_HOME/bin/start-hbase.sh && \
    hive --service metastore