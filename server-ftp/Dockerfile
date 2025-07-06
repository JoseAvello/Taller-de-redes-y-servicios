FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y build-essential git autoconf libtool libpam0g-dev libssl-dev

RUN git clone https://github.com/proftpd/proftpd.git /opt/proftpd

WORKDIR /opt/proftpd
RUN ./configure --prefix=/usr/local/proftpd && make && make install

RUN useradd -m ftpuser && echo "ftpuser:ftppassword" | chpasswd

RUN mkdir -p /home/ftpuser/files && chown -R ftpuser:ftpuser /home/ftpuser/files

COPY proftpd.conf /usr/local/proftpd/etc/proftpd.conf

EXPOSE 21 30000-30010

CMD ["/usr/local/proftpd/sbin/proftpd", "-n", "-c", "/usr/local/proftpd/etc/proftpd.conf"]
