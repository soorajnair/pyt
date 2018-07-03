FROM ubuntu:16.04
ENV JAVA_HOME=\"/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java\"
EXPOSE 8080
RUN apt-get update && \
apt-get install -y default-jre && \
apt-get install -y default-jdk && \
apt-get install -y wget && \
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add - && \
sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list' && \
apt-get update && \
apt-get install -y jenkins
ENTRYPOINT service jenkins start && \
apt-get update && \
tail -f /var/log/jenkins/jenkins.log\

