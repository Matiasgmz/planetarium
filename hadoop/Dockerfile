# Utiliser une image de base Ubuntu
FROM ubuntu:20.04

# Définir les variables d'environnement
ENV HADOOP_VERSION=3.4.0
ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# Installer les dépendances nécessaires
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk ssh rsync curl && \
    apt-get clean

# Télécharger et installer Hadoop
RUN curl -O https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} /usr/local/hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Configurer Hadoop
COPY core-site.xml $HADOOP_CONF_DIR/core-site.xml
COPY hdfs-site.xml $HADOOP_CONF_DIR/hdfs-site.xml
COPY mapred-site.xml $HADOOP_CONF_DIR/mapred-site.xml
COPY yarn-site.xml $HADOOP_CONF_DIR/yarn-site.xml

# Formater le NameNode (nécessaire avant de démarrer HDFS)
RUN $HADOOP_HOME/bin/hdfs namenode -format

ADD run.sh /run.sh
RUN chmod a+x /run.sh && mkdir -p /var/run/sshd && echo 'mkdir -p /var/run/sshd' >> /etc/rc.local

# Exposer les ports nécessaires
EXPOSE 9870 8088 9000

CMD ["/app/hadoop/sbin/start-dfs.sh"]